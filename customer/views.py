from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from orders.models import Order
from .models import *


# Create your views here.

# Login page
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        return render(request, 'customers/login.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

        else:
            messages.error(request, ' Wrong username OR password')
            return redirect("login")


# Customer dashboard
@login_required(login_url="login")
def account_dashboard(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cart_item': cartItems, 'customer': customer}
    return render(request, 'customers/account-dashboard.html', context)


# Customer order
@login_required(login_url="login")
def account_order(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cart_item': cartItems, 'customer': customer}
    return render(request, 'customers/account-order.html', context)


# Customer info
@login_required(login_url="login")
def account_detail(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cart_item': cartItems, 'customer': customer}
    return render(request, 'customers/account-info.html', context)

#Register page
def registerPage(request):
    return render(request, 'customers/register.html')


# Dang ky thanh vien
def registerUser(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        fullname = firstname + " " + lastname
        dob = request.POST['dob']
        username = request.POST['username'].lower()
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']

        u = User.objects.filter(username=username)
        if u.exists():
            messages.error(request, "Account existed !!")
            return redirect("register")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            customer = Customer.objects.create(
                user=user,
                fullname=fullname,
                birthday=dob,
                email=email,
                phone=phone
            )
            customer.save()
            login(request, user)
            return redirect("index")


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect("login")