# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from cart.views import get_or_create_cart
from store.models import Product
from .models import Order, OrderItem

@login_required
def order_create(request):
    """Crea un nuovo ordine dal carrello"""
    cart = get_or_create_cart(request)
    
    if not cart.items.exists():
        messages.warning(request, 'Il tuo carrello è vuoto.')
        return redirect('store:product_list')
    
    if request.method == 'POST':
        # Validazione base
        required_fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        for field in required_fields:
            if not request.POST.get(field):
                messages.error(request, f'Il campo {field.replace("_", " ")} è obbligatorio.')
                return render(request, 'orders/order_create.html', {'cart': cart})
        
        # Crea l'ordine
        order = Order.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone', ''),
            address=request.POST.get('address'),
            postal_code=request.POST.get('postal_code'),
            city=request.POST.get('city'),
            province=request.POST.get('province', ''),
            country=request.POST.get('country', 'Italia'),
            shipping_notes=request.POST.get('shipping_notes', ''),
            total=cart.total_price,
        )
        
        # Crea gli articoli dell'ordine
        for cart_item in cart.items.select_related('product').all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                product_name=cart_item.product.name,
                price=cart_item.product.price,
                quantity=cart_item.quantity,
            )
            
            # Aggiorna lo stock
            product = cart_item.product
            product.stock -= cart_item.quantity
            if product.stock <= 0:
                product.available = False
            product.save()
        
        # Svuota il carrello
        cart.items.all().delete()
        request.session['cart_items'] = 0
        
        # Salva l'ID dell'ordine nella sessione per il pagamento
        request.session['order_id'] = order.id
        
        # Invia email di conferma
        send_order_confirmation_email(order)
        
        messages.success(request, f'Ordine #{order.order_number} creato con successo!')
        return redirect('payment:payment_process')
    
    context = {
        'cart': cart,
        'cart_items': cart.items.select_related('product').all(),
    }
    return render(request, 'orders/order_create.html', context)

@login_required
def order_history(request):
    """Mostra lo storico degli ordini dell'utente"""
    orders = Order.objects.filter(user=request.user).prefetch_related('items')
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_history.html', context)

@login_required
def order_detail(request, order_id):
    """Mostra i dettagli di un ordine specifico"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {
        'order': order,
        'items': order.items.select_related('product').all(),
    }
    return render(request, 'orders/order_detail.html', context)

@login_required
def order_cancel(request, order_id):
    """Permette di cancellare un ordine non ancora pagato"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if order.status == 'pending':
        order.mark_as_cancelled()
        
        # Ripristina lo stock
        for item in order.items.all():
            product = item.product
            product.stock += item.quantity
            product.available = True
            product.save()
        
        messages.success(request, f'Ordine #{order.order_number} cancellato.')
    else:
        messages.error(request, 'Non puoi cancellare questo ordine.')
    
    return redirect('orders:order_detail', order_id=order.id)

def send_order_confirmation_email(order):
    """Invia email di conferma ordine"""
    subject = f'Conferma Ordine #{order.order_number} - InCantoPipe'
    message = f'''
Gentile {order.first_name} {order.last_name},

Grazie per il tuo ordine su InCantoPipe!

Dettagli dell'ordine:
Numero ordine: {order.order_number}
Data: {order.created.strftime('%d/%m/%Y')}

Articoli ordinati:
'''
    for item in order.items.all():
        message += f'- {item.product_name} x {item.quantity} = € {item.get_cost()}\n'
    
    message += f'''
Totale: € {order.total}

Indirizzo di spedizione:
{order.first_name} {order.last_name}
{order.address}
{order.postal_code} {order.city} ({order.province})
{order.country}

La tua pipe artigianale sarà spedita al più presto.
Riceverai una notifica quando l'ordine verrà spedito.

Cordiali saluti,
InCantoPipe
'''
    
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [order.email],
            fail_silently=True,
        )
    except:
        pass