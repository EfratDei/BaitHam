# Generated by Django 4.0 on 2021-12-23 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20211216_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='discuss',
            field=models.CharField(default=None, max_length=1000, verbose_name='התגובה'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='forum.forum', verbose_name='הנושא עליו תרצה להגיב'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='תאריך'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.CharField(blank=True, max_length=1000, verbose_name='תיאור'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='email',
            field=models.CharField(max_length=200, null=True, verbose_name='אימייל'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.CharField(default='anonymous', max_length=200, verbose_name='שם'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='topic',
            field=models.CharField(max_length=300, verbose_name='נושא'),
        ),
    ]