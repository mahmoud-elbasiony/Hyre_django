from django.urls import path
from .views import create_checkout_session,stripe_checkout_session

urlpatterns = [
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('checkout/<int:co_id>/<str:pr_id>', stripe_checkout_session),
]