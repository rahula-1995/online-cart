from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.index, name="home"),
    path('home/', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('account/', views.account, name="account"),
    path('shop/', views.shop, name="shop"),
    path('detailed/', views.detailed, name="detailed"),
    path('wishlist/', views.wishlist, name="wishlist"),
]