from django.db import models
from django.conf import settings
from store.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'In Attesa'),
        ('paid', 'Pagato'),
        ('shipped', 'Spedito'),
        ('delivered', 'Consegnato'),
        ('cancelled', 'Cancellato'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    paypal_transaction_id = models.CharField(max_length=100, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f"Order {self.id}"
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity