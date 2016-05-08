from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
		model = Contact
		fields = ('name','email','message',)
		widgets = {
			'name': forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Your Name *','data-validation-required-message':'Please enter your name.'}),
			'email': forms.EmailInput(attrs={'type':'text','class':'form-control','placeholder':'Your Email *','data-validation-required-message':'Please enter your email.'}),
			'message': forms.Textarea(attrs={'type':'text','class':'form-control','placeholder':'Your Message *','data-validation-required-message':'Please enter your message.'}),
			}
