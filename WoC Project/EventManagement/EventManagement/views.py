from imp import reload
from xmlrpc.client import DateTime
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from twilio.rest import Client
from .forms import EventForm
from .models import Event
from .forms import ParticipantForm
from .models import Participant
import datetime
def index(request):
    context = {'name':'Vedant'}
    return render(request,'index.html',context)

def event_registration(request):
    if request.method=="POST":
        form=EventForm(request.POST)    
        if form.is_valid():
            thanks="Thankyou for registering an event"
            name=request.POST['name']
            email=request.POST['email']
            desc=request.POST['desc']
            From=request.POST['To']
            To=request.POST['From']
            Registration_Deadline=request.POST['Registration_Deadline']
            message = "%s\n Name: %s\n Email: %s\n Description: %s\n From: %s\n To: %s\n Registration_Deadline: %s\n" % (
                    thanks,
                    name , 
                    email,
                    desc,
                    From,
                    To,
                    Registration_Deadline)
            form.save()
            send_mail(
                'Test',
                message,
                'vedantparikh421@gmail.com',
                [email]
            )
            return HttpResponseRedirect('/event_registration')
    else:
        form=EventForm
    return render(request,'event_registration.html',{'form':form})

def participant_registration(request):
    list=Event.objects.all()
    for item in list:
        if item.Registration_Deadline.replace(tzinfo=None)<datetime.datetime.now().replace(tzinfo=None):
            item.delete()
    if request.method=="POST":
        flag=0
        form=ParticipantForm(request.POST)  
        name=request.POST['name']
        Contact_no=request.POST['Contact_no']
        Email_ID=request.POST['Email_ID']
        Event_name=request.POST.get('Event_name',False)
        Registration_Type=request.POST['Registration_Type']
        No_of_people=request.POST['No_of_people']
        participant=Participant(name=name,Contact_no=Contact_no,Email_ID=Email_ID,Event_name=Event_name,Registration_Type=Registration_Type,No_of_people=No_of_people)
        if Event_name == False:
            messages.error(request,"Please enter event name")
            return HttpResponseRedirect('/participant_registration')
        if name == "":
            messages.error(request,"Please enter your name")
            return HttpResponseRedirect('/participant_registration')
        if Contact_no == "":
            messages.error(request,"Please enter contact no")
            return HttpResponseRedirect('/participant_registration')
        for item in Participant.objects.all():
          if item.Email_ID==Email_ID:
            if item.Event_name==Event_name:
              flag=1
        if flag==1:
            messages.error(request,"This email ID already exists")
            return HttpResponseRedirect('/participant_registration')

        participant.save()


            #account_sid = 'AC5e7957d055a49d897da005172a5a9b60'
            #auth_token ='bdf62192a911a9c66840e8ff7863d295'
            #client = Client(account_sid, auth_token)
            #name=request.POST['name']
            #Contact_no=str(request.POST['Contact_no'])
            #Email_ID=request.POST['Email_ID']
            #Event_name=request.POST['Event_name']
            #message = "Name: %s\n Contact No: %s\n Email: %s\n Event Name: %s\n " % (
                    #name , 
                    #Contact_no,
                    #Email_ID,
                    #Event_name)
            #message = client.messages.create(
                              #body=message,
                              #from_='+16066033405',
                              #to=Contact_no
                          #)
            #print(message.sid)
        messages.success(request,'Your Form Has been Submitted')
        return HttpResponseRedirect('/participant_registration')
    else:
        form=ParticipantForm
    return render(request,'participant_registration.html',{'list':list,'form':form})



