from django.contrib import admin

# Register your models here.
from .models import Product, Customer, Order
# from .models import Category, SubCategory

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
# admin.site.register(Category)
# admin.site.register(SubCategory)