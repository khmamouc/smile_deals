"""SmileApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from deal import views

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    # Supplier paths
    path('admin/', admin.site.urls),
    path('supp', views.supp),
    path('showSupplier', views.showSupplier),
    path('editSupplier/<int:id>', views.editSupplier),
    path('updateSupplier/<int:id>', views.updateSupplier),
    path('deleteSupplier/<int:id>', views.destroySupplier),
    # Client paths
    path('cli', views.cli),
    path('showClient', views.showClient),
    path('editClient/<int:id>', views.editClient),
    path('updateClient/<int:id>', views.updateClient),
    path('deleteClient/<int:id>', views.destroyClient),
    # Client Deals
    path('dea', views.dea),
    path('showDeal', views.showDeal),
    path('editDeal/<int:id>', views.editDeal),
    path('updateDeal/<int:id>', views.updateDeal),
    path('deleteDeal/<int:id>', views.destroyDeal),
    # Sale Order paths
    path('so', views.so),
    path('showSO', views.showSO),
    path('editSO/<int:id>', views.editSO),
    path('updateSO/<int:id>', views.updateSO),
    path('deleteSO/<int:id>', views.destroySO),
    # HOME path
    path('Home', views.Home),
]
