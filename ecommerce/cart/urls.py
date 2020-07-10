from django.urls import path
from cart import views
urlpatterns=[

    
    path('cart_item/',views.cart_item,name='cart page'),
    path('update_cart/<int:id>/',views.updata_cart,name="add to cart")
    
]