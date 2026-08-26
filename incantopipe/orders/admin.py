# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'product_name', 'price', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'first_name', 'last_name', 'total', 'status', 'created']
    list_filter = ['status', 'payment_status', 'created']
    search_fields = ['order_number', 'first_name', 'last_name', 'email']
    readonly_fields = ['order_number', 'created', 'updated', 'paid_at', 'shipped_at', 'delivered_at']
    inlines = [OrderItemInline]
    fieldsets = (
        ('Informazioni Ordine', {
            'fields': ('order_number', 'user', 'status', 'total', 'shipping_cost')
        }),
        ('Dati Cliente', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Indirizzo Spedizione', {
            'fields': ('address', 'postal_code', 'city', 'province', 'country', 'shipping_notes')
        }),
        ('Informazioni Pagamento', {
            'fields': ('payment_method', 'paypal_transaction_id', 'payment_status')
        }),
        ('Date', {
            'fields': ('created', 'updated', 'paid_at', 'shipped_at', 'delivered_at')
        }),
    )
    
    actions = ['mark_as_paid', 'mark_as_shipped', 'mark_as_delivered', 'mark_as_cancelled']
    
    def mark_as_paid(self, request, queryset):
        for order in queryset:
            order.mark_as_paid()
        self.message_user(request, f'{queryset.count()} ordini segnati come pagati.')
    mark_as_paid.short_description = 'Segna come pagati'
    
    def mark_as_shipped(self, request, queryset):
        for order in queryset:
            order.mark_as_shipped()
        self.message_user(request, f'{queryset.count()} ordini segnati come spediti.')
    mark_as_shipped.short_description = 'Segna come spediti'
    
    def mark_as_delivered(self, request, queryset):
        for order in queryset:
            order.mark_as_delivered()
        self.message_user(request, f'{queryset.count()} ordini segnati come consegnati.')
    mark_as_delivered.short_description = 'Segna come consegnati'
    
    def mark_as_cancelled(self, request, queryset):
        for order in queryset:
            order.mark_as_cancelled()
        self.message_user(request, f'{queryset.count()} ordini cancellati.')
    mark_as_cancelled.short_description = 'Cancella ordini'