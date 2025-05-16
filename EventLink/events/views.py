from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event
from .forms import RSVPForm
from .services import get_upcoming_events, get_rsvp_count, get_past_events
from datetime import date
from datetime import datetime

# Create your views here.

# These are just placeholders
def event_list(request):
	upcoming = get_upcoming_events()
	past = get_past_events()


	return render(request, 'event_list.html', {
		'upcoming_events': upcoming,
		'past_events': past
	})

def event_detail(request, event_id):
	event = Event.objects.get(id=event_id)
	rsvp_count = get_rsvp_count(event)

	now = datetime.now()
	event_datetime = datetime.combine(event.date, event.time)

	is_past = event_datetime < now
	return render(request, 'event_detail.html', {
		'event': event, 
		'rsvp_count': rsvp_count,
		'is_past': is_past
	})

def rsvp(request, event_id):
    event = Event.objects.get(id=event_id)

    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event
            attendee.save()
            return redirect('rsvp_success')
    else:
        form = RSVPForm()

    return render(request, 'rsvp.html', {'event': event, 'form':form})

def rsvp_success(request):
	return render(request, 'event_rsvp_success.html')
