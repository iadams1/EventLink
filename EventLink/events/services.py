from .models import Event, Attendee
from django.utils import timezone
from datetime import date

def get_upcoming_events():
    return Event.objects.filter(date__gte=date.today()).order_by('date')

def get_past_events():
    return Event.objects.filter(date__lt=date.today()).order_by('-date')

def get_rsvp_count(event):
    return Attendee.objects.filter(event=event).count()
