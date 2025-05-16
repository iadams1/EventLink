from django.contrib import admin
from .models import Event, Attendee

# Register your models here.
class EventAdmin (admin.ModelAdmin):
	list_display = ("title","description","date","time","location","category",)

class AttendeeAdmin (admin.ModelAdmin):
	list_display = ("name","email","event",)

admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)