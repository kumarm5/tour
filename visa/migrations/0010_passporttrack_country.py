# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-02 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0009_visahistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='passporttrack',
            name='country',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Country'),
        ),
    ]
