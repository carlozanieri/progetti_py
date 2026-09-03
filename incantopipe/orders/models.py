# orders/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone
from store.models import Product
import uuid

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'In Attesa'),
        ('processing', 'In Lavorazione'),
        ('paid', 'Pagato'),
        ('shipped', 'Spedito'),
        ('delivered', 'Consegnato'),
        ('cancelled', 'Cancellato'),
        ('refunded', 'Rimborsato'),
    ]
    
    # Identificativo unico pubblico
    order_number = models.CharField(max_length=20, unique=True, blank=True)
    
    # Relazione utente
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    
    # Dati cliente
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Cognome')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Telefono')
    
    # Indirizzo spedizione
    address = models.CharField(max_length=250, verbose_name='Indirizzo')
    postal_code = models.CharField(max_length=20, verbose_name='CAP')
    city = models.CharField(max_length=100, verbose_name='Città')
    province = models.CharField(max_length=2, blank=True, verbose_name='Provincia')
    country = models.CharField(max_length=100, default='Italia', verbose_name='Paese')
    shipping_notes = models.TextField(blank=True, verbose_name='Note di spedizione')
    
    # Informazioni pagamento
    payment_method = models.CharField(max_length=20, default='paypal', verbose_name='Metodo di pagamento')
    paypal_transaction_id = models.CharField(max_length=100, blank=True, verbose_name='ID transazione PayPal')
    payment_status = models.CharField(max_length=20, default='pending', verbose_name='Stato pagamento')
    
    # Informazioni ordine
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Stato')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Totale')
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Costo spedizione')
    
    # Timestamp
    created = models.DateTimeField(auto_now_add=True, verbose_name='Data creazione')
    updated = models.DateTimeField(auto_now=True, verbose_name='Data aggiornamento')
    paid_at = models.DateTimeField(null=True, blank=True, verbose_name='Data pagamento')
    shipped_at = models.DateTimeField(null=True, blank=True, verbose_name='Data spedizione')
    delivered_at = models.DateTimeField(null=True, blank=True, verbose_name='Data consegna')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Ordine'
        verbose_name_plural = 'Ordini'
    
    def __str__(self):
        return f'Ordine #{self.order_number}'
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)
    
    def generate_order_number(self):
        """Genera un numero ordine unico"""
        import random
        import string
        prefix = 'ICP'  # InCantoPipe
        timestamp = timezone.now().strftime('%Y%m%d')
        random_part = ''.join(random.choices(string.digits, k=6))
        return f'{prefix}-{timestamp}-{random_part}'
    
    def get_total_cost(self):
        """Calcola il totale degli articoli"""
        return sum(item.get_cost() for item in self.items.all())
    
    def get_total_with_shipping(self):
        """Totale con spedizione"""
        return self.get_total_cost() + self.shipping_cost
    
    def mark_as_paid(self, transaction_id=''):
        """Segna l'ordine come pagato"""
        self.status = 'paid'
        self.payment_status = 'paid'
        self.paid_at = timezone.now()
        if transaction_id:
            self.paypal_transaction_id = transaction_id
        self.save()
    
    def mark_as_shipped(self):
        """Segna l'ordine come spedito"""
        self.status = 'shipped'
        self.shipped_at = timezone.now()
        self.save()
    
    def mark_as_delivered(self):
        """Segna l'ordine come consegnato"""
        self.status = 'delivered'
        self.delivered_at = timezone.now()
        self.save()
    
    def mark_as_cancelled(self):
        """Segna l'ordine come cancellato"""
        self.status = 'cancelled'
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, blank=True)  # Nome al momento dell'ordine
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    PAYMENT_METHOD_CHOICES = [
    ('paypal', 'PayPal'),
    ('bank_transfer', 'Bonifico bancario'),
    ('cash_on_delivery', 'Contrassegno'),
]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='paypal', verbose_name='Metodo di pagamento')
    class Meta:
        verbose_name = 'Articolo ordine'
        verbose_name_plural = 'Articoli ordine'
    
    def __str__(self):
        return f'{self.quantity} x {self.product_name}'
    
    def save(self, *args, **kwargs):
        if not self.product_name:
            self.product_name = self.product.name
        super().save(*args, **kwargs)
    
    def get_cost(self):
        return self.price * self.quantity

    # orders/models.py - aggiungi questo modello

class PaymentTransaction(models.Model):
    """Registra le transazioni PayPal"""
    STATUS_CHOICES = [
        ('created', 'Creata'),
        ('approved', 'Approvata'),
        ('completed', 'Completata'),
        ('failed', 'Fallita'),
        ('refunded', 'Rimborsata'),
    ]
    
    order = models.ForeignKey(Order, related_name='transactions', on_delete=models.CASCADE)
    paypal_order_id = models.CharField(max_length=100, unique=True, verbose_name='ID ordine PayPal')
    paypal_transaction_id = models.CharField(max_length=100, blank=True, verbose_name='ID transazione PayPal')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created', verbose_name='Stato')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Importo')
    currency = models.CharField(max_length=3, default='EUR', verbose_name='Valuta')
    payer_email = models.EmailField(blank=True, verbose_name='Email pagatore')
    payer_name = models.CharField(max_length=200, blank=True, verbose_name='Nome pagatore')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Transazione PayPal'
        verbose_name_plural = 'Transazioni PayPal'
    
    def __str__(self):
        return f'Transazione {self.paypal_order_id}'