# Generated by Django 4.0.1 on 2022-01-19 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0003_event_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='from_date',
        ),
        migrations.AddField(
            model_name='event',
            name='From',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Host_Email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Registration_Deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
