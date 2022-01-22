from asyncio.windows_events import NULL
from django import forms
from django.forms import ModelForm
from EventManagement.models import Event
from EventManagement.models import Participant

class EventForm(ModelForm):
    class Meta:
        model=Event
        fields=("name","email","desc","address","From","To","Registration_Deadline","Host_Email")
        widgets={
          "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
          "email": forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
          "desc": forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
          "address": forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
          "From": forms.TextInput(attrs={'class':'form-control','placeholder':'From(DD/MM/YYYY HH:MM:SS)'}),
          "To": forms.TextInput(attrs={'class':'form-control','placeholder':'To(DD/MM/YYYY HH:MM:SS)'}),
          "Registration_Deadline":forms.TextInput(attrs={'class':'form-control','placeholder':'Registration Deadline(DD/MM/YYYY HH:MM:SS)'}),
          "Host_Email":forms.TextInput(attrs={'class':'form-control','placeholder':'Host Email'},),
        }
    def clean_name(self):
        name=self.cleaned_data.get('name')
        for item in Event.objects.all():
          if item.name==name:
            raise forms.ValidationError('Please Enter Different Event name')
        return name

class ParticipantForm(ModelForm):
    
    class Meta:
        model=Participant
        fields=("name","Contact_no","Email_ID","Event_name","Registration_Type","No_of_people")
        widgets={
          "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
          "Contact_no": forms.TextInput(attrs={'class':'form-control','placeholder':'Contact_no'}),
          "Email_ID": forms.TextInput(attrs={'class':'form-control','placeholder':'Email_ID'}),
          "Registration_Type": forms.RadioSelect(),
          "Event_name": forms.TextInput(attrs={'class':'form-control','placeholder':'Event_name'}),
        }
    def clean_Email_ID(self):
        Email_ID=self.cleaned_data.get('Email_ID')
        Event_name=self.cleaned_data.get('Event_name')
        if(Email_ID==""):
           self.add_error('name','This field is mandatory')
        for item in Participant.objects.all():
          if item.Email_ID==Email_ID and item.Event_name==Event_name:
            raise forms.ValidationError('This Email-ID already exists')
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
    
            
  
