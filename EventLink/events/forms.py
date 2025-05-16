from django import forms
from .models import Attendee

class RSVPForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email']