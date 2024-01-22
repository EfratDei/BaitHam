from django.forms import ModelForm
from .models import event


# create a form for the event app

class EventForm(ModelForm):
    class Meta:
        model = event
        fields = ['name', 'date', 'text', 'image']
