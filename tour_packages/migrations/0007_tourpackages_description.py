# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-17 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_packages', '0006_auto_20180317_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourpackages',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]