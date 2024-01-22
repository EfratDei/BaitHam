from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .models import stock
from .forms import StockForm
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt
from .filters import stockFilter
from django.contrib import messages


def selectStock(request):
    """the function update an item in the stock according to the request of the user and save it in the database"""
    if request.method == 'GET':
        Stock = stock.objects.all()
        myfilter = stockFilter(request.GET, queryset=Stock)
        Stock = myfilter.qs
        context = {'Stock': Stock, 'myfilter': myfilter}
        return render(request, 'Stock/selectStock.html', context)
    if request.method == 'POST':
        Stock = stock.objects.get(item=request.POST['item'])

        return redirect("Stock:updateStock", Stock.id)

    return render(request, 'Stock/selectStock.html')


def updateStock(request, id=None):
    if not id == None:
        Stock = stock.objects.get(id=id)
        form = StockForm(instance=Stock)
        if request.method == 'POST':
            form = StockForm(request.POST, instance=Stock)
            if form.is_valid():
                form.save()
                messages.success(request,'פריט עודכן בהצלחה!')
                return redirect('Stock:selectStock')
        context = {"form": form, "Stock": Stock}
        return render(request, 'Stock/updateStock.html', context=context)
    return redirect('home')


def export_pdf(request):
    """Function for exporting a pdf document from the system"""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)  # creat a new page
    textob = c.beginText()  # creat a text object
    textob.setTextOrigin(inch, inch)  # set the sizes of the text
    pdfmetrics.registerFont(TTFont('David', 'David.ttf'))
    textob.setFont("David", 14)  # set the font of the text

    stocks = stock.objects.all()  # designate the model
    lines = []  # creat a new list for the objects
    # print all data we need
    for st in stocks:
        lines.append('Item: ' + str(st.item))
        lines.append('Amount: ' + str(st.amount))
        lines.append('_______________________________________')

    textob.textLine("Stock report of the 'Bait Ham' association:")  # the title of the file
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()  # save the file
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='stock.pdf')


def export_excel(request):
    """Function for exporting an excel document from the system"""
    response = HttpResponse(content_type='stock/excel')
    response['Content-Disposition'] = 'attachment; filename=stock' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('stock')  # give a name to the sheet
    row_num = 2  # initial row for objects
    font_style = xlwt.XFStyle()  # set the font of the text
    font_style.font.bold = True

    ws.write(0, 0, 'Stock report of the "Bait Ham" association:', font_style)  # the title of the file

    columns = ['Item', 'Amount']  # the columns in the table
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # save all the data we need from database
    rows = stock.objects.all().values_list('item', 'amount')

    font_style = xlwt.XFStyle()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)  # enter all the data to the table

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    wb.save(response)  # save the file

    return response
