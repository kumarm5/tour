# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-28 03:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_fixed_departure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onewayseat',
            name='sector',
        ),
    ]