from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('produit/<categorie>/<slug>', ProduitDetail.as_view(), name='produit'),
    path('About', about, name='about'),
    path('contact', contact, name='contact'),
    path('panier', panier, name='panier'),
    path('404', error, name='error'), 
    path('ajout-au-panier/<categorie>/<slug>/', ajout_au_panier, name='ajout-au-panier'),
    path('supp-du-panier/<categorie>/<slug>/', supp_du_panier, name='supp-du-panier'),
]
