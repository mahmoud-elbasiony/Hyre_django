from django.urls import path, include
from Tenant.api.views import InterviewView, InterviewDetailView
from Tenant.api.views.applicant import index, show, store, edit, destroy
from Tenant.api.views.candidates import CandidateView
from .views.mail import MailView
from .views.position import PositionView,PositionDetailView


urlpatterns = [
    path('interviews/', InterviewView.as_view() ),
    path('interviews/<str:pk>/', InterviewDetailView.as_view() ),
    path('applicants/create/', store),
    path('applicants/', index),
    path('applicants/<str:pk>/edit/', edit),
    path('applicants/<str:pk>/destroy/', destroy),
    path('applicants/<str:pk>/', show),
    path('positions', PositionView.as_view()),
    path('positions/<int:id>', PositionDetailView.as_view()),
    path('candidates', CandidateView.as_view()),
    path('candidates/<str:pk>', CandidateView.as_view()),
    path("emails/<str:type>",MailView.as_view()),

]

