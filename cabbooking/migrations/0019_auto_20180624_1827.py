# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabbooking', '0018_auto_20180624_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraPickUpDropTerms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('details', models.TextField(verbose_name='Details')),
            ],
            options={
                'verbose_name': 'Extra Pick Up Drop Term',
                'verbose_name_plural': 'Extra Pick Up Drop Terms',
            },
        ),
        migrations.AlterModelOptions(
            name='termsandcondition',
            options={'verbose_name': 'Car Rental Term', 'verbose_name_plural': 'Car Rental Terms'},
        ),
    ]
