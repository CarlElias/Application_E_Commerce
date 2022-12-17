from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('produit/<categorie>/<slug>', ProduitDetail.as_view(), name='produit')
]