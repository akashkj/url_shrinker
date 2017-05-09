# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Url, Click

admin.site.register(Url)
admin.site.register(Click)
