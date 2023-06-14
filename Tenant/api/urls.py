
from django.urls import path, include
from Tenant.api.views import InterviewView, InterviewDetailView

urlpatterns = [
    path('interviews', InterviewView.as_view()),
    path('interviews/<str:pk>', InterviewDetailView.as_view())

]
