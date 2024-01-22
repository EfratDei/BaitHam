from django.contrib import admin
from .models import attendance


class attendanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']


admin.site.register(attendance, attendanceAdmin)
