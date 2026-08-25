from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category
from django.contrib import messages


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    # Nota: il percorso è 'store/product_list.html'
    return render(request, 'store/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    if product.is_unique:
        messages.info(request, f'"{product.name}" è un pezzo unico realizzato a mano.')
    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)