# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def register_user(request):
	if request.method == 'POST':
		pass
	return render(request, 'user_manager/register.html')


def login_user(request):
	if request.method == 'POST':
		pass
	return render(request, 'user_manager/login.html')
