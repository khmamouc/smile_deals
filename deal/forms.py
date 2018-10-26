from django import forms
from django.db import models

from deal.models import Supplier, Client, Deal, SaleOrder

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'


class SaleOrderForm(forms.ModelForm):
    total_paid = forms.FloatField(required=False)
    class Meta:
        model = SaleOrder
        fields = '__all__'