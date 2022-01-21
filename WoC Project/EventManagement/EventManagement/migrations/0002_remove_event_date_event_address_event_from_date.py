# Generated by Django 4.0.1 on 2022-01-19 11:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]