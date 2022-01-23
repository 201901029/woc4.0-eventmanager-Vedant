from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models


class Event(models.Model):
  event_id=models.AutoField
  name=models.CharField(max_length=32,blank=True)
  email=models.EmailField(blank=True)
  desc=models.TextField(blank=True)  
  address=models.CharField(max_length=32,blank=True)
  From=models.DateTimeField(blank=True)
  To=models.DateTimeField(blank=True)
  Registration_Deadline=models.DateTimeField(blank=True)
  Host_Email=models.EmailField(blank=True)

temp=(('Group','Group'),
      ('Individual','Individual')
     )
class Participant(models.Model):
  participant_id=models.AutoField
  name=models.CharField(max_length=32,blank=True)
  Contact_no=models.IntegerField(blank=True)
  Email_ID=models.EmailField(blank=True)
  Event_name=models.CharField(max_length=32,blank=True)
  Registration_Type=models.CharField(max_length=32,blank=True,choices=temp)
  No_of_people=models.IntegerField(blank=True)