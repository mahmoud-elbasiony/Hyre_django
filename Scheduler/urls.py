from django.urls import path, include
from .tasks import check_interview
from django.urls import path


urlpatterns = [
    path('check_interview', check_interview),
    # Other URL patterns...
 
]

