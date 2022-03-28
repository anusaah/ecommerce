from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
        return render(request, 'contact.html', {})

def product(request):
    return render(request, 'product.html', {})

def about(request):
    return render(request, 'about.html', {})

def cart(request):
    return render(request, 'cart.html', {})