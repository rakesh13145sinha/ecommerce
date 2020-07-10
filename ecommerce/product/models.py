from django.db import models

# Create your models here.
class Category(models.Model):
    name              =models.CharField(max_length=100)
    image             =models.ImageField(upload_to='category/images/')
    time              =models.DateTimeField(auto_now_add=True,auto_now=False)
    update            =models.DateTimeField(auto_now_add=False, auto_now=True)
    activate          =models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name

class MenuBar(models.Model):
    pass

class Colors(models.Model):
    name              =models.CharField(max_length=100)
    activate          =models.BooleanField(default=True)


    def __str__(self):
        return self.name

class Size(models.Model):
    size              =models.CharField(max_length=50)
    activate          =models.BooleanField(default=True)


    def __str__(self):
        return self.size

class Brand(models.Model):
        name            =models.CharField(max_length=100)
        madeIn          =models.CharField(max_length=100)
        activate        =models.BooleanField(default=True)

        
        def __str__(self):
            return self.name

class Product(models.Model):
    name            =models.CharField(max_length=100)
    brand            =models.ForeignKey(Brand, on_delete=models.CASCADE)
    model           =models.CharField(max_length=50,null=True)
    price           =models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    newprice        =models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    reference       =models.CharField(max_length=100)
    Quantity        =models.IntegerField(default=False)
    slug            =models.SlugField()
    colors          =models.ManyToManyField(Colors)
    size            =models.ManyToManyField(Size)
    activate        =models.BooleanField(default=True)
    trending        =models.BooleanField(default=True)
    season          =models.BooleanField(default=True)
    exclusive       =models.BooleanField(default=True)
    feature         =models.BooleanField(default=True)
    new             =models.BooleanField(default=True)
    discripsion     =models.TextField(max_length=500)



    
    def __str__(self):
        return self.name
        
    def get_price(self):
        return self.price   

class ProductImage(models.Model):
    products         =models.ForeignKey(Product,on_delete=models.CASCADE)
    categories       =models.ForeignKey(Category,on_delete=models.CASCADE,default=True)
    image            =models.ImageField(upload_to='products/images/')
    featured         =models.BooleanField(default=False)
    thumbnail        =models.BooleanField(default=True)
    active           =models.BooleanField(default=True)
    updated          =models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __unicode__(self):
        return self.products.id

