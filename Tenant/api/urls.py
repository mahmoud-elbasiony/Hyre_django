
from django.urls import path, include
from Tenant.api.views import InterviewView, InterviewDetailView
from Tenant.api.views.candidates import CandidateView

urlpatterns = [
    path('interviews', InterviewView.as_view()),
    path('interviews/<str:pk>', InterviewDetailView.as_view()),
    path('candidates', CandidateView.as_view()),
    path('candidates/<str:pk>', CandidateView.as_view())

]
