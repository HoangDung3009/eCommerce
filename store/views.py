from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
    featured_products = Product.objects.all().order_by('-id')[:4][::-1]
    categories = Category.objects.all()
    context = {
        'feature_products': featured_products,
        'categories': categories
    }
    return render(request, 'index.html', context)


# # Cart
# def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderdetail_set.all()
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#
#     context = {'items': items, 'order': order}
#     return render(request, 'cart.html', context)
#
#
# # Checkout
#
# def checkout(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderdetail_set.all()
#     else:
#         # Create empty cart for now for non-logged in user
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#
#     context = {'items': items, 'order': order}
#     return render(request, 'checkout.html', context)
#
#
# def updateCart(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action:', action)
#     print('Product:', productId)
#
#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)
#
#     orderItem, created = OrderDetail.objects.get_or_create(order=order, product=product)
#
#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)
#
#     orderItem.save()
#
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#
#     return JsonResponse('Item was added', safe=False)
