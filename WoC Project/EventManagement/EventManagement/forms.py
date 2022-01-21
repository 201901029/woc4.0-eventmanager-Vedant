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
  
class ParticipantForm(ModelForm):
    class Meta:
        model=Participant
        fields=("name","Contact_no","Email_ID","Event_name","Registration_Type","No_of_people")
        widgets={
          "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
          "Contact_no": forms.TextInput(attrs={'class':'form-control','placeholder':'Contact_no'}),
          "Email_ID": forms.TextInput(attrs={'class':'form-control','placeholder':'Email_ID'}),
          "Registration_Type": forms.RadioSelect()
        }
  
