from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import AttendanceForm
from .models import attendance
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt


def logoutuser(request):
    """function for disconnecting the user from the system"""
    if request.method == 'POST':
        logout(request)
    return redirect('volunteer:loginuser')


def loginuser(request):
    """function for connecting the user to the system"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # check if the details is valid
            user = form.get_user()
            login(request, user)  # connect the user to the system
            return redirect('home')  # refer to the homepage
        else:
            # if the username or password are invalid, a message will appear accordingly
            return render(request, 'volunteer/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'username and password did not match'})
    else:
        form = AuthenticationForm(request)
        context = {'form': form}
    return render(request, 'volunteer/loginuser.html', context)


def update(request):
    """A function that allows the volunteer to report volunteer hours"""
    if request.method == 'GET':
        return render(request, 'volunteer/updateAttend.html', {'form': AttendanceForm()})  # refer to attendance report page
    else:
        form = AttendanceForm(request.POST)  # creat a form from attendance model
        if form.is_valid():
            new_attend = form.save(commit=False)
            new_attend.user = request.user  # link between the report and the logged in user
            new_attend.save()  # save the report in the database
            messages.success(request, 'דיווח התווסף בהצלחה!')
            return redirect('volunteer:update')  # refer to the homepage
        else:
            return render(request, 'volunteer/updateAttend.html',
                          {'form': AttendanceForm(), 'error': 'קלט לא תקין'})


def export_pdf(request):
    """Function for exporting a pdf document from the system"""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)  # creat a new page
    textob = c.beginText()  # creat a text object
    textob.setTextOrigin(inch, inch)  # set the sizes of the text
    pdfmetrics.registerFont(TTFont('David', 'David.ttf'))
    textob.setFont("David", 14)  # set the font of the text

    Attendance = attendance.objects.filter(user=request.user)  # designate the model

    lines = []  # creat a new list for the objects
    # print all data we need
    for obj in Attendance:
        lines.append('Date: ' + str(obj.date))
        lines.append('Entrance time: ' + str(obj.entrance_time))
        lines.append('Leaving time ' + str(obj.leaving_time))
        lines.append('_____________________________________________')
        lines.append('    ')

    name = request.user.first_name  # save the name of the logged in user
    textob.textLine("Attendance report for last month, for the volunteer: " + name)  # the title of the file
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()  # save the file
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='attendance.pdf')


def export_excel(request):
    """Function for exporting an excel document from the system"""
    response = HttpResponse(content_type='attendance/excel')
    response['Content-Disposition'] = 'attachment; filename=attendance' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('attendance')  # give a name to the sheet
    row_num = 2  # initial row for objects
    font_style = xlwt.XFStyle()  # set the font of the text
    font_style.font.bold = True
    name = request.user.first_name
    ws.write(0, 0, 'Attendance report for last month, for the volunteer: ' + name, font_style)  # the title of the file

    columns = ['Date', 'Entrance time', 'Leaving time']  # the columns in the table
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # save all the data we need from database
    rows = attendance.objects.filter(user=request.user).values_list('date', 'entrance_time', 'leaving_time')

    font_style = xlwt.XFStyle()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)  # enter all the data to the table

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    wb.save(response)  # save the file

    return response
