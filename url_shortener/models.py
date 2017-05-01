# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=20)
	email = models.CharField(max_length=25)


class Url(models.Model):
	url = models.CharField(max_length=150)
	short_code = models.CharField(max_length=15)
	creation_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, null=True)


class Click(models.Model):
	url = models.ForeignKey(Url)
