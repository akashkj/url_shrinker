# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=20)
	email = models.CharField(max_length=25)
	activated = models.BooleanField(default=True)

	def __str__(self):
		return self.username

	def __repr__(self):
		return self.username
