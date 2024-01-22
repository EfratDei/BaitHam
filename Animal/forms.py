from django.forms import ModelForm, Form
from django import forms

from .models import animal


class Add_Animal_Form(ModelForm):
    class Meta:
        model = animal
        fields = ['name', 'submitter', 'species', 'breed', 'description', 'sex', 'Adoption', 'image']
        widgets = {
        'description': forms.Textarea(attrs={'placeholder': 'הכנס תיאור מפורט ככל הניתן'}),
        }

