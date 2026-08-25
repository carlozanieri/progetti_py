# store/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, Category


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True, stock__gt=0)
    
    # Filtro per categoria
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Filtri aggiuntivi
    material = request.GET.get('material')
    finish = request.GET.get('finish')
    shape = request.GET.get('shape')
    search_query = request.GET.get('search')
    
    if material:
        products = products.filter(material=material)
    if finish:
        products = products.filter(finish=finish)
    if shape:
        products = products.filter(shape=shape)
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Ordinamento
    sort = request.GET.get('sort', '-created')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    else:
        products = products.order_by('-created')
    
    # Paginazione
    paginator = Paginator(products, 9)  # 9 pipe per pagina
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'material_choices': Product.MATERIAL_CHOICES,
        'finish_choices': Product.FINISH_CHOICES,
        'shape_choices': Product.SHAPE_CHOICES,
        'current_material': material,
        'current_finish': finish,
        'current_shape': shape,
        'search_query': search_query,
        'sort': sort,
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    
    # Pipe correlate (stessa categoria o stesso materiale)
    related_products = Product.objects.filter(
        Q(category=product.category) | Q(material=product.material)
    ).exclude(id=product.id).filter(available=True, stock__gt=0)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'store/product_detail.html', context)