from pyexpat import model
from django.db import models


class Event(models.Model):
  event_id=models.AutoField
  name=models.CharField(max_length=32)
  email=models.EmailField()
  desc=models.TextField()  
  address=models.CharField(max_length=32)
  From=models.DateTimeField()
  To=models.DateTimeField()
  Registration_Deadline=models.DateTimeField()
  Host_Email=models.EmailField()

class Participant(models.Model):
  participant_id=models.AutoField
  name=models.CharField(max_length=32)
  Contact_no=models.IntegerField()
  Email_ID=models.EmailField()
  Event_name=models.CharField(max_length=32)