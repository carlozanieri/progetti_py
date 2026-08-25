from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .models import Cart, CartItem

def get_or_create_cart(request):
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
    # Nota: il percorso è 'cart/cart_detail.html'
    return render(request, 'cart/cart_detail.html', {'cart': cart})