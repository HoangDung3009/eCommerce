from django.db import models
from customer.models import Customer
from store.models import Product
# Create your models here.
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

    @property
    def get_cart_counts(self):
        order_detail = self.orderdetail_set.all()
        total = len(order_detail)
        return total

    @property
    def shipping(self):
        shipping = False
        orderdetails = self.orderdetail_set.all()
        for i in orderdetails:
            if i.product.isActive == False:
                shipping = True
        return shipping

    # Order details


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        orderItems = "Order: {} -- OrderItem: {}"
        return orderItems.format(self.order.id, self.product.product_name)

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
    district = models.CharField(max_length=500, null=True)
    zip_code = models.CharField(max_length=500,null=True)
    addedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
