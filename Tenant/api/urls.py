
from django.urls import path, include
from Tenant.api.views import InterviewView, InterviewDetailView
from Tenant.api.views.candidates import CandidateView
from .views.mail import MailView
from .views.position import PositionView,PositionDetailView


urlpatterns = [
    path('interviews', InterviewView.as_view()),
    path('interviews/<str:pk>', InterviewDetailView.as_view()),
    path('candidates', CandidateView.as_view()),
    path('candidates/<str:pk>', CandidateView.as_view())
    path("emails/<str:type>",MailView.as_view()),
    path('positions/', PositionView.as_view()),
    path('positions/<int:id>/', PositionDetailView.as_view()),

]

