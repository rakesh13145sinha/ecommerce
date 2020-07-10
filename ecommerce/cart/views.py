from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from cart.models import Cart
from product.models import Product

# Create your views here.
def cart_item(requst):
    cart=Cart.objects.all()[0]
    for t in cart.product.all():
        p=t.Quantity*t.price
        
    return render(requst,'templates/cart/cart.html',{'cart':cart,'p':p})
def updata_cart(request,id):
    cart=Cart.objects.all()[0]
    try:
        product=Product.objects.get(id=id)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in cart.product.all():
        cart.product.add()
    else:
        cart.product.remove(product)
    cart.save()
    return HttpResponseRedirect(reverse('cart page'))