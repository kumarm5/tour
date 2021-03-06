# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-20 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0003_auto_20180320_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='title',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='address',
            field=models.CharField(default=None, max_length=800, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='first_name',
            field=models.CharField(default=None, max_length=60, verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='last_name',
            field=models.CharField(default=None, max_length=60, verbose_name='Last Name'),
            preserve_default=False,
        ),
    ]
