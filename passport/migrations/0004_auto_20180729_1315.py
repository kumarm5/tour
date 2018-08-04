# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('passport', '0003_auto_20180522_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='passportinfo',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='passportinfo',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At'),
        ),
        migrations.AddField(
            model_name='passportinfo',
            name='status',
            field=models.CharField(choices=[('GENERATED', 'GENERATED'), ('IN-PROCESS', 'IN-PROCESS'), ('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED')], default='GENERATED', max_length=100),
        ),
    ]