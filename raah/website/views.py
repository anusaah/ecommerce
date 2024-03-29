import json
import uuid
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Product, Cart, CartItems, Order, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import date, datetime


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
            messages.warning(request, "Your username must be under 10 characters")
            return redirect('index')

        if not username.isalnum():
            messages.warning(request, "username should only contain letters and numbers")
            return redirect('index')

        if pass1 != pass2:
            messages.warning(request, "Password do not match")
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
    q = request.GET['q']

    products = Product.objects.all
    content = {'productList': products}
    prod = [content for content in products if searchMatch(query in content.desc)]


def base():
    if request.user.is_authenticated:
        user = request.user;
        cart, created = Cart.objects.get_or_create(user=user, completed=False)
        cartitems = cart.cartitems_set.all()
    return render(request, 'base.html', {'cart': cart, 'cartitems': cartitems})


def index(request):
    products = Product.objects.all
    cart = []
    cartitems = []
    if request.user.is_authenticated:
        user = request.user;
        cart, created = Cart.objects.get_or_create(user=user, completed=False)
        cartitems = cart.cartitems_set.all()
    content = {'productList': products, 'cart': cart, 'cartitems': cartitems}
    return render(request, 'index.html', content)


def contact(request):
    cart = []
    cartitems = []
    if request.user.is_authenticated:
        user = request.user;
        cart, created = Cart.objects.get_or_create(user=user, completed=False)
        cartitems = cart.cartitems_set.all()
    content = {'cart': cart, 'cartitems': cartitems}

    if request.method == 'POST':
        # now = datetime.now()
        email = request.POST['email']
        msg = request.POST['msg']
        msg_date = datetime.today().strftime('%Y-%m-%d')
        contact, created = Contact.objects.get_or_create(email=email, msg=msg, msg_date=msg_date)
        contact.save()
    return render(request, 'contact.html', content)


# def login(request):
#     return render(request, 'login.html', {})

def product(request):
    cart = []
    cartitems = []
    if request.user.is_authenticated:
        user = request.user;
        cart, created = Cart.objects.get_or_create(user=user, completed=False)
        cartitems = cart.cartitems_set.all()
    products = Product.objects.all
    content = {'productList': products, 'cart': cart, 'cartitems': cartitems}
    return render(request, 'product.html', content)


def about(request):
    cart = []
    cartitems = []
    if request.user.is_authenticated:
        user = request.user;
        cart, created = Cart.objects.get_or_create(user=user, completed=False)
        cartitems = cart.cartitems_set.all()
    content = {'cart': cart, 'cartitems': cartitems}
    return render(request, 'about.html', content)


def cart(request):
    cart = []
    cartitems = []
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
    quantity = data["quantity"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, completed=False)
    cartitem, created = CartItems.objects.get_or_create(cart=cart, product=product)

    if action == "add":
        cartitem.quantity = quantity
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


def checkout(request):
    today = date.today()
    if request.method == "POST":
        cart_id = request.POST.get('cartId', '')
        cart = Cart.objects.get(id=cart_id)
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        cartItems = CartItems.objects.filter(cart_id=cart_id)
        total = 0;
        for ci in cartItems.iterator():
            computedTotal = ci.product.price * ci.quantity;
            total += computedTotal
        order_date = today.strftime("%b-%d-%Y")
        user_id = request.user
        order = Order(cart_id=cart, user_id=user_id, total=total, address=address, phone=phone,
                      order_date=order_date)
        order.save()
        cart.completed = True
        cart.save()
        thank = True
        return render(request, 'cart.html', {'thank': thank, 'id': order.id})
    return render(request, 'cart.html')


def deletecartitem(request, cartItems_id):
    if request.method == "POST":
        cartitem = CartItems.objects.get(id=cartItems_id)
        cartitem.delete()
    return redirect('index')
