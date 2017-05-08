from django import forms
#from django.core.validators import UrlValidator
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
	username = forms.CharField(label="Username", max_length=15)
	password = forms.CharField(label="Password", max_length=20)


class RegistrationForm(forms.Form):
	username = forms.CharField(label="Username", max_length=15)
	password = forms.CharField(label="Password", max_length=20)
	email = forms.CharField(label="Email Address", max_length=25)