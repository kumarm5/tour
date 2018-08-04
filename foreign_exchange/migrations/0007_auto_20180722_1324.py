# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreign_exchange', '0006_auto_20180703_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquirydetails',
            name='send_email',
            field=models.BooleanField(default=False, verbose_name='Send Email'),
        ),
        migrations.AlterField(
            model_name='enquirydetails',
            name='status',
            field=models.CharField(choices=[('GENERATED', 'GENERATED'), ('IN-PROCESS', 'IN-PROCESS'), ('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED')], default='GENERATED', max_length=100),
        ),
    ]