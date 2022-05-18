from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllProduct, name='product-list'),
    path('book/', views.getAllBook, name='product-book'),
    path('clothes/', views.getAllClothes, name='product-clothes'),
    path('phone/', views.getAllPhone, name='product-phone'),
    path('laptop/', views.getAllLaptop, name='product-laptop'),
    path('<str:category_name>-<int:product_id>/', views.getProductDetail, name='product-details'),
    path('search/', views.searchProduct, name='searchProduct')
]