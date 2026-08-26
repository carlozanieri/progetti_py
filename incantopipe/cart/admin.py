# cart/admin.py
from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'added_at']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at', 'total_items', 'total_price']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'session_key']
    inlines = [CartItemInline]
    
    def total_items(self, obj):
        return obj.total_items
    total_items.short_description = 'Articoli'
    
    def total_price(self, obj):
        return f'€ {obj.total_price}'
    total_price.short_description = 'Totale'