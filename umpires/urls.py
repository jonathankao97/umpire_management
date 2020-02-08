from django.urls import path

from umpires import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
]