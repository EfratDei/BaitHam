from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_month(value):
    if not 1 <= value < 12:
        raise ValidationError(
            _('%(value)s is not a valid month'),
            params={'value': value},
        )


class animal(models.Model):
    Sex_Choice = [('M', 'זכר'), ('F', 'נקבה')]
    Species_choice = [('dog', 'כלב'), ('cat', 'חתול')]
    Adoption_ready = [('N', 'לא'), ('Y', 'כן')]

    name = models.CharField(max_length=100, verbose_name="שם")  # Name of the Pet
    submitter = models.CharField(max_length=100, null=True, verbose_name="הוכנס על ידי")  # Name of Submitter
    species = models.CharField(max_length=30, choices=Species_choice, blank=False,
                               default='Dog', verbose_name="סוג")  # What is the Pet species? (dog, cat)
    breed = models.CharField(max_length=30, blank=False, verbose_name="גזע")  # Pet's breed
    description = models.TextField(blank=False, verbose_name="תיאור")  # Description like where was found etc...
    sex = models.CharField(max_length=30, choices=Sex_Choice, default='M', blank=False, verbose_name="מין")  # Gender
    submission_date = models.DateTimeField(auto_now_add=True, verbose_name="תאריך קליטה")  # Date submitted to shelter
    image = models.ImageField(upload_to='Animal', blank=True, default='default.png',
                              verbose_name="העלאת תמונה")  # for animal images
    Adoption = models.CharField(max_length=30, choices=Adoption_ready, blank=False, default='No',
                                verbose_name="מוכן לאימוץ")  # adoption filter

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "מאגר בעלי חיים"


class Stats(models.Model):
    created = models.IntegerField(blank=True, default=0)
    deleted = models.IntegerField(blank=True, default=0)
    current = models.IntegerField(blank=True, default=0)
    month = models.IntegerField(blank=True, default=1, validators=[validate_month])

    class Meta:
        verbose_name_plural = "סטטיסטיקה"
