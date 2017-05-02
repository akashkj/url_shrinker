# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=20)
	email = models.CharField(max_length=25)

	def __str__(self):
		return self.username

	def __repr__(self):
		return self.username


class Url(models.Model):
	url = models.CharField(max_length=150)
	short_code = models.CharField(max_length=15)
	creation_date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	user = models.ForeignKey(User, null=True)

	def __str__(self):
		return self.url

	def __repr__(self):
		return self.url


class Click(models.Model):
	last_click = models.DateTimeField(auto_now=True)
	url = models.ForeignKey(Url)

	def __str__(self):
		return "{} - {}".format(self.url, self.url.short_code)

	def __repr__(self):
		return "{} - {}".format(self.url, self.url.short_code)
