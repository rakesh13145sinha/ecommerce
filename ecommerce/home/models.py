from django.db import models

# Create your models here.
class Slider(models.Model):
    name              =models.CharField(max_length=100)
    image             =models.ImageField(upload_to='slider/image/')
    header_text       =models.CharField(max_length=200,null=True,blank=True)
    text              =models.CharField(max_length=300,null=True,blank=True)
    slug              =models.SlugField()
    active            =models.BooleanField(default=True)
    updated           =models.DateTimeField(auto_now=True, auto_now_add=False)
    time              =models.DateTimeField(auto_now_add=True,auto_now=False)
    featured          =models.BooleanField(default=False)
    

    def __str__(self):
        return self.name

class Parallex(models.Model):
    tittle            =models.CharField(max_length=100)
    image             =models.ImageField(upload_to='parallex/image/')
    header_text       =models.CharField(max_length=200,null=True,blank=True)
    text              =models.CharField(max_length=300,null=True,blank=True)
    active            =models.BooleanField(default=True)
    slug              =models.SlugField()
    featured          =models.BooleanField(default=False)


def __str__(self):
    return self.tittle

