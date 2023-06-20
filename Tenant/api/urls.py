from django.urls import path, include
from Tenant.api.views import InterviewView, InterviewDetailView
from Tenant.api.views.applicant import index, show, store, destroy, generateAplicantFormLink, show_by_position, edit
from Tenant.api.views.candidates import CandidateView
from Tenant.api.views.delete_users import destroy_user
from .views.mail import MailView
from .views.position import PositionView,PositionDetailView
from .views.user import UserView

urlpatterns = [
    path('interviews/', InterviewView.as_view() ),
    path('interviews/<str:pk>/', InterviewDetailView.as_view() ),
    path('applicants/formLink',generateAplicantFormLink),
    path('applicants/create/<str:token>', store),
    path('applicants/', index),
    path('users', UserView.as_view()),
    path ('applicants/<str:pk>/edit' , edit),
    path('applicants/position/<str:position_id>' , show_by_position),
    path('users/<int:pk>/destroy/', destroy_user),
    path('applicants/<str:pk>/destroy/', destroy),
    path('applicants/<str:pk>/', show),
    path('positions', PositionView.as_view()),
    path('positions/<int:id>', PositionDetailView.as_view()),
    path('candidates', CandidateView.as_view()),
    path('candidates/<str:pk>', CandidateView.as_view()),
    path("emails/<str:type>",MailView.as_view()),
]

