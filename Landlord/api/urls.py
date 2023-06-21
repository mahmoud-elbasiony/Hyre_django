from django.urls import path , include
from .views.subscription import SubscriptionView
from .views.change_subscription import ChangeSubscriptionView
from .views.company import company_full_data, company_positions, company_image


urlpatterns = [
    path('subscriptions',SubscriptionView.as_view() ),
    path('change/subscriptions',ChangeSubscriptionView.as_view() ),
    path('company/image/<str:token>', company_image),
    path('company/positions/<str:token>', company_positions),
    path('company', company_full_data)
]