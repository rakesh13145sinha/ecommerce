from django.shortcuts import render,HttpResponseRedirect
from home.models import Parallex,Slider,Instagram
from django.urls import reverse
from product.models import Product,Product_Type
from cart.models import Cart

# Create your views here.

def home(request):
    slide=Slider.objects.all()
    para=Parallex.objects.all()
    trending_item=Product.objects.all()
    instagram=Instagram.objects.all()
    pro_type=Product_Type.objects.all()
    cart=Cart.objects.all()[0]
    for t in cart.product.all():
        print(t.Quantity)
        print(t.price)
        p=t.Quantity*t.price
        print(p)
    context={
        'slide':slide,
        'para':para,
        'trending_item':trending_item,
        'instagram':instagram,
        'pro_type':pro_type,
        'cart':cart
                    }
    return render(request,'templates/home/bags.html',context)
    