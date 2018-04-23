# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-10 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='Remark')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
    ]