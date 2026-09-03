# payment/paypal_service.py
import requests
import json
from django.conf import settings
from orders.models import Order, PaymentTransaction
import logging

logger = logging.getLogger(__name__)

class PayPalService:
    """Servizio per interagire con PayPal API"""
    
    def __init__(self):
        self.client_id = settings.PAYPAL_CLIENT_ID
        self.secret = settings.PAYPAL_SECRET
        self.api_url = settings.PAYPAL_API_URL
        self.access_token = None
    
    def get_access_token(self):
        """Ottiene il token di accesso PayPal"""
        if self.access_token:
            return self.access_token
        
        url = f'{self.api_url}/v1/oauth2/token'
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en_US',
        }
        data = {
            'grant_type': 'client_credentials'
        }
        
        try:
            response = requests.post(
                url,
                headers=headers,
                data=data,
                auth=(self.client_id, self.secret)
            )
            
            if response.status_code == 200:
                self.access_token = response.json()['access_token']
                return self.access_token
            else:
                logger.error(f'Errore ottenimento token: {response.text}')
                return None
        except Exception as e:
            logger.error(f'Eccezione ottenimento token: {str(e)}')
            return None
    
    def create_order(self, order):
        """Crea un ordine PayPal"""
        access_token = self.get_access_token()
        if not access_token:
            return None, 'Impossibile ottenere token PayPal'
        
        url = f'{self.api_url}/v2/checkout/orders'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}',
        }
        
        # Prepara i dati dell'ordine
        payload = {
            'intent': 'CAPTURE',
            'purchase_units': [{
                'reference_id': str(order.id),
                'description': f'Ordine #{order.order_number} - InCantoPipe',
                'amount': {
                    'currency_code': 'EUR',
                    'value': str(order.total),
                },
            }],
            'application_context': {
                'brand_name': 'InCantoPipe',
                'landing_page': 'NO_PREFERENCE',
                'user_action': 'PAY_NOW',
                'shipping_preference': 'SET_PROVIDED_ADDRESS',
                'return_url': f'https://incantopipe.it/payment/success/',
                'cancel_url': f'https://incantopipe.it/payment/cancel/',
            },
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 201:
                paypal_order = response.json()
                
                # Salva la transazione
                transaction = PaymentTransaction.objects.create(
                    order=order,
                    paypal_order_id=paypal_order['id'],
                    status='created',
                    amount=order.total,
                    currency='EUR',
                )
                
                return paypal_order, None
            else:
                logger.error(f'Errore creazione ordine: {response.text}')
                return None, response.text
        except Exception as e:
            logger.error(f'Eccezione creazione ordine: {str(e)}')
            return None, str(e)
    
    def capture_order(self, paypal_order_id):
        """Cattura il pagamento di un ordine PayPal"""
        access_token = self.get_access_token()
        if not access_token:
            return None, 'Impossibile ottenere token PayPal'
        
        url = f'{self.api_url}/v2/checkout/orders/{paypal_order_id}/capture'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}',
        }
        
        try:
            response = requests.post(url, headers=headers)
            
            if response.status_code == 201:
                capture_data = response.json()
                
                # Trova la transazione
                try:
                    transaction = PaymentTransaction.objects.get(
                        paypal_order_id=paypal_order_id
                    )
                    
                    # Aggiorna la transazione
                    if capture_data.get('purchase_units'):
                        purchase_unit = capture_data['purchase_units'][0]
                        if purchase_unit.get('payments', {}).get('captures'):
                            capture = purchase_unit['payments']['captures'][0]
                            transaction.paypal_transaction_id = capture['id']
                            transaction.status = 'completed'
                            transaction.save()
                            
                            # Aggiorna l'ordine
                            order = transaction.order
                            order.mark_as_paid(capture['id'])
                            
                            # Aggiorna le informazioni del pagatore
                            if capture_data.get('payer'):
                                payer = capture_data['payer']
                                transaction.payer_email = payer.get('email_address', '')
                                payer_name = payer.get('name', {})
                                transaction.payer_name = f"{payer_name.get('given_name', '')} {payer_name.get('surname', '')}"
                                transaction.save()
                    
                    return capture_data, None
                except PaymentTransaction.DoesNotExist:
                    return None, 'Transazione non trovata'
            else:
                logger.error(f'Errore cattura pagamento: {response.text}')
                return None, response.text
        except Exception as e:
            logger.error(f'Eccezione cattura pagamento: {str(e)}')
            return None, str(e)
    
    def verify_webhook(self, headers, body):
        """Verifica la firma del webhook PayPal"""
        access_token = self.get_access_token()
        if not access_token:
            return False
        
        url = f'{self.api_url}/v1/notifications/verify-webhook-signature'
        headers['Authorization'] = f'Bearer {access_token}'
        headers['Content-Type'] = 'application/json'
        
        # Questo è un esempio semplificato - in produzione dovresti verificare la firma
        return True