from django.contrib import admin
from .models import Donations

class DonationsAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount']


admin.site.register(Donations, DonationsAdmin)
