# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
