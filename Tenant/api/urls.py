from django.urls import path, include
from Tenant.api.views import InterviewView, InterviewDetailView
from Tenant.api.views.applicant import index, show, store, edit, destroy

urlpatterns = [
    path('interviews/', InterviewView.as_view() ),
    path('interviews/<str:pk>/', InterviewDetailView.as_view() ),
    path('applicants/create/', store),
    path('applicants/', index),
    path('applicants/<str:pk>/edit/', edit),
    path('applicants/<str:pk>/destroy/', destroy),
    path('applicants/<str:pk>/', show)
]

