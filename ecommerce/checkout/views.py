from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from checkout.forms import Billing_Address
from cart.models import Cart,CartItem


# Create your views here.

def mailing(request):
    form=Billing_Address()
    if request.method=='POST':
        form=Billing_Address(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Billing_Address()
    return render(request,'templates/checkout/checkout.html',{'form':form})

def testing(requst):
    try:
        main_id = requst.session.get('cart_id')
        print(main_id)
    except:
        main_id = None
    if main_id:
        cart=Cart.objects.get(id=main_id)
        cart_item=CartItem.objects.get(id=main_id)
        print(cart)
        print('cartitem:=',cart_item.product.name)
        context={'cart':cart,
                'cart_item':cart_item,
                        }
    else:
        msg="your cart is empty keep shoping"
        context={'empty':True,'msg':msg}
    return render(requst,'templates/home/base.html',context)