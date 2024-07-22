from django.shortcuts import render, redirect
from product.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from . filters import *
# Create your views here.
def homepage(request):
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        'product':product
    }
    return render(request, 'users/index.html',context)

def productpage(request):
    user = request.user.id
    product = Product.objects.all().order_by('-id')[:4]
    item = Cart.objects.filter(user=user)
    product_filter = ProductFilter(request.GET, queryset=product)
    product_final = product_filter.qs
    context = {
        'product':product_final,
        'product_filter':product_filter,
        'items':item
    }
    return render(request, 'users/products.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product':product
    }
    return render(request, 'users/productdetail.html',context)
def user_register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account Created Successfully!')
            return redirect('/register')
        else:
            messages.add_message(request, messages.ERROR, 'Kindly verify the fields')
            return render(request, 'users/register.html', {'form':form})
    context = {
        'form':UserCreationForm
    }
    return render(request, 'users/register.html',context)
    

def user_login(request):
    if request.method=='POST':
        form = loginform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username = data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('/ecommerceadmin')
                else:
                    return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Kindly provide correct credential!')
            return render(request, 'users/login.html', {'form':forms})
    
    context = {
        'form':loginform
    }
    return render(request, 'users/login.html',context)  
     
def user_logout(request):
    logout(request)
    return redirect('/login')

@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    check_items_present = Cart.objects.filter(user=user, product=product)
    if check_items_present:
        messages.add_message(request, messages.ERROR, 'Product already present in cart')
        return redirect('/productpage')
    else:
        cart = Cart.objects.create(product=product, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Product added successfully in carts')
            return redirect('/cart')
        else:
            messages.add_message(request, messages.ERROR, 'Some error Occurs')
@login_required            
def viewcart(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    context = {
        'items':items
    }
    return render(request, 'users/cart.html', context)

@login_required            
def deletecart(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    messages.add_message(request, messages.ERROR, 'Product removed from cart')
    return redirect('/cart')