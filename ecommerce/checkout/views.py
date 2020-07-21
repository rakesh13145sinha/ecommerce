from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from checkout.forms import Billing_Address
from cart.models import Cart,CartItem
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required


# Create your views here.

# def mailing(request):
    
#     form=Billing_Address()
#     if request.method=='POST':
#         form=Billing_Address(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form=Billing_Address()
#     return render(request,'templates/checkout/checkout.html',{'form':form})

'''checkout function'''
@login_required
def mailing(request):
    ''' try  feching cart session '''
    try:
        main_id = request.session.get('cart_id') 
    except:
        main_id = None

    '''creating checkout form submit'''
    if main_id:
        cart=Cart.objects.get(id=main_id)
        cart_item=CartItem.objects.get(id=main_id)
        form=Billing_Address()
        if request.method=='POST':
            form=Billing_Address(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                form=Billing_Address()

        context={'cart':cart,
                'cart_item':cart_item,
                'form':form,
                }
    else:
        msg="your cart is empty keep shoping"
        context={'empty':True,'msg':msg}
    return render(request,'templates/checkout/checkout.html',context)
