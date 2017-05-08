# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UrlForm
from .models import Url
from .utils import get_usable_shortcode, get_url_for_shortcode


def index(request):
	if request.method == 'POST':
		form = UrlForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			short_code = get_usable_shortcode()
			Url(url=data['url'], short_code=short_code).save()
			return HttpResponse("<a href='http://127.0.0.1:8000/{}'>http://127.0.0.1:8000/{}</a>".format(short_code, short_code))
		return HttpResponse("not valid")
	form = UrlForm()
	return render(request, 'url_shortener/index.html', {"form": form})


def redirect(request, short_code):
	url_redirect = get_url_for_shortcode(short_code)
	if not url_redirect:
		return HttpResponse("Not valid url")
	return HttpResponseRedirect(url_redirect)