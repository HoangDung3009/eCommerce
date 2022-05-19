from django.shortcuts import render
from .models import *
from orders.models import Order, OrderDetail
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    featured_products = Product.objects.all().order_by('-id')[:4][::-1]
    categories = Category.objects.all()
    context = {
        'feature_products': featured_products,
        'categories': categories,
        'cart_item': cartItems,
        'customer': customer
    }
    return render(request, 'index.html', context)
