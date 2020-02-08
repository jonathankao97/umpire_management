from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from umpires import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
]