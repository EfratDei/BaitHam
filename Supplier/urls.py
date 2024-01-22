from django.urls import path
from .views import export_pdf, export_excel

app_name = 'Supplier'

urlpatterns = [

    path('export_pdf/', export_pdf, name="export_pdf"),
    path('export_excel/', export_excel, name="export_excel"),

]
