
from django.urls import path , include
from .views.subscription import SubscriptionView
from .views.change_subscription import ChangeSubscriptionView


urlpatterns = [
    path('subscriptions',SubscriptionView.as_view() ),
    path('change/subscriptions',ChangeSubscriptionView.as_view() ),

]