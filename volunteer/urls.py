from django.urls import path
from . import views

app_name = 'volunteer'

urlpatterns = [

    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('update/', views.update, name='update'),
    path('export_pdf', views.export_pdf, name='export_pdf'),
    path('export_excel', views.export_excel, name='export_excel'),
]
