from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('product.html', views.product, name='product'),
    path('about.html', views.about, name='about'),
    path('cart.html', views.cart, name='cart'),
    path('product1.html', views.product1, name='product1'),
]