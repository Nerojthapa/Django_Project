from typing import Any
from django import forms
from product.models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method', 'contact_no', 'address','quantity']  

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

def _init_(self, *args, **kwargs):
    super(ProfileUpdateForm, self)._init_(*args,**kwargs)