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
list=Event.objects.all()
temp=(('Group','Group'),
      ('Individual','Individual')
     )
class Participant(models.Model):
  participant_id=models.AutoField
  name=models.CharField(max_length=32,blank=True,null=True)
  Contact_no=models.IntegerField(blank=True,null=True)
  Email_ID=models.EmailField(blank=True,null=True)
  Event_name=models.CharField(max_length=32,blank=True,null=True,choices=[(x.name, x.name) for x in list])
  Registration_Type=models.CharField(max_length=32,blank=True,null=True,choices=temp)
  No_of_people=models.IntegerField(blank=True,null=True)