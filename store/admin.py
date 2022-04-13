from django.contrib import admin

# Register your models here.
from store.models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OrderDetail)
admin.site.register(PaymentMethod)
admin.site.register(Payment)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(Customer)

