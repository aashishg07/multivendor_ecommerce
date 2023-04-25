from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username
    

class ProductCategory(models.Model):
    title = models.CharField(max_length=255, null=True)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title
    

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True)
    detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.order_time)

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product.title

