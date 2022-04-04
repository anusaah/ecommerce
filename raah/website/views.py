from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all
    content = {'productList': products}
    return render(request, 'index.html', content)

def contact(request):
    return render(request, 'contact.html', {})

def product(request):
    products = Product.objects.all
    content = {'productList':products}
    return render(request, 'product.html', content)

def about(request):
    return render(request, 'about.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def product1(request):
    return render(request, 'product1.html', {})