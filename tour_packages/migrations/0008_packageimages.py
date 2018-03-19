# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-17 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour_packages', '0007_tourpackages_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_images', models.FileField(upload_to='documents/', verbose_name='Package Image')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_packages.TourPackages', verbose_name='Package')),
            ],
            options={
                'verbose_name': 'Packages',
                'verbose_name_plural': 'Packages',
            },
        ),
    ]
