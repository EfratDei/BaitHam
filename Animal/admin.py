from django.contrib import admin
from .models import animal, Stats


class animalAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'sex', 'submission_date', 'Adoption']


class StatsAdmin(admin.ModelAdmin):
    list_display = ['created', 'deleted', 'current', 'month']


admin.site.register(animal, animalAdmin)
admin.site.register(Stats, StatsAdmin)
