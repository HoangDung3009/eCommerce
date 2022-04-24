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




