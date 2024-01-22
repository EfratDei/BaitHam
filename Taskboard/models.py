from django.db import models
from django.contrib.auth.models import User
from datetime import date


class list_task(models.Model):
    date = models.DateField(default=date.today,verbose_name="תאריך")
    name = models.CharField(max_length=100, blank=False,verbose_name="כותרת")
    text = models.TextField(max_length=5000, blank=False,verbose_name="תיאור")
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "לוח מטלות"