# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-31 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=500, verbose_name='Currency Name')),
                ('buy', models.CharField(max_length=300, verbose_name='Buy')),
                ('sale', models.CharField(max_length=300, verbose_name='Sale')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
        ),
    ]
