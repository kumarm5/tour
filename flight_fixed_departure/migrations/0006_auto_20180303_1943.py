# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-03 14:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_fixed_departure', '0005_auto_20180301_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplierdepartureseatinfo',
            options={'verbose_name': 'Round Trip Departure Seat', 'verbose_name_plural': 'Round Trip Departure Seats'},
        ),
        migrations.AlterModelOptions(
            name='supplierreturnseatinfo',
            options={'verbose_name': 'Round Trip Return Seat', 'verbose_name_plural': 'Round Trip Return Seats'},
        ),
    ]