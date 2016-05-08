from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
		model = Contact
		fields = ('name','email','message',)
		widgets = {
			'nama': forms.TextInput(attrs={'id':'icon_prefix','type':'text','class':'validate white-text','placeholder':'Your Name *','data-validation-required-message':'Please enter your name.'}),
			'email': forms.EmailInput(attrs={'id':'icon_email','type':'text','class':'validate white-text','placeholder':'Your Email *','data-validation-required-message':'Please enter your email.'}),
			'pesan': forms.Textarea(attrs={'id':'icon_prefix2','type':'text','class':'materialize-textarea white-text','style':'height: 85px;','placeholder':'Your Message *','data-validation-required-message':'Please enter your message.'}),
			}
