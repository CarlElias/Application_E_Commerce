from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class HomeView(ListView):
    model = Item
    template_name = 'index.html'

class ProduitDetail (DetailView):
    model = Item
    template_name = 'single-product.html'
    