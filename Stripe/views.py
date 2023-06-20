from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import stripe
from Landlord.models import Subscription # gives me Import "Landlord.models" could not be resolved

@api_view(['POST'])
def create_checkout_session(request):

    try:
        subscription_data = Subscription.objects.get(name=request.data['name'],type=request.data['type'])
        price_id = subscription_data.pr_id
        stripe.api_key = settings.SECRET_STRIPE_KEY
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:4200/payment/successful',
            cancel_url='http://localhost:4200/dashboard/subscriptions',
        )
    except stripe.error.StripeError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    return Response({'url': checkout_session.url})