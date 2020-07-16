from django import forms
from django.forms import ModelForm
from checkout.models import Address

class Billing_Address(ModelForm):
    class Meta:
        model=Address
        fields='__all__'