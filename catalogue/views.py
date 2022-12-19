from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import *

class HomeView(ListView):
    model = Item
    template_name = 'index.html'

class ProduitDetail (DetailView):
    model = Item
    template_name = 'single-product.html'
    
    
def ajout_au_panier(request, slug, categorie):
    item = get_object_or_404(Item, slug=slug, categorie=categorie)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, Ordered=False)
    order_qs = Order.objects.filter(user=request.user, Ordered=False)
    
    if order_qs.exists():
        
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, f"{item.titre} quantité mise à jour.")
            return redirect("produit", slug=slug, categorie=categorie)
            
        else:
            
            order.items.add(order_item)
            order.save()
            messages.success(request, f"{item.titre} ajouté au panier.")
            return redirect("produit", slug=slug, categorie=categorie) 
    else:
        
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, Ordered=False, Ordered_date=ordered_date)
        order.items.add(order_item)
        order.save()
        messages.success(request, f"{item.titre} ajouté au panier.")
        return redirect("produit", slug=slug, categorie=categorie)

def supp_du_panier(request, slug, categorie):
    item = get_object_or_404(Item, slug=slug, categorie=categorie)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, Ordered=False)
    order_qs = Order.objects.filter(user=request.user, Ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order.items.remove(order_item)
            order.save()
            messages.success(request, f"{item.titre} à été supprimé du panier.")
            return redirect("produit", slug=slug, categorie=categorie)
        else:
            messages.info(request, f"{item.titre} n'est pas dans le panier.")
            return redirect("produit", slug=slug, categorie=categorie) 
    else:
        messages.info(request, "Vous n'avez pas de commande en cours!")
        return redirect("produit", slug=slug, categorie=categorie) 
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def panier(request):
    return render(request, 'cart.html')

def error(request):
    return render(request, '404.html')
