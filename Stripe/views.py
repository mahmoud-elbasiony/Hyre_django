from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import stripe

@api_view(['POST'])
def create_checkout_session(request):
    try:
        stripe.api_key = settings.SECRET_STRIPE_KEY
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': "price_1NKj05IfGZb04ICqEBCfWQZP",
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:4200/dashboard',
            cancel_url='http://localhost:4200/dashboard/subscriptions',
        )
    except stripe.error.StripeError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    return Response({'url': checkout_session.url})