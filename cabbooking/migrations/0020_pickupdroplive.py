# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabbooking', '0019_auto_20180624_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickUpDropLive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.CharField(max_length=300, verbose_name='Booking Type')),
                ('airport', models.CharField(max_length=300, verbose_name='Airport')),
                ('pick_up_point', models.CharField(max_length=300, verbose_name='Pick Up Point')),
                ('trip_route', models.CharField(max_length=300, verbose_name='Trip Route')),
                ('num_of_seats', models.CharField(max_length=300, verbose_name='Num of Seats')),
                ('flight_date', models.CharField(max_length=300, verbose_name='Flight Date')),
                ('flight_time', models.CharField(max_length=300, verbose_name='Flight Time')),
                ('cab_date', models.CharField(max_length=300, verbose_name='Cab Date')),
                ('cab_departure_time', models.CharField(max_length=300, verbose_name='Cab Departure Time')),
                ('cab_pickup_time', models.CharField(max_length=300, verbose_name='Cab Pickup Time')),
                ('mobile_num', models.CharField(max_length=300, verbose_name='Mobile Num')),
                ('email_id', models.CharField(max_length=300, verbose_name='Email Id')),
                ('first_name', models.CharField(max_length=300, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=300, verbose_name='Last Name')),
                ('pick_up_address', models.CharField(blank=True, max_length=300, null=True, verbose_name='Pick Up Address')),
                ('drop_address', models.CharField(blank=True, max_length=300, null=True, verbose_name='Drop Address')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Pick Up Drop Live Request',
                'verbose_name_plural': 'Pick Up Drop Live Request',
            },
        ),
    ]