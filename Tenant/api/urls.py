
from django.urls import path , include
from .views.mail import MailView
urlpatterns = [
    path("emails/<str:type>",MailView.as_view(),name="send-mail")
]