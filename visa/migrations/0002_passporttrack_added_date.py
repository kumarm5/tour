# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-12 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passporttrack',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=None, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
