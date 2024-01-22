from django.contrib import admin
from .models import stock

class stockAdmin(admin.ModelAdmin):
    list_display = ['item', 'amount']

admin.site.register(stock, stockAdmin)
