from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from adopter import views

app_name = 'adopter'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home, name='home'),
    path('admin_page/', views.admin, name='admin_page'),
    path('reports',views.reports,name='reports'),
    path('adopter/', views.contact_us, name='contact_us'),
    path('Report/',include('Report.urls')),
    path('Article/',include('Article.urls')),
    path('success_story/',include('success_story.urls')),
    path('Animal/',include('Animal.urls'), name='Animal'),
    path('volunteer/',include('volunteer.urls')),
    path('Event/',include('Event.urls')),
    path('Donations/',include('Donations.urls'), name='Donations)'),
    path('forum/', include('forum.urls'), name='forum'),
    path('Taskboard/',include('Taskboard.urls'), name='Taskboard)'),
    path('Supplier/',include('Supplier.urls'),name='Supplier'),
    path('Stock/',include('Stock.urls'),name='Stock'),
    path('contact_us/',views.contact_us,name='contact_us'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
