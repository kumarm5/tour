# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-20 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0002_auto_20180320_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='title',
            field=models.CharField(max_length=600, verbose_name='Title'),
        ),
    ]
