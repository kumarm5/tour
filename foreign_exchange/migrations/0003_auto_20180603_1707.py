# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreign_exchange', '0002_foreignexchange_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_num', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mobile Number')),
                ('email_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email Id')),
                ('username', models.CharField(max_length=200, verbose_name='Username')),
                ('currency', models.CharField(blank=True, max_length=200, null=True, verbose_name='currency')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Enquiry Detail',
                'verbose_name_plural': 'Enquiry Details',
            },
        ),
        migrations.AlterModelOptions(
            name='foreignexchange',
            options={'verbose_name': 'Foreign Exchange', 'verbose_name_plural': 'Foreign Exchanges'},
        ),
    ]
