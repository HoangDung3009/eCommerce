from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllProduct, name='product-list'),
    path('<str:category_name>-<int:product_id>/', views.getProductDetail, name='product-details'),
    path('search/', views.searchProduct, name='searchProduct')
]