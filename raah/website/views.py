from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request,product_id=1):
    products = Product.objects.get(id=product_id)
    context = {'products': products}
    return render(request, 'index.html', context)

def contact(request):
        return render(request, 'contact.html', {})

def product(request,product_id=1):
    products = Product.objects.get(id=product_id)
    context = {'products': products}
    return render(request, 'product.html', context)

def about(request):
    return render(request, 'about.html', {})

def cart(request):
    return render(request, 'cart.html', {})