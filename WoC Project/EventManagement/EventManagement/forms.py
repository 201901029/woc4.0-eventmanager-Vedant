from asyncio.windows_events import NULL
from django import forms
from django.forms import ModelForm
from EventManagement.models import Event
from EventManagement.models import Participant
import datetime
class EventForm(ModelForm):
    class Meta:
        model=Event
        fields=("name","email","address","From","To","Registration_Deadline","desc")
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
        fields=("name","Contact_no","Email_ID","Registration_Type","No_of_people")
        widgets={
          "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
         "Contact_no": forms.TextInput(attrs={'class':'form-control','placeholder':'Contact_no'}),
          "Email_ID": forms.EmailInput(attrs={'class':'form-control','placeholder':'Email_ID'}),
          "Registration_Type": forms.RadioSelect(),
        }
        
  
    
      
    
    
            
  
