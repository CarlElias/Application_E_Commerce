from django.contrib import admin
from .models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}
    list_display = ['titre', 'prix', 'prix_reduit']

class ItemVariationAdmin(admin.ModelAdmin):
    list_display = ['variation', 'valeur', 'attachment']
    search_fields = ['valeur']
    list_filter = ['variation', 'variation__item']
    
class ItemVariationInlineAdmin(admin.TabularInline):
    model = Item_Variation
    extra = 1
    
class VariationAdmin(admin.ModelAdmin):
    list_display = ['item', 'nom']
    search_fields = ['item']
    list_filter = ['item']
    inlines = [ItemVariationInlineAdmin]
    
    
admin.site.register(Item_Variation, ItemVariationAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)