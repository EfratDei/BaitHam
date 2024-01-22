from django.contrib import admin
from .models import articles


class articlesAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'genre']

admin.site.register(articles, articlesAdmin)