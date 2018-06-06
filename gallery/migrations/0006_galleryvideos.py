# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-05 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20180321_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('video_url', models.CharField(max_length=900, verbose_name='Video Url')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.GallerySubCat', verbose_name='Sub Category')),
            ],
            options={
                'verbose_name': 'Gallery Video',
                'verbose_name_plural': 'Gallery Videos',
            },
        ),
    ]