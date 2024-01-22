import django_filters
from .models import animal


class animalFilter(django_filters.FilterSet):
    class Meta:
        model = animal
        fields = ['species', 'sex']
