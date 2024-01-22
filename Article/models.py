from django.db import models


class articles(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    type = models.CharField(max_length=10, choices=[("cat", "חתול"), ("dog", "כלב")], verbose_name="סוג")
    genre = models.CharField(max_length=200,choices=[("adoption", "אימוץ"), ( "info","מידע"), ("training", "אילוף"),("other", "אחר")], default="other",verbose_name="ז'אנר")
    link = models.CharField(max_length=2000, default=None)
    def __str__(self):
        return f'name: {self.name}\n type: {self.type}'

    class Meta:
        verbose_name_plural = "מאמרים"