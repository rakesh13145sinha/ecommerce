from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password']