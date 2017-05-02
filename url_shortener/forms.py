from django import forms
#from django.core.validators import UrlValidator
from django.core.exceptions import ValidationError


class UrlForm(forms.Form):
	url = forms.CharField(label="Url to shorten", max_length=150)

