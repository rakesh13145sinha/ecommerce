from django.urls import path
from product import views
urlpatterns=[

    
    path('list/',views.trending_product,name='trending item'),
    
]