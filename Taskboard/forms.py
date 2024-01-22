from django.forms import ModelForm
from .models import list_task

class TaskForm(ModelForm):
    class Meta:
        model = list_task
        fields = ['date', 'name', 'text']

