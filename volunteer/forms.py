from django.forms import ModelForm
from .models import attendance


class AttendanceForm(ModelForm):
    class Meta:
        model = attendance
        fields = ['date', 'entrance_time', 'leaving_time']
