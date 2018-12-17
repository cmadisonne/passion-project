from django import forms
from .models import Events, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': forms.Textarea
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields= '__all__'
        widgets = {
            'description': forms.Textarea
        }
