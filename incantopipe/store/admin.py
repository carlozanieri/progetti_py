# store/admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'material', 'finish', 'shape', 'available', 'created']
    list_filter = ['available', 'category', 'material', 'finish', 'shape', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description', 'serial_number']
    readonly_fields = ['created', 'updated']
    fieldsets = (
        ('Informazioni Base', {
            'fields': ('category', 'name', 'slug', 'description', 'price', 'available')
        }),
        ('Immagini', {
            'fields': ('image', 'image_2', 'image_3', 'image_4')
        }),
        ('Caratteristiche Pipe', {
            'fields': ('material', 'finish', 'shape', 'filter', 'filter_size')
        }),
        ('Dimensioni', {
            'fields': ('length_mm', 'height_mm', 'bowl_diameter_mm', 'bowl_depth_mm', 'weight_grams')
        }),
        ('Informazioni Aggiuntive', {
            'fields': ('is_unique', 'year_made', 'serial_number', 'created', 'updated')
        }),
    )