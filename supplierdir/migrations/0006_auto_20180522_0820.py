# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-22 02:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplierdir', '0005_auto_20180516_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplierdirectory',
            options={'verbose_name': 'Supplier Details', 'verbose_name_plural': 'Supplier Details'},
        ),
    ]