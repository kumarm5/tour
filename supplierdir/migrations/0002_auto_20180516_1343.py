# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplierdir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Sales Person')),
                ('email_id', models.CharField(max_length=300, verbose_name='Email Id')),
                ('contact_number', models.CharField(max_length=30, verbose_name='Contact Number')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SupplierSalesPerson', to='supplierdir.SupplierDirectory')),
            ],
            options={
                'verbose_name': 'Sales Person',
                'verbose_name_plural': 'Sales Persons',
            },
        ),
        migrations.CreateModel(
            name='SupplierImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=450, verbose_name='Title')),
                ('supplier_images', models.FileField(upload_to='documents/', verbose_name='Supplier Image')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='supplierdir.SupplierDirectory', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Supplier Image',
                'verbose_name_plural': 'Supplier Images',
            },
        ),
        migrations.AddField(
            model_name='supplierdirectory',
            name='supplier_images',
            field=models.ManyToManyField(to='supplierdir.SupplierImages', verbose_name='Supplier Images'),
        ),
    ]
