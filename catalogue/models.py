from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

CATEGORIE_CHOIX = (
    ('L', 'Legumes'),
    ('F', 'Fruits'),
    ('C', 'Cereales'),
)
LABEL_CHOIX = (
    ('S', 'Secondary'),
    ('P', 'Primary'),
    ('D', 'Danger'),
)


class Item(models.Model): #Item du catalogue
    titre = models.CharField(max_length=100)
    prix = models.FloatField()
    prix_reduit = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    categorie = models.CharField(choices=CATEGORIE_CHOIX, max_length=1)
    label = models.CharField(choices=LABEL_CHOIX, max_length=1)
    description = models.TextField()
    image = models.ImageField(default='tt.png', upload_to='')
    def __str__(self):
        return self.titre
    
    def get_add_to_cart_url(self):
        return reverse("ajout-au-panier", kwargs={
            'categorie': self.categorie,
            'slug': self.slug
        })
        
    def get_remove_from_cart_url(self):
        return reverse("supp-du-panier", kwargs={
            'categorie': self.categorie,
            'slug': self.slug
        })
           
class Variation(models.Model): #Variation de l'item
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    
    class Meta:
        unique_together = (
            ('item', 'nom'),
        )
    
    def __str__(self):
        return self.nom  
    
class Item_Variation(models.Model): #Variation de l'item
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    valeur = models.CharField(max_length=200)
    attachment = models.ImageField(upload_to='')
    
    class Meta:
        unique_together = (
            ('variation', 'valeur'),
        )
    
    def __str__(self):
        return self.valeur            

class OrderItem(models.Model): #Item de la commande
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} of {self.item.titre}"

class Order(models.Model): #Commande de l'utilisateur
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    Ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    Ordered_date = models.DateTimeField()
    
    def __str__(self):
        return self.user.username