from django.urls import path, include
from .tasks import check_interview

urlpatterns = [
    path('check_interview', check_interview),
    # Other URL patterns...
]