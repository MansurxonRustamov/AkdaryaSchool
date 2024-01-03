from django import forms
from .models import *


class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields=['ism', 'telefon_raqam','xabar']


