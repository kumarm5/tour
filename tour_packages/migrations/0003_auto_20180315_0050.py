# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-14 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour_packages', '0002_auto_20180315_0040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tours',
            options={'verbose_name': 'Tour', 'verbose_name_plural': 'Tours'},
        ),
    ]
