# payment/views.py
import json
import logging
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import Order
from .paypal_service import PayPalService

logger = logging.getLogger(__name__)
paypal_service = PayPalService()

@login_required
def payment_process(request):
    """Mostra la pagina di pagamento"""
    order_id = request.session.get('order_id')
    if not order_id:
        messages.error(request, 'Nessun ordine da pagare.')
        return redirect('store:product_list')
    
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if order.status == 'paid':
        messages.info(request, 'Questo ordine è già stato pagato.')
        return redirect('orders:order_detail', order_id=order.id)
    
    context = {
        'order': order,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID,
    }
    return render(request, 'payment/process.html', context)

@csrf_exempt
@require_http_methods(["POST"])
@login_required
def create_paypal_order(request):
    """Crea un ordine PayPal"""
    try:
        order_id = request.session.get('order_id')
        if not order_id:
            return JsonResponse({'error': 'Ordine non trovato'}, status=400)
        
        order = get_object_or_404(Order, id=order_id, user=request.user)
        
        if order.status == 'paid':
            return JsonResponse({'error': 'Ordine già pagato'}, status=400)
        
        paypal_order, error = paypal_service.create_order(order)
        
        if error:
            return JsonResponse({'error': error}, status=500)
        
        return JsonResponse({'id': paypal_order['id']})
    
    except Exception as e:
        logger.error(f'Errore creazione ordine PayPal: {str(e)}')
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
@login_required
def capture_paypal_order(request):
    """Cattura il pagamento PayPal"""
    try:
        data = json.loads(request.body)
        paypal_order_id = data.get('orderID')
        
        if not paypal_order_id:
            return JsonResponse({'error': 'ID ordine PayPal mancante'}, status=400)
        
        capture_data, error = paypal_service.capture_order(paypal_order_id)
        
        if error:
            return JsonResponse({'error': error}, status=500)
        
        # Trova l'ordine dalla sessione
        order_id = request.session.get('order_id')
        if order_id:
            order = Order.objects.get(id=order_id)
            
            # Rimuovi dalla sessione
            del request.session['order_id']
            
            return JsonResponse({
                'success': True,
                'redirect_url': f'/orders/{order.id}/'
            })
        
        return JsonResponse({'success': True})
    
    except Exception as e:
        logger.error(f'Errore cattura pagamento: {str(e)}')
        return JsonResponse({'error': str(e)}, status=500)

def payment_success(request):
    """Pagina di successo pagamento"""
    return render(request, 'payment/success.html')

def payment_cancel(request):
    """Pagina di annullamento pagamento"""
    return render(request, 'payment/cancel.html')