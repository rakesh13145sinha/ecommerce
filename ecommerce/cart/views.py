from django.shortcuts import render
from cart.models import Cart
from product.models import Product

# Create your views here.
def cart_item(requst):
    cart=Cart.objects.all()[0]
    for t in cart.product.all():
        p=t.Quantity*t.price
        
    return render(requst,'templates/cart/cart.html',{'cart':cart,'p':p})
def updata_cart(request,id):
    pass