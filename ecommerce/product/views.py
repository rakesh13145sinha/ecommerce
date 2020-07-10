from django.shortcuts import render,HttpResponseRedirect
from product.models import Product
from django.urls import reverse


# Create your views here.
def trending_product(request):
    trending_item=Product.objects.all()
    return render(request,"templates/home/bags.html",{'trending_item':trending_item})
    #return HttpResponseRedirect(reverse("home page"))
def product_detail(request,id):
    product_details=Product.objects.filter(id=id)
    suggest_product=Product.objects.all()
    context={
        'product_details':product_details,
        'suggest_product':suggest_product
    }
    return render(request,'templates/product/product-page(no-sidebar).html',context)