from asyncio.windows_events import NULL
from django import forms
from django.forms import ModelForm
from EventManagement.models import Event
from EventManagement.models import Participant
from EventManagement.models import EventDashboard
import datetime
class EventForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Event
        fields=("name","email","address","From","To","Registration_Deadline","desc","password")
        widgets={
          "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
          "email": forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
          "desc": forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
          "address": forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
          "From": forms.TextInput(attrs={'class':'form-control','placeholder':'From(MM/DD/YYYY HH:MM:SS)'}),
          "To": forms.TextInput(attrs={'class':'form-control','placeholder':'To(MM/DD/YYYY HH:MM:SS)'}),
          "Registration_Deadline":forms.TextInput(attrs={'class':'form-control','placeholder':'Registration Deadline(MM/DD/YYYY HH:MM:SS)'}),
          }
    def clean_name(self):
        name=self.cleaned_data.get('name')
        for item in Event.objects.all():
          if item.name.lower()==name.lower():
            raise forms.ValidationError('Please Enter Different Event name')
        return name
    
    def clean_To(self):
      To=self.cleaned_data['To']
      From=self.cleaned_data['From']
      if To.replace(tzinfo=None)<From.replace(tzinfo=None):
          raise forms.ValidationError('End time should be greater than start time')
      return To

    def clean_password(self):
      password=self.cleaned_data['password']
      for item in Event.objects.all():
        if item.password==password:
          raise forms.ValidationError('This password is not available. Please enter different password')
        return password  
class ParticipantForm(ModelForm):
    
    class Meta:
        model=Participant
        fields=("name","Contact_no","Email_ID","Registration_Type","No_of_people")
        widgets={
          "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
          "Email_ID": forms.EmailInput(attrs={'class':'form-control','placeholder':'Email_ID'}),
          "Registration_Type": forms.RadioSelect(),
        }

class EventDashboardform(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    class Meta:
      model=EventDashboard
      fields=("Email_ID","password")
      widgets={
          "Email_ID": forms.EmailInput(attrs={'class':'form-control','placeholder':'Email_ID'}),
        }

        
  
    
      
    
    
            
  
