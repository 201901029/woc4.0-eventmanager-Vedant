# Generated by Django 4.0.1 on 2022-01-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0012_alter_event_from_alter_event_registration_deadline_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_ID', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]