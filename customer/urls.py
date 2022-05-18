from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('dashboard/', views.account_dashboard, name='profile'),
    path('order/', views.account_order, name='order'),
    path('info/', views.account_detail, name='info'),
    path('logout/', views.logoutUser, name='logout'),
]