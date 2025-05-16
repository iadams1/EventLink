from django.urls import path
from . import views

urlpatterns = [
	path('', views.event_list, name='event_list'),
	path('events/<int:event_id>/', views.event_detail, name='event_detail'),
	path('rsvp/<int:event_id>/', views.rsvp, name='rsvp'),
	path('rsvp-success/', views.rsvp_success, name='rsvp_success'),
]