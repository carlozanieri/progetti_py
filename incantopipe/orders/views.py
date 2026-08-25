from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.views import get_or_create_cart
from .models import Order, OrderItem
from django.core.mail import send_mail
from django.conf import settings


@login_required
def order_create(request):
    # ... codice esistente ...
    
    if request.method == 'POST':
        # ... crea ordine ...
        
        # Invia email di conferma
        subject = f'Conferma Ordine #{order.id} - InCantoPipe'
        message = f'''
        Gentile {order.first_name} {order.last_name},
        
        Grazie per il tuo ordine su InCantoPipe!
        
        Dettagli dell'ordine:
        {order}
        
        La tua pipe artigianale sarà spedita al più presto.
        
        Cordiali saluti,
        InCantoPipe
        '''
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [order.email],
            fail_silently=True,
        )

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    # Nota: il percorso è 'orders/order_history.html'
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    # Nota: il percorso è 'orders/order_detail.html'
    return render(request, 'orders/order_detail.html', {'order': order})