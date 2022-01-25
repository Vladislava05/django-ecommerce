from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'base/store.html', context)

def cart(request):
    orders = Order.objects.all()
    context = {'orders':orders}
    return render(request, 'base/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'base/checkout.html', context)