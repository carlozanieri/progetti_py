# store/models.py
# store/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Descrizione')
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True, null=True, verbose_name='Immagine')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('store:category_products', args=[self.slug])

class Product(models.Model):
    # Scelte per i materiali
    MATERIAL_CHOICES = [
        ('radica', 'Radica'),
        ('morta', 'Radica Morta'),
        ('oliva', 'Oliva'),
        ('ciliegio', 'Ciliegio'),
        ('noce', 'Noce'),
        ('quercia', 'Quercia'),
        ('acero', 'Acero'),
        ('ebano', 'Ebano'),
    ]
    
    # Scelte per le finiture
    FINISH_CHOICES = [
        ('liscia', 'Liscia'),
        ('sabbiata', 'Sabbiata'),
        ('rustica', 'Rustica'),
        ('liscia_sabbiata', 'Liscia/Sabbiata'),
        ('levigata', 'Levigata'),
        ('naturale', 'Naturale'),
    ]
    
    # Scelte per le forme
    SHAPE_CHOICES = [
        ('dritta', 'Dritta'),
        ('curva', 'Curva'),
        ('mezza_curva', 'Mezza Curva'),
        ('churchwarden', 'Churchwarden'),
        ('poker', 'Poker'),
        ('billiard', 'Billiard'),
        ('dublin', 'Dublin'),
        ('bulldog', 'Bulldog'),
        ('prince', 'Prince'),
        ('apple', 'Apple'),
        ('pot', 'Pot'),
        ('canadian', 'Canadian'),
        ('lumberman', 'Lumberman'),
        ('freehand', 'Freehand'),
        ('custom', 'Custom'),
    ]
    
    # Campi base
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Categoria')
    name = models.CharField(max_length=200, verbose_name='Nome')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(verbose_name='Descrizione')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Prezzo')
    available = models.BooleanField(default=True, verbose_name='Disponibile')
    stock = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name='Disponibilità')
    
    # Immagini
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, verbose_name='Immagine principale')
    image_2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, verbose_name='Immagine 2')
    image_3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, verbose_name='Immagine 3')
    image_4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, verbose_name='Immagine 4')
    
    # Caratteristiche specifiche pipe
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='radica', verbose_name='Materiale')
    finish = models.CharField(max_length=20, choices=FINISH_CHOICES, default='liscia', verbose_name='Finitura')
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES, default='dritta', verbose_name='Forma')
    
    # Dimensioni
    length_mm = models.IntegerField(null=True, blank=True, verbose_name='Lunghezza (mm)')
    height_mm = models.IntegerField(null=True, blank=True, verbose_name='Altezza (mm)')
    bowl_diameter_mm = models.IntegerField(null=True, blank=True, verbose_name='Diametro fornello (mm)')
    bowl_depth_mm = models.IntegerField(null=True, blank=True, verbose_name='Profondità fornello (mm)')
    weight_grams = models.IntegerField(null=True, blank=True, verbose_name='Peso (grammi)')
    
    # Altre caratteristiche
    filter = models.BooleanField(default=False, verbose_name='Filtro')
    filter_size = models.CharField(max_length=10, blank=True, verbose_name='Misura filtro (mm)')
    is_unique = models.BooleanField(default=True, verbose_name='Pezzo unico')
    year_made = models.IntegerField(null=True, blank=True, verbose_name='Anno realizzazione')
    serial_number = models.CharField(max_length=50, blank=True, verbose_name='Numero di serie')
    
    # Timestamp
    created = models.DateTimeField(auto_now_add=True, verbose_name='Data creazione')
    updated = models.DateTimeField(auto_now=True, verbose_name='Data aggiornamento')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Pipe'
        verbose_name_plural = 'Pipe'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.is_unique:
            self.stock = 1 if self.available else 0
        super().save(*args, **kwargs)
    
    @property
    def is_in_stock(self):
        return self.stock > 0 and self.available
    
    @property
    def main_image(self):
        if self.image:
            return self.image.url
        return '/static/images/prestige4.jpg'