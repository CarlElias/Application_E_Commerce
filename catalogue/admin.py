from django.contrib import admin
from .models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}
    list_display = ['titre', 'prix', 'prix_reduit']

admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)