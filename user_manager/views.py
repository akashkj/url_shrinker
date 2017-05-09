# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .forms import LoginForm, RegistrationForm
from .models import User


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			User(username=data['username'], password=data['password'], email=data['email']).save()
			return HttpResponse("registered successfully")
		return HttpResponse("Error in registration")
	else:
		form = RegistrationForm()
		return render(request, 'user_manager/register.html', {'form': form})


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = User.objects.filter(username=data['username'], password=data['password'])
			if user:
				return HttpResponse("Login successful")
			else:
				return HttpResponse("Invalid login")
		return HttpResponse("Invalid input")
	else:
		form = LoginForm()
		return render(request, 'user_manager/login.html', {'form': form})
