from django.shortcuts import render

from orders.models import Order
from store.models import Product, Category
from products.books.models import Book
from products.phones.models import Phone
from products.clothes.models import Clothes, Color, Size
from products.laptops.models import Laptop
from django.core.paginator import Paginator


# Create your views here.
# Lay ra tat ca san pham:
def getAllProduct(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    product_list = Product.objects.all()
    # paginator = Paginator(product_list, 8)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {'product_lists': product_list, 'cart_item': cartItems}
    return render(request, 'products/product-list.html', context)


# Lay ra tat ca san pham: Book
def getAllBook(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    product_list = Book.objects.all();
    # paginator = Paginator(product_list, 8)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {'product_lists': product_list, 'cart_item': cartItems}
    return render(request, 'products/product-list.html', context)


# Lay ra tat ca san pham: Phone
def getAllPhone(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    product_list = Phone.objects.all();
    # paginator = Paginator(product_list, 8)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {'product_lists': product_list, 'cart_item': cartItems, 'customer': customer}
    return render(request, 'products/product-list.html', context)


# Lay ra tat ca san pham: Laptop
def getAllLaptop(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    product_list = Laptop.objects.all();
    # paginator = Paginator(product_list, 8)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {'product_lists': product_list, 'cart_item': cartItems, 'customer': customer}
    return render(request, 'products/product-list.html', context)


# Lay ra tat ca san pham: Quan Ao
def getAllClothes(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    product_list = Clothes.objects.all();
    # paginator = Paginator(product_list, 8)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {'product_lists': product_list, 'cart_item': cartItems, 'customer': customer}
    return render(request, 'products/product-list.html', context)


# Lay ra mot san pham theo id va category
def getProductDetail(request, product_id, category_name):
    context = {}

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    if category_name == 'Book':
        product = Book.objects.get(id=product_id)
        context = {'product': product, 'cart_item': cartItems}
    elif category_name == 'Laptop':
        product = Laptop.objects.get(id=product_id)
        context = {'product': product, 'cart_item': cartItems}
    elif category_name == 'Clothes':
        product = Clothes.objects.get(id=product_id)
        query1 = 'SELECT clothes_color.id, clothes_color.name ' \
                 'from clothes_clothes_color INNER JOIN clothes_color ' \
                 'ON clothes_clothes_color.color_id = clothes_color.id ' \
                 'AND clothes_clothes_color.clothes_id = %s' % product_id
        clothes_color = Color.objects.raw(query1)

        query2 = 'SELECT clothes_size.id, clothes_size.name ' \
                 'from clothes_clothes_size INNER JOIN clothes_size ' \
                 'ON clothes_clothes_size.size_id = clothes_size.id ' \
                 'AND clothes_clothes_size.clothes_id = %s' % product_id
        clothes_size = Size.objects.raw(query2)

        context = {'product': product,
                   'clothes_color': clothes_color,
                   'clothes_size': clothes_size,
                   'cart_item': cartItems
                   }
    elif category_name == 'Phone':
        product = Phone.objects.get(id=product_id)
        context = {'product': product, 'cart_item': cartItems, 'customer': customer}

    return render(request, 'products/product-details.html', context)


def searchProduct(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderdetail_set.all()
        cartItems = order.get_cart_counts
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    keyword = request.GET['keyword']
    products = Product.objects.filter(product_name__contains=keyword)
    context = {'product_lists': products, 'cart_item': cartItems, 'customer': customer}
    return render(request, 'products/product-list.html', context)
