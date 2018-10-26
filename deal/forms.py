from django import forms
from django.db import models

from deal.models import Supplier, Client, Deal

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
        supplier_id = models.ForeignKey('Supplier', on_delete=models.CASCADE, )
        fields = '__all__'