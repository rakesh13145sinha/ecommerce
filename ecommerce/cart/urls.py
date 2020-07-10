from django.urls import path
from cart import views
urlpatterns=[

    
    path('cart_item/',views.cart_item,name='cart page'),
    
]