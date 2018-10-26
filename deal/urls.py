from django.contrib import admin
from django.urls import path
from deal import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('supp', views.supp),
    path('showSupplier',views.showSupplier),
    path('editSupplier/<int:id>', views.editSupplier),
    path('updateSupplier/<int:id>', views.updateSupplier),
    path('deleteSupplier/<int:id>', views.destroySupplier),
    path('cli', views.cli),
    path('showClient',views.showClient),
    path('editClient/<int:id>', views.editClient),
    path('updateClient/<int:id>', views.updateClient),
    path('deleteClient/<int:id>', views.destroyClient),
    path('dea', views.dea),
    path('showDeal', views.showDeal),
    path('editDeal/<int:id>', views.editDeal),
    path('updateDeal/<int:id>', views.updateDeal),
    path('deleteDeal/<int:id>', views.destroyDeal),
]