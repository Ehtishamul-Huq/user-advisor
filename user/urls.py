from django.conf.urls import url
from user.views import UserRegistrationView, UserLoginView
from django.urls import path

urlpatterns = [
    url(r'^register', UserRegistrationView.as_view()),
    url(r'^login', UserLoginView.as_view()),
]