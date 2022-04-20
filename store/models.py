from django.db import models
from django.contrib.auth.models import User


# Customer
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=500, null=True, blank=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='static/images/customer')
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname

    @property
    def photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url


# Category
class Category(models.Model):
    cat_name = models.CharField(max_length=500, blank=True, null=True)
    cat_description = models.TextField(max_length=500, blank=True, null=True)
    cat_thumb = models.ImageField(upload_to='static/images/category', null=True, blank=True)

    def __str__(self):
        return self.cat_name

    @property
    def photo_url(self):
        if self.cat_thumb and hasattr(self.cat_thumb, 'url'):
            return self.cat_thumb.url


# Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    product_name = models.CharField(max_length=500, blank=True, null=True)
    price = models.FloatField(default=0.00, null=True)
    product_thumb = models.ImageField(upload_to='static/images/product', null=True, blank=True)
    product_description = models.TextField(blank=True, null=True)
    unit_in_stock = models.IntegerField(null=True)
    isActive = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['product_name']

    def __str__(self):
        return self.product_name

    @property
    def photo_url(self):
        if self.product_thumb and hasattr(self.product_thumb, 'url'):
            return self.product_thumb.url


# Order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(null=True, max_length=300)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_detail = self.orderdetail_set.all()
        total = sum([item.get_total for item in order_detail])
        return total

    @property
    def get_cart_items(self):
        order_detail = self.orderdetail_set.all()
        total = sum([item.quantity for item in order_detail])
        return total

    # Order details


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


# Payment method
class PaymentMethod(models.Model):
    payment_method = models.CharField(null=True, blank=True, max_length=500)


# Payment
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    payment_mtd = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, blank=True, null=True)


# Shipping Address
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField(null=True)
    city = models.CharField(null=True, max_length=500)
    country = models.CharField(max_length=500, null=True)
    zip_code = models.IntegerField(null=True)
    addedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
