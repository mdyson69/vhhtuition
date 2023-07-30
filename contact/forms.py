from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact Form
    """
    class Meta:
        model = Contact
        fields = ('name', 'contact_email', 'contact_phone',
                  'subject', 'message',)
