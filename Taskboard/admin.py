from django.contrib import admin
from .models import list_task

class tasksAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'user']

admin.site.register(list_task,tasksAdmin)

