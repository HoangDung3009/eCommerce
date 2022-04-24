from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(OrderDetail)
admin.site.register(PaymentMethod)
admin.site.register(Payment)
admin.site.register(ShippingAddress)
admin.site.register(Order)
