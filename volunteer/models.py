import datetime
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today, verbose_name="תאריך ")
    entrance_time = models.TimeField(verbose_name="שעת כניסה ", default=None)
    leaving_time = models.TimeField(default=datetime.datetime.now, verbose_name="שעת יציאה ")

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = "נוכחות מתנדבים"
