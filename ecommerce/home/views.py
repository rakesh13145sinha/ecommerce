from django.shortcuts import render,HttpResponseRedirect
from home.models import Parallex,Slider
from django.urls import reverse

# Create your views here.

def home(request):
    slide=Slider.objects.all()
    para=Parallex.objects.all()
    context={
        'slide':slide,
        'para':para
            }
    return render(request,'templates/home/bags.html',context)
    #return HttpResponseRedirect(reverse('trending item'))