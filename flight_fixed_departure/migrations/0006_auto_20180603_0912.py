# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 03:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_fixed_departure', '0005_auto_20180603_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onewayseat',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='supplierdepartureseatinfo',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='supplierreturnseatinfo',
            name='sector',
        ),
    ]
