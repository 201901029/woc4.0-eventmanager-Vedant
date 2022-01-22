from xmlrpc.client import DateTime
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import EventForm
from .models import Event
from .forms import ParticipantForm
import datetime
def index(request):
    context = {'name':'Vedant'}
    return render(request,'index.html',context)

def event_registration(request):
    if request.method=="POST":
        form=EventForm(request.POST)    
        if form.is_valid():
            form.save()
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
        form=ParticipantForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.success(request,'Your Form Has been Submitted')
            return HttpResponseRedirect('/participant_registration')
        else:
            messages.error(request,'Please fill the form correctly')
    else:
        form=ParticipantForm
    return render(request,'participant_registration.html',{'list':list,'form':form})



