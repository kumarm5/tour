# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-23 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabbooking', '0014_auto_20180623_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extrapickupdrop',
            name='pickupdate',
        ),
        migrations.RemoveField(
            model_name='extrapickupdrop',
            name='pickuptime',
        ),
    ]
