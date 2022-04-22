import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Product, Cart, CartItems
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
# def base(request):
#     if request.method == 'POST':
#         # username = request.POST.get('username')
#         username = request.POST['username']
#         email = request.POST['email']
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
#         address = request.POST['address']
#         phno = request.POST['phno']
#
#         myuser = User.objects.create_user(username, email, pass1)
#
#         myuser.save()
#
#         messages.success(request, "Your Account has been succesfully created.")
#
#         return redirect('base')
#
#     return render(request, 'base.html', {})

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        fname = request.POST['fname']
        lname = request.POST['lname']

        # check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Your username must be under 10 characters")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, "username should only contain letters and numbers")
            return redirect('index')

        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('index')

        # create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been succesfully created")
        return redirect('index')
        # or you can also writereturn redirect('/')
    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername,
                            password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Succesfully Logged In")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect('index')

    return HttpResponse('404 - Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('index')


def serchMatch(query, content):
    return True


def search(request):
    query = request.GET.get('search')
    products = Product.objects.all
    content = {'productList': products}
    prod = [content for content in products if searchMatch(query in content.desc)]


def index(request):
    products = Product.objects.all
    content = {'productList': products}
    return render(request, 'index.html', content)


def contact(request):
    return render(request, 'contact.html', {})


# def login(request):
#     return render(request, 'login.html', {})

def product(request):
    # if request.user.is_authenticated:
    #     user_id = request.user
    #     cart, created = Cart.objects.get_or_create(user_id=user_id, completed=False),
    #     cartitems = cart.cartitems_set.all()

    products = Product.objects.all
    content = {'productList': products, 'cart': cart}
    return render(request, 'product.html', content)


def about(request):
    return render(request, 'about.html', {})


def cart(request):
    if request.user.is_authenticated:
        user = request.user;
        cart, created = Cart.objects.get_or_create(user=user, completed=False)
        cartitems = cart.cartitems_set.all()

    return render(request, 'cart.html', {'cartitems': cartitems, 'cart': cart})


def product1(request):
    return render(request, 'product1.html', {})


def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    user = request.user
    print(f"User: {user}")
    cart, created = Cart.objects.get_or_create(user=user, completed=False)
    cartitem, created = CartItems.objects.get_or_create(cart=cart, product=product)

    if action == "add":
        cartitem.quantity += 1
        cartitem.save()

    return JsonResponse("Cart Updated", safe=False)


def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = CartItems.objects.filter(product__name=quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Qunatity updated", safe=False)
