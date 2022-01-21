from django.contrib import admin 
from EventManagement.models import Event
from EventManagement.models import Participant
admin.site.register(Event)
admin.site.register(Participant)
