# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20180411_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Address')),
                ('banking', models.TextField(verbose_name='Banking')),
                ('companies', models.TextField(verbose_name='Partner Group of Companies')),
            ],
            options={
                'verbose_name': 'Contact Information',
                'verbose_name_plural': 'Contact Informations',
            },
        ),
    ]
