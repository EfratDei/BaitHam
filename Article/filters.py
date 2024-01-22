import django_filters
from .models import articles


class articleFilter(django_filters.FilterSet):
    class Meta:
        model = articles
        fields = ['type', 'genre']