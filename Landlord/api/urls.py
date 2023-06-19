
from django.urls import path , include
from .views.subscription import SubscriptionView

urlpatterns = [
    path('subscriptions',SubscriptionView.as_view() ),
    path('changr/subscriptions',SubscriptionView.as_view() ),

    
]