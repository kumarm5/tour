# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-31 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreign_exchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignexchange',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
    ]
