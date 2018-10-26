# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('initial_price', models.FloatField()),
                ('deal_price', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'deal',
            },
        ),
        migrations.CreateModel(
            name='sale_order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('total_paid', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deal.Client')),
            ],
            options={
                'db_table': 'sale_order',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('working_hours', models.CharField(max_length=23)),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.AddField(
            model_name='deal',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deal.Supplier'),
        ),
    ]
