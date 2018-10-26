# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from deal.models import Supplier, Client, Deal, SaleOrder
from deal.forms import SupplierForm, ClientForm, DealForm, SaleOrderForm

"""
    SUPPLIER VIEWS
"""

def supp(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showSupplier')
            except:
                pass
    else:
        form = SupplierForm()

    return render(request, 'index_supplier.html', {'form': form})

def showSupplier(request):
    suppliers = Supplier.objects.all()
    return render(request,"show_supplier.html",{'suppliers':suppliers})

def editSupplier(request, id):
    supplier = Supplier.objects.get(id=id)
    return render(request,'edit_supplier.html', {'supplier':supplier})

def updateSupplier(request, id):
    supplier = Supplier.objects.get(id=id)
    form = SupplierForm(request.POST, instance = supplier)
    if form.is_valid():
        form.save()
        return redirect("/showSupplier")
    return render(request, 'edit_supplier.html', {'supplier': supplier})

def destroySupplier(request, id):
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    return redirect("/showSupplier")

"""
    CLIENT VIEWS
"""

def cli(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showClient')
            except:
                pass
    else:
        form = ClientForm()

    return render(request, 'index_client.html', {'form': form})

def showClient(request):
    clients = Client.objects.all()
    return render(request,"show_client.html",{'clients': clients})

def editClient(request, id):
    client = Client.objects.get(id=id)
    form = ClientForm()
    return render(request,'edit_client.html', {'client': client}, {'form': form})

def updateClient(request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
        form.save()
        return redirect("/showClient")
    return render(request, 'edit_client.html', {'client': client})

def destroyClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect("/showClient")


"""
    DEAL VIEWS
"""

def dea(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        import pdb; pdb.set_trace()
        if form.is_valid():
            try:
                form.save()
                return redirect('/showDeal')
            except:
                pass
    else:
        form = DealForm()

    return render(request, 'index_deal.html', {'form': form})

def showDeal(request):
    deals = Deal.objects.all()
    return render(request,"show_deal.html",{'deals':deals})

def editDeal(request, id):
    deal = Deal.objects.get(id=id)
    return render(request, 'edit_deal.html', {'deal': deal})

def updateDeal(request, id):
    deal = Deal.objects.get(id=id)
    form = DealForm(request.POST, instance=deal)
    try:
        if form.is_valid():
            form.save()
            return redirect("/showDeal")
    except:
        import sys
        sys.__stdout__.write("That doesn't work")
    finally:
        return render(request, 'edit_deal.html', {'deal': deal})

def destroyDeal(request, id):
    deal = Deal.objects.get(id=id)
    deal.delete()
    return redirect("/showDeal")


"""
    SALE ORDER VIEWS
"""

def so(request):
    if request.method == 'POST':
        form = SaleOrderForm(request.POST)
        import pdb; pdb.set_trace()
        if form.is_valid():
            try:
                form.save()
                return redirect('/showSO')
            except:
                pass
    else:
        form = SaleOrderForm()

    return render(request, 'index_so.html', {'form': form})

def showSO(request):
    sos = SaleOrder.objects.all()
    return render(request,"show_so.html",{'sos':sos})

def editSO(request, id):
    so = SaleOrder.objects.get(id=id)
    return render(request, 'edit_so.html', {'so': so})

def updateSO(request, id):
    so = SaleOrder.objects.get(id=id)
    form = SaleOrderForm(request.POST, instance=so)
    try:
        if form.is_valid():
            form.save()
            return redirect("/showSO")
    except:
        pass
    return render(request, 'edit_so.html', {'so': so})

def destroySO(request, id):
    so = Deal.objects.get(id=id)
    so.delete()
    return redirect("/showSO")

"""
    HOME VIEW
"""

def Home(request):
    return render(request, "home.html")