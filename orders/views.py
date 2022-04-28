from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from products.clothes.models import Clothes
from .models import *


# Create your views here.
# Cart page

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)


# Checkout page
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)


# update cart
def addCart(request):
    product_id = request.POST['product_id']
    action = request.POST['action']
    quantity = int(request.POST['quantity'])

    product = Product.objects.get(id=product_id)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderDetail, created = OrderDetail.objects.get_or_create(order=order, product=product)

    orderDetail.quantity += quantity
    orderDetail.save()
    messages.success(request, 'Item was added to cart !!')
    if action == "updateItem":
        return redirect('cart')
    elif action == "quickAdd":
        return redirect('product-list')


def updateQuantity(request):
    product_id = request.POST['product_id']
    action = request.POST['action']
    # quantity = int(request.POST['quantity'])

    product = Product.objects.get(id=product_id)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderDetail, created = OrderDetail.objects.get_or_create(order=order, product=product)

    if action == '+':
        orderDetail.quantity += 1
    elif action == '-':
        orderDetail.quantity -= 1
    if action == 'Remove':
        orderDetail.delete()

    orderDetail.save()

    if action == 'Remove':
        orderDetail.delete()
    if orderDetail.quantity <= 0:
        orderDetail.delete()

    return redirect('cart')
