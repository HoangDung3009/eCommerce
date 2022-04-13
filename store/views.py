from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    featured_products = Product.objects.all().order_by('-id')[:4][::-1]
    categories = Category.objects.all()
    context = {
        'feature_products': featured_products,
        'categories': categories
    }
    return render(request, 'index.html', context)


# Cart
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
    else:
        items = []

    context = {'items': items}
    return render(request, 'cart.html', context)
