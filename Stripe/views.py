from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import stripe
from Landlord.models import Subscription
from Landlord.models import Tenant

@api_view(['POST'])
def create_checkout_session(request):
    try:
        subscription_data = Subscription.objects.get(name=request.data['name'], type=request.data['type'])
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
            success_url = f'http://localhost:4200/checkout/{request.user.company_id}/{price_id}',
            mode='payment',
            cancel_url='http://localhost:4200/payment/failed',
        )
        return Response({'url': checkout_session.url})  # Include the session ID in the response
    except stripe.error.StripeError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def stripe_checkout_session(request, co_id, pr_id):
    try:

        # Retrieve the subscription using the price ID
        subscription = Subscription.objects.get(pr_id=pr_id)

        # Retrieve the company
        company = Tenant.objects.get(pk=co_id)

        # Update the company's subscription
        company.subscription = subscription
        company.save()
        return Response({
            "success":True,
            "message":"Payment successful",
            "url":"http://localhost:4200/payment/successful"
            },
            status=status.HTTP_201_CREATED)
    except stripe.error.StripeError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    except Subscription.DoesNotExist:
        return Response({
            "success":False,
            "message":"Invalid subscription"}, status=status.HTTP_400_BAD_REQUEST)
    except Tenant.DoesNotExist:
        return Response({
            "success":False,
            "message":"Invalid company"},
            status=status.HTTP_400_BAD_REQUEST)
