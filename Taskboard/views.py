from django.shortcuts import render, redirect
from .models import list_task
from .forms import TaskForm
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt


def all_task(request):
    tasks = list_task.objects.all()
    return render(request, 'Taskboard/all_task.html', {'tasks': tasks})


def task_detail(request, id=None):
    task_obj = None
    if id is not None:
        task_obj = list_task.objects.get(id=id)
    context = {"object": task_obj}
    return render(request, 'Taskboard/task_detail.html', context=context)


def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.save()
            return redirect('Taskboard:all_task')
    return render(request, 'Taskboard/createTask.html', {'form': TaskForm()})


def assignTask(request, id):
    list_task.objects.filter(id=id).update(user=request.user)
    return redirect('Taskboard:all_task')


def doneTask(request, id):
    list_task.objects.filter(id=id).update(status=True)
    return redirect('Taskboard:all_task')

def deleteTask(request, task_id):
    """the function delete a task according to the request of the user (admin only) and delete it
     from the database """
    task = list_task.objects.get(pk=task_id)
    task.delete()  # delete the task from the database
    return redirect('Taskboard:all_task')  # refers to the page of all tasks

def export_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # creat a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    pdfmetrics.registerFont(TTFont('David', 'David.ttf'))
    textob.setFont("David", 14)

    tasks = list_task.objects.all()  # designate the model
    lines = []  # creat blank link

    for task in tasks:
        lines.append('Date: ' + str(task.date))
        lines.append('Task: ' + task.name[::-1])
        lines.append('Details: ' + task.text[::-1])
        lines.append('Associated to: ' + str(task.user))
        if task.status:
            lines.append('Status: ' + 'המטלה בוצעה'[::-1])
        else:
            lines.append('Status: ' + "המטלה טרם בוצעה"[::-1])
        lines.append('_______________________________________')
        lines.append('    ')

    textob.textLine("Weekly tasks report of the 'Bait Ham' association:")
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='tasks.pdf')


def export_excel(request):
    response = HttpResponse(content_type='tasks/excel')
    response['Content-Disposition'] = 'attachment; filename=tasks' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('tasks')  # give a name to the sheet
    row_num = 2
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.write(0, 0, 'Weekly tasks report of the "Bait Ham" association:', font_style)

    columns = ['Date', 'Task', 'Details', 'Done?']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    rows = list_task.objects.all().values_list('date', 'name', 'text', 'status')

    font_style = xlwt.XFStyle()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    wb.save(response)

    return response
