# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import Cart, CartItem

def get_or_create_cart(request):
    """Ottiene o crea il carrello per l'utente corrente"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def cart_detail(request):
    cart = get_or_create_cart(request)
    context = {
        'cart': cart,
        'cart_items': cart.items.select_related('product').all(),
    }
    return render(request, 'cart/cart_detail.html', context)

@require_POST
def cart_add(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id, available=True)
    
    # Verifica disponibilità
    if product.stock <= 0:
        messages.error(request, f'"{product.name}" non è più disponibile.')
        return redirect('store:product_list')
    
    # Verifica se il prodotto è già nel carrello
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        # Il prodotto è già nel carrello
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'Quantità di "{product.name}" aggiornata.')
        else:
            messages.warning(request, f'Non puoi aggiungere più di {product.stock} unità di "{product.name}".')
    else:
        messages.success(request, f'"{product.name}" aggiunto al carrello.')
    
    # Aggiorna il contatore nella sessione
    request.session['cart_items'] = cart.total_items
    
    # Se c'è un next nella richiesta, redirect lì, altrimenti al carrello
    next_url = request.POST.get('next', request.GET.get('next'))
    if next_url:
        return redirect(next_url)
    return redirect('cart:cart_detail')

@require_POST
def cart_update(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        if quantity <= cart_item.product.stock:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f'Quantità aggiornata per "{cart_item.product.name}".')
        else:
            messages.warning(request, f'Quantità massima disponibile: {cart_item.product.stock}.')
    else:
        cart_item.delete()
        messages.success(request, f'"{cart_item.product.name}" rimosso dal carrello.')
    
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'"{product_name}" rimosso dal carrello.')
    
    # Aggiorna il contatore nella sessione
    cart = get_or_create_cart(request)
    request.session['cart_items'] = cart.total_items
    
    return redirect('cart:cart_detail')

@require_POST
def cart_clear(request):
    cart = get_or_create_cart(request)
    cart.items.all().delete()
    messages.success(request, 'Carrello svuotato.')
    request.session['cart_items'] = 0
    return redirect('cart:cart_detail')