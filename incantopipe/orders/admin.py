from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'price', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 
                   'total', 'status', 'created']
    list_filter = ['status', 'created']
    search_fields = ['first_name', 'last_name', 'email']
    inlines = [OrderItemInline]
    readonly_fields = ['paypal_transaction_id']