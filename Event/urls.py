from django.urls import path
from . import views

app_name = 'Event'

urlpatterns = [
    path('all_events/', views.all_events, name='all_events'),
    path('createEvent/', views.createEvent, name='createEvent'),
    path('deleteEvent/<event_id>', views.deleteEvent, name='deleteEvent'),
    path('event_detail/<int:id>', views.Event_detail, name='Event_detail'),
    path('export_pdf', views.export_pdf, name='export_pdf'),
    path('export_excel', views.export_excel, name='export_excel'),
]
