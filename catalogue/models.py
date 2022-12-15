from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model): #Item du catalogue
    titre = models.CharField(max_length=100)
    prix = models.FloatField()
    prix_reduit = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    def __str__(self):
        return self.titre

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