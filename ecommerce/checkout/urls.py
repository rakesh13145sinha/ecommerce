from django.urls import path
from checkout import views


urlpatterns = [
    path('mail/',views.mailing,name='mailing address')
    
]
