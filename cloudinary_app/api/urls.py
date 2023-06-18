from django.urls import path, include
from .views.image import ImageView


urlpatterns = [
    path('image', ImageView.as_view() ),
    

]

