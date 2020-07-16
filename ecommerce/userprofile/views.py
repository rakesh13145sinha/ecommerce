from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from userprofile.forms import UserRegistration 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

'''registration'''
def registration(request): 
    form=UserRegistration()
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/')
        else:
            form=UserRegistration()
    return render(request,'registration/register.html',{'form':form})



