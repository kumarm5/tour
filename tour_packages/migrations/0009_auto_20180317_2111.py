# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-17 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_packages', '0008_packageimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packageimages',
            options={'verbose_name': 'Package Image', 'verbose_name_plural': 'Package Images'},
        ),
        migrations.AddField(
            model_name='packageimages',
            name='title',
            field=models.CharField(default=None, max_length=450, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
