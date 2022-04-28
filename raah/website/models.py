import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# class Category(models.Model):
#     c_id = models.AutoField
#     c_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.c_name
#
# class SubCategory(models.Model):
#     s_id = models.AutoField
#     c_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#     size = models.CharField(max_length=10, default='')
#
#     def __str__(self):
#         return self.size

class Product(models.Model):
    product_id = models.AutoField
    reference_id = models.IntegerField(default=0)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    size = models.CharField(max_length=10, default='')
    color = models.CharField(max_length=10, default='')
    # s_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default='')
    desc = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='static/website/images', blank=True, null=True)

    def __str__(self):
        return self.product_name


# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, default='')
#     email = models.CharField(max_length=200)
#
#     def __str__(self):
#         return str(self.name)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    completed = models.BooleanField(default=False)

    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total

    @property
    def get_itemtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    def __str__(self):
        return str(self.id)


class CartItems(models.Model):
    cartItems_id = models.AutoField
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


    @property
    def get_total(self):
        total = self.quantity * self.product.price
        if total == 0:
            self.delete()
        return total

    def __str__(self):
        return str(self.id) + ', ' + str(self.cart)


class Order(models.Model):
    order_id = models.AutoField
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, default='')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    # quantity = models.IntegerField()
    total = models.IntegerField(default=0)
    order_date = models.DateField(auto_now=True, blank=False)
    address = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default='')

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    contact_id = models.AutoField
    email = models.CharField(max_length=200)
    msg = models.CharField(max_length=500)
    msg_date = models.DateField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.msg_date) + ', ' + str(self.email)


