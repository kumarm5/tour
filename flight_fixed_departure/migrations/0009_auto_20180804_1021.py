# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-04 04:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flight_fixed_departure', '0008_auto_20180731_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquirydetails',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='enquirydetails',
            name='send_email',
            field=models.BooleanField(default=False, verbose_name='Send Email'),
        ),
        migrations.AddField(
            model_name='enquirydetails',
            name='send_sms',
            field=models.BooleanField(default=False, verbose_name='Send SMS'),
        ),
        migrations.AddField(
            model_name='enquirydetails',
            name='sms_or_email_message',
            field=models.TextField(blank=True, null=True, verbose_name='Email or SMS Message'),
        ),
    ]