from django.urls import path
from . import views

app_name = 'Stock'

urlpatterns = [

    path('export_pdf', views.export_pdf, name="export_pdf"),
    path('export_excel', views.export_excel, name="export_excel"),
    path('selectStock/', views.selectStock, name='selectStock'),
    path('updateStock/<str:id>', views.updateStock, name='updateStock'),

]
