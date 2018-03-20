# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-20 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0004_auto_20180320_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='address',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='last_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Last Name'),
        ),
    ]
