# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_deals', '0004_enquirydetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteldetails',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='Remark'),
        ),
    ]