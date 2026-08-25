# payment/views.py
import requests
import json
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order

def get_paypal_access_token():
    if settings.PAYPAL_MODE == 'sandbox':
        url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    else:
        url = "https://api-m.paypal.com/v1/oauth2/token"
    
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en_US",
    }
    
    data = {
        "grant_type": "client_credentials"
    }
    
    try:
        response = requests.post(
            url,
            headers=headers,
            data=data,
            auth=(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_SECRET)
        )
        
        if response.status_code == 200:
            return response.json()['access_token']
    except:
        pass
    
    return None

def payment_process(request):
    order_id = request.session.get('order_id')
    if not order_id:
        return redirect('store:product_list')
    
    order = get_object_or_404(Order, id=order_id)
    
    context = {
        'order': order,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID,
    }
    return render(request, 'payment/process.html', context)

@csrf_exempt
def create_paypal_order(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Metodo non valido'}, status=400)
    
    order_id = request.session.get('order_id')
    if not order_id:
        return JsonResponse({'error': 'Ordine non trovato'}, status=400)
    
    order = get_object_or_404(Order, id=order_id)
    
    access_token = get_paypal_access_token()
    if not access_token:
        return JsonResponse({'error': 'Impossibile ottenere token PayPal'}, status=500)
    
    if settings.PAYPAL_MODE == 'sandbox':
        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
    else:
        url = "https://api-m.paypal.com/v2/checkout/orders"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    
    payload = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "reference_id": str(order.id),
            "amount": {
                "currency_code": "EUR",
                "value": str(order.total),
            },
            "description": f"Ordine #{order.id} - InCantoPipe",
        }],
        "application_context": {
            "brand_name": "InCantoPipe",
            "landing_page": "NO_PREFERENCE",
            "user_action": "PAY_NOW",
            "return_url": f"http://{request.get_host()}/payment/success/",
            "cancel_url": f"http://{request.get_host()}/payment/cancel/",
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 201:
            return JsonResponse(response.json())
        else:
            return JsonResponse({'error': 'Errore nella creazione ordine PayPal'}, status=response.status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def capture_paypal_order(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Metodo non valido'}, status=400)
    
    try:
        data = json.loads(request.body)
        paypal_order_id = data.get('orderID')
        
        order_id_local = request.session.get('order_id')
        if not order_id_local:
            return JsonResponse({'error': 'Ordine non trovato'}, status=400)
        
        order = get_object_or_404(Order, id=order_id_local)
        
        access_token = get_paypal_access_token()
        if not access_token:
            return JsonResponse({'error': 'Impossibile ottenere token PayPal'}, status=500)
        
        if settings.PAYPAL_MODE == 'sandbox':
            url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{paypal_order_id}/capture"
        else:
            url = f"https://api-m.paypal.com/v2/checkout/orders/{paypal_order_id}/capture"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        
        response = requests.post(url, headers=headers)
        
        if response.status_code == 201:
            order.status = 'paid'
            order.paypal_transaction_id = response.json()['id']
            order.save()
            
            if 'order_id' in request.session:
                del request.session['order_id']
            
            return JsonResponse({'success': True, 'redirect_url': f'/orders/{order.id}/'})
        else:
            return JsonResponse({'error': 'Errore nel catturare il pagamento'}, status=response.status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def payment_success(request):
    return render(request, 'payment/success.html')

def payment_cancel(request):
    return render(request, 'payment/cancel.html')