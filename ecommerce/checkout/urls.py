from django.urls import path
from checkout import views


urlpatterns = [
    path('test/',views.testing, name='checkout'),
    path('mail/',views.mailing,name='mailing address')
    
]
