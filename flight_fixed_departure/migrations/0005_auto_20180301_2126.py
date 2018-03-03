# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-01 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight_fixed_departure', '0004_auto_20180301_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneWaySeatRemarkInline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_remark', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('supplier_seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oneway_seat_detail', to='flight_fixed_departure.OneWaySeat')),
            ],
            options={
                'verbose_name': 'One Way Seat Remark',
                'verbose_name_plural': 'One Way Seat Remarks',
                'db_table': 'oneway_seat_remark',
            },
        ),
        migrations.AlterField(
            model_name='supplierdetails',
            name='oneway_rate_supplier',
            field=models.IntegerField(blank=True, null=True, verbose_name='One Way Rate Supplier'),
        ),
    ]
