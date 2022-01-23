from asyncio.windows_events import NULL
from django import forms
from django.forms import ModelForm
from EventManagement.models import Event
from EventManagement.models import Participant
import datetime
class EventForm(ModelForm):
    class Meta:
        model=Event
        fields=("name","email","desc","address","From","To","Registration_Deadline","Host_Email")
        widgets={
          "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
          "email": forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
          "desc": forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
          "address": forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
          "From": forms.TextInput(attrs={'class':'form-control','placeholder':'From(MM/DD/YYYY HH:MM:SS)'}),
          "To": forms.TextInput(attrs={'class':'form-control','placeholder':'To(MM/DD/YYYY HH:MM:SS)'}),
          "Registration_Deadline":forms.TextInput(attrs={'class':'form-control','placeholder':'Registration Deadline(DD/MM/YYYY HH:MM:SS)'}),
          "Host_Email":forms.TextInput(attrs={'class':'form-control','placeholder':'Host Email'},),
        }
    def clean_name(self):
        name=self.cleaned_data.get('name')
        for item in Event.objects.all():
          if item.name==name:
            raise forms.ValidationError('Please Enter Different Event name')
        return name
    
    def clean_To(self):
      To=self.cleaned_data['To']
      From=self.cleaned_data['From']
      if To.replace(tzinfo=None)<From.replace(tzinfo=None):
          raise forms.ValidationError('End time should be greater than start time')
      return To
class ParticipantForm(ModelForm):
    
    class Meta:
        model=Participant
        fields=("name","Contact_no","Event_name","Email_ID","Registration_Type","No_of_people")
        widgets={
          "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
         
          "Email_ID": forms.EmailInput(attrs={'class':'form-control','placeholder':'Email_ID'}),
          "Registration_Type": forms.RadioSelect(),
          "Event_name": forms.TextInput(attrs={'class':'form-control','placeholder':'Event_name'}),
          
        }
    def clean_Email_ID(self):
        flag=0
        Email_ID=self.cleaned_data['Email_ID']
        Event_name=self.cleaned_data['Event_name']
        if(Email_ID==""):
           raise forms.ValidationError('This field is mandatory')
        for item in Participant.objects.all():
          if item.Email_ID==Email_ID:
            if item.Event_name==Event_name:
              flag=1
        if flag==1:
          raise forms.ValidationError('This email-ID already exists')
        return Email_ID
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if(name==""):
          raise forms.ValidationError('This field is mandatory')
        return name

    def clean_Event_name(self):
        Event_name=self.cleaned_data.get('Event_name')
        flag=0
        if(Event_name==""):
          raise forms.ValidationError('This field is mandatory')
        for item in Event.objects.all():
          if item.name==Event_name:
            flag=1
        if(flag==0):
          raise forms.ValidationError('This event does not exists')
        return Event_name
      
    
    
            
  
