# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
