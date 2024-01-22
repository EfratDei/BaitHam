from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .models import SupplierRegistration
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt


def export_pdf(request):
    """Function for exporting a pdf document from the system"""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)  # creat a new page
    textob = c.beginText()  # creat a text object
    textob.setTextOrigin(inch, inch)  # set the sizes of the text
    pdfmetrics.registerFont(TTFont('David', 'David.ttf'))
    textob.setFont("David", 14)  # set the font of the text

    suppliers = SupplierRegistration.objects.all()  # designate the model
    lines = []  # creat a new list for the objects

    # print all data we need
    for supplier in suppliers:
        lines.append('Supplier: ' + supplier.Supplier_name)
        lines.append('Owner: ' + supplier.owner_name)
        lines.append('Address: ' + supplier.address)
        lines.append('Phone number: ' + supplier.phone_number)
        lines.append('    ')
        lines.append('_______________________________________')
        lines.append('    ')

    textob.textLine("Suppliers report of the 'Bait Ham' association:")  # the title of the file
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()  # save the file
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='suppliers.pdf')


def export_excel(request):
    """Function for exporting an excel document from the system"""
    response = HttpResponse(content_type='suppliers/excel')
    response['Content-Disposition'] = 'attachment; filename=suppliers' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('suppliers')  # give a name to the sheet
    row_num = 2  # initial row for objects
    font_style = xlwt.XFStyle()  # set the font of the text
    font_style.font.bold = True

    ws.write(0, 0, 'Suppliers report of the "Bait Ham" association:', font_style)  # the title of the file

    columns = ['Supplier', 'Owner', 'Address', 'Phone number']  # the columns in the table

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # save all the data we need from database
    rows = SupplierRegistration.objects.all().values_list('Supplier_name', 'owner_name', 'address', 'phone_number')

    font_style = xlwt.XFStyle()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)  # enter all the data to the table

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    wb.save(response)  # save the file

    return response
