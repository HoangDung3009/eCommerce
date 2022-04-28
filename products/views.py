from django.shortcuts import render
from store.models import Product, Category
from products.books.models import Book
from products.phones.models import Phone
from products.clothes.models import Clothes, Color, Size
from products.laptops.models import Laptop


# Create your views here.
# Lay ra tat ca san pham:
def getAllProduct(request):
    product_list = Product.objects.all()
    context = {'product_lists': product_list}
    return render(request, 'products/product-list.html', context)


# Lay ra mot san pham theo id va category
def getProductDetail(request, product_id, category_name):
    context = {}
    if category_name == 'Book':
        product = Book.objects.get(id=product_id)
        context = {'product': product}
    elif category_name == 'Laptop':
        product = Laptop.objects.get(id=product_id)
        context = {'product': product}
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
                   'clothes_size': clothes_size
                   }
    elif category_name == 'Phone':
        product = Phone.objects.get(id=product_id)
        context = {'product': product}

    return render(request, 'products/product-details.html', context)

# def searchProduct(request, keyword):
