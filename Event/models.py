from django.db import models
from datetime import date


# create a new model for event app

class event(models.Model):
    name = models.CharField(max_length=100,verbose_name="שם")  # the name of the event
    date = models.DateField(default=date.today,verbose_name="תאריך")  # the date of the event
    text = models.TextField(blank=True, verbose_name="תיאור")  # the content of the event
    image = models.ImageField(upload_to='Event', blank=True, verbose_name="תמונה")  # photo of the event

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "אירועי עמותה"