# Generated by Django 4.0.1 on 2022-01-19 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0002_remove_event_date_event_address_event_from_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='To',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
