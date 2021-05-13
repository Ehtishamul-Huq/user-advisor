from .views import AdvisorView, AdvisorBookingView, AdvisorDetail
from django.urls import path
urlpatterns = [
    path('<str:pk>/advisor', AdvisorView.as_view()),
    path('<str:pk>/advisor/<str:advisor_id>', AdvisorBookingView.as_view()),
    path('<str:pk>/advisor/booking/', AdvisorDetail.as_view()),
]