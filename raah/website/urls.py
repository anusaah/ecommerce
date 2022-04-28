from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('product.html', views.product, name='product'),
    path('about.html', views.about, name='about'),
    path('cart.html', views.cart, name='cart'),
    path('updatecart', views.updateCart, name='updatecart'),
    path('updatequantity', views.updateQuantity, name='updatequantity'),
    path('product1.html', views.product1, name='product1'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('checkout', views.checkout, name='checkout'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('deletecartitem/<int:cartItems_id>', views.deletecartitem, name="deletecartitem")
]