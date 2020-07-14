from django.db import models

# Create your models here.
from product.models import Product

# Create your models here.
class Cart(models.Model):
    
    #product=models.ManyToManyField(Product,null=True,blank=True)
    total=models.DecimalField(max_digits=100,decimal_places=2,default=00.00)
    timestamp=models.DateTimeField(auto_now=False ,auto_now_add=True)
    update=models.DateTimeField(auto_now=True,auto_now_add=False)
    active=models.BooleanField(default=True)

    def __unicode__(self):
        return "cart id: %s",(self.id)

class CartItem(models.Model):
    cart=models.ForeignKey('Cart',null=True ,blank=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    product_total=models.IntegerField(default=1.00)
    upadate=models.DateTimeField(auto_now_add=False,auto_now=True)
    def __unicode__(self):
        try:

            return self.str(cart.id)
        except:
            return self(product.name)