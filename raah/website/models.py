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

class Customer(models.Model):
    customer_id = models.AutoField
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phno = models.IntegerField()

    def __str__(self):
        return self.username

class Order(models.Model):
    order_id = models.AutoField
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField(default=0)
    order_date = models.DateField(auto_now=True, blank=False)