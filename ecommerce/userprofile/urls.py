from django.urls import path
from userprofile import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import login,logout



urlpatterns = [
    path('register/',views.registration,name='register'),
    
     
]