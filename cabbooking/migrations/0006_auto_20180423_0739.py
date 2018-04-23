# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-23 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabbooking', '0005_tariffdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='TariffEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, verbose_name='Username')),
                ('mobile_num', models.CharField(max_length=15, verbose_name='Mobile Number')),
                ('email_id', models.CharField(max_length=100, verbose_name='Email Address')),
                ('subject', models.CharField(max_length=500, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Tariff Enquiry',
                'verbose_name_plural': 'Tariff Enquiries',
            },
        ),
        migrations.AlterModelOptions(
            name='vehiclemaster',
            options={'verbose_name': ' Vehicle', 'verbose_name_plural': ' Vehicles'},
        ),
    ]
