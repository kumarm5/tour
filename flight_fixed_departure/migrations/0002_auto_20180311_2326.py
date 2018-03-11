# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-11 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_fixed_departure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onewayseat',
            options={'verbose_name': '   One Way Seat', 'verbose_name_plural': '   One Way Seats'},
        ),
        migrations.AlterModelOptions(
            name='sector',
            options={'verbose_name': '     Sector', 'verbose_name_plural': '     Sectors'},
        ),
        migrations.AlterModelOptions(
            name='supplierdepartureseatinfo',
            options={'verbose_name': '   Round Trip Departure Seat', 'verbose_name_plural': '   Round Trip Departure Seats'},
        ),
        migrations.AlterModelOptions(
            name='supplierdetails',
            options={'verbose_name': '    Supplier Detail', 'verbose_name_plural': '    Supplier Details'},
        ),
        migrations.AlterModelOptions(
            name='supplierreturnseatinfo',
            options={'verbose_name': '  Round Trip Return Seat', 'verbose_name_plural': '  Round Trip Return Seats'},
        ),
    ]
