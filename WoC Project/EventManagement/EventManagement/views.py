from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import EventForm
from .models import Event
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
    return render(request,'participant_registration.html',{'list':list})



