from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order

def payment_process(request):
    order_id = request.session.get('order_id')
    if not order_id:
        return redirect('store:product_list')
    
    order = get_object_or_404(Order, id=order_id)
    
    context = {
        'order': order,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID,
    }
    # Nota: il percorso è 'payment/process.html'
    return render(request, 'payment/process.html', context)

def payment_success(request):
    # Nota: il percorso è 'payment/success.html'
    return render(request, 'payment/success.html')

def payment_cancel(request):
    # Nota: il percorso è 'payment/cancel.html'
    return render(request, 'payment/cancel.html')