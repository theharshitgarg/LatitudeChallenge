from django.contrib import admin

# Register your models here.

from .models import Event, EventRegistration, Participant

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(EventRegistration)
