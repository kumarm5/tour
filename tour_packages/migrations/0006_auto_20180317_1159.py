# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-17 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour_packages', '0005_auto_20180317_0923'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Packages',
            new_name='TourPackages',
        ),
    ]