from django.urls import path , include
from .views.subscription import SubscriptionView
from .views.company import company_full_data, company_positions

urlpatterns = [
    path('subscriptions',SubscriptionView.as_view() ),
    path('company', company_full_data),
    path('company/positions/<str:token>' , company_positions)
]