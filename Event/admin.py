from django.contrib import admin
from .models import event


class eventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'image']

admin.site.register(event, eventAdmin) # add the model to the management page (admin)
