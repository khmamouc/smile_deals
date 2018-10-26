# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'client'

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    working_hours = models.CharField(max_length=23)

    class Meta:
        db_table = 'supplier'

class Deal(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=40)
    description = models.TextField()
    initial_price = models.FloatField()
    deal_price = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    stock = models.IntegerField(null=True)
    class Meta:
        db_table = 'deal'

class SaleOrder(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    deal = models.ForeignKey('Deal', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_paid = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'sale_order'
