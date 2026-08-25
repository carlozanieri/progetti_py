# store/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'


class Product(models.Model):
    # Campi esistenti
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(default=1)  # Ogni pipe è unica, stock=1
    
    # Campi specifici per pipe artigianali
    material = models.CharField(max_length=100, default='Radica')  # Materiale principale
    finish = models.CharField(max_length=100, blank=True)  # Finitura (liscia, sabbiata, ecc.)
    length_cm = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    weight_grams = models.IntegerField(null=True, blank=True)
    bowl_diameter_mm = models.IntegerField(null=True, blank=True)
    is_unique = models.BooleanField(default=True)  # Pezzo unico
    year_made = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created']  # Mostra prima le più recenti
        verbose_name = 'Pipe'
        verbose_name_plural = 'Pipe'