from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.

SHIPING_CHOICES =[
    ("S_A", "SHIPPING_ADDRESS"), 
    ("B_A", "BILLING_ADDRESS"), 

]
COUNTRY_CHOICE=[
    ('IND','INDIA'),
    ('US','UNITED STATE'),
    ('UK','UNITED KIGNDOM')
]
# creating a form  
class Address(models.Model): 
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=1000,choices = SHIPING_CHOICES)
    first_name=models.CharField(max_length=1000)
    last_name=models.CharField(max_length=1000)
    phone_no=models.CharField(max_length=100)
    email=models.EmailField()
    country=models.CharField(max_length=1000,choices=COUNTRY_CHOICE)
    street=models.CharField(max_length=10000)
    town=models.CharField(max_length=1000)
    state=models.CharField(max_length=100)
    postal_code=models.IntegerField()

    def __str__(self):
        return self.user.username




    