from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('addCart/', views.addCart, name='addCart'),

    path('addQuantity', views.updateQuantity, name='addQuantity'),

    path('processOrder', views.processOrder, name='processOrder'),

    path('complete/', views.completeOder, name='complete')
]
