import django_filters
from .models import stock


class stockFilter(django_filters.FilterSet):
    class Meta:
        model = stock
        fields = ['item']
