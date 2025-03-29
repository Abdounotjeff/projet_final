from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('detail/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.registerPage, name='registerPage'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
    path('resend/', views.resend_verification, name ='resend_verification'),
    path('verify/', views.activ, name='activ'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
