from .views.signin import SigninView
from .views.signup import SignupView
from .views.changepassword import ChangePasswordView

from django.urls import path , include
urlpatterns = [
    path('signup',SignupView.as_view() ),
    path('signin', SigninView.as_view() ),
    path('changepassword', ChangePasswordView.as_view() )
]