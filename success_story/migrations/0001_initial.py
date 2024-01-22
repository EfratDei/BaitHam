# Generated by Django 4.0 on 2022-01-03 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='תאריך')),
                ('name', models.CharField(max_length=100, verbose_name='שם')),
                ('text', models.TextField(max_length=5000, verbose_name='תיאור')),
            ],
            options={
                'verbose_name_plural': 'stories',
            },
        ),
    ]
