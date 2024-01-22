from django.forms import ModelForm
from .models import stock


# create a form for stock app

class StockForm(ModelForm):
    class Meta:
        model = stock
        fields = ['amount']

