from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from cart.models import Cart,CartItem
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart_item(requst):
    try:
        main_id = requst.session['cart_id']
    except:
        main_id = None
    if main_id:
        cart=Cart.objects.get(id=main_id) 
        context={'cart':cart}
    else:
        msg="your cart is empty keep shoping"
        context={'empty':True,'msg':msg}
    return render(requst,'templates/cart/cart.html',context)


def updata_cart(request,id):
    request.session.set_expiry(12000)
    
    '''quantity'''
    
    try:
        qty= request.POST.get('qty')
        update_qty=True
    except:
        qty = None
        update_qty = False


    '''try to find cart'''
    try:
        main_id=request.session['cart_id']
    except:
        new_cart=Cart()
        new_cart.save()
        request.session['cart_id']=new_cart.id
        main_id=new_cart.id

    cart=Cart.objects.get(id=main_id)
    try:
        product=Product.objects.get(id=id)
    except Product.DoesNotExist:
        pass
    except:
        pass
    '''creating a new cart item'''
    cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)

    '''update cart quantity and save'''

    if  update_qty and qty:

        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity=qty
            cart_item.save()
    else:
        pass


    '''total of cart'''    
    newtotal=0
    for item in cart.cartitem_set.all():
        total=float(item.product.price)*(item.quantity)
        newtotal+=total

    '''product total by it's quantity'''
    for item in cart.cartitem_set.all():
        product_total=float(item.product.price)*(item.quantity)
        cart_item.product_total=product_total
    cart_item.save()

    request.session['item_total']=cart.cartitem_set.count()
    cart.total=newtotal
    cart.save()
    return HttpResponseRedirect(reverse('cart page'))