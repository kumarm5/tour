# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-22 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabbooking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=300, verbose_name='Vehicle Name')),
                ('category', models.CharField(max_length=300, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
            },
        ),
    ]
