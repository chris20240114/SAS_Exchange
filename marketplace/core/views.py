from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth.decorators import login_required
from .models import Seller
from .forms import SignupForm, SellerForm
from django import *

def index(request):
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
        
    return render(request, 'core/signup.html', {
        'form':form
    })
    
def get_username(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

@login_required
def registerSeller(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            Seller = form.save(commit=False)
            Seller.created_by = request.user
            Seller.save()

            return redirect('/')
    else:
        form = SellerForm()
        
    return render(request, 'core/seller.html', {
        'form':form
    })
