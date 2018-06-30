# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabbooking', '0021_pickupdropliveterms'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.IntegerField(verbose_name='Hour')),
                ('minute', models.IntegerField(verbose_name='Minute')),
            ],
            options={
                'verbose_name': 'Time Change',
                'verbose_name_plural': 'Time Changes',
            },
        ),
    ]