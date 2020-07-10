from django.shortcuts import render,HttpResponseRedirect
from product.models import Product
from django.urls import reverse


# Create your views here.
def trending_product(request):
    trending_item=Product.objects.all()
    return render(request,"templates/home/bags.html",{'trending_item':trending_item})
    #return HttpResponseRedirect(reverse("home page"))