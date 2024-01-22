from django.shortcuts import render, redirect
from .models import event
from .forms import EventForm
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt


def createEvent(request):
    """the function creat a new event according to the request of the user(admin only) and save it in the database"""
    if request.method == 'GET':
        return render(request, 'Event/createEvent.html', {'form': EventForm()})
    else:
        form = EventForm(request.POST)  # creat a form for the event
        new_event = form.save(commit=False)
        new_event.save()  # saving the new event in the database
        return redirect('Event:all_events')  # refers to the page of all events


def all_events(request):
    """""the function presents all events"""
    events = event.objects.order_by('-date')
    return render(request, 'Event/all_events.html', {'events': events})


def deleteEvent(request, event_id):
    """the function delete a event according to the request of the user (admin only) and delete it
         from the database """
    Event = event.objects.get(pk=event_id)
    Event.delete()  # delete the report from the database
    return redirect('Event:all_events')  # refers to the page of all events


def Event_detail(request, id=None):
    """the function presents a single page of each event according to the user request"""
    event_obj = None
    if id is not None:
        event_obj = event.objects.get(id=id)
    context = {"object": event_obj}
    return render(request, 'Event/event_detail.html', context=context)


def export_pdf(request):
    """Function for exporting a pdf document from the system"""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)  # creat a new page
    textob = c.beginText()  # creat a text object
    textob.setTextOrigin(inch, inch)  # set the sizes of the text
    pdfmetrics.registerFont(TTFont('David', 'David.ttf'))
    textob.setFont("David", 14)  # set the font of the text

    events = event.objects.all()  # designate the model
    lines = []  # creat a new list for the objects
    # print all data we need
    for ev in events:
        lines.append('Title: ' + ev.name[::-1])
        lines.append('Date: ' + str(ev.date))
        lines.append('Details: ' + ev.text[::-1])
        lines.append('_______________________________________')
        lines.append('    ')

    textob.textLine("Monthly event report of the 'Bait Ham' association:")  # the title of the file
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()  # save the file
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='events.pdf')


def export_excel(request):
    """Function for exporting an excel document from the system"""
    response = HttpResponse(content_type='events/excel')
    response['Content-Disposition'] = 'attachment; filename=events' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('events')  # give a name to the sheet
    row_num = 2  # initial row for objects
    font_style = xlwt.XFStyle()  # set the font of the text
    font_style.font.bold = True

    ws.write(0, 0, 'Monthly event report of the "Bait Ham" association:', font_style)  # the title of the file

    columns = ['Title', 'Date', 'Details']  # the columns in the table
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # save all the data we need from database
    rows = event.objects.all().values_list('name', 'date', 'text')

    font_style = xlwt.XFStyle()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)  # enter all the data to the table

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    wb.save(response)  # save the file

    return response
