
from django.urls import path
from . import views

urlpatterns = [
    path('',views.products_view, name='products_view'),
    path('cart_details/',views.cart_details, name='cart_details'),
    path('cart/add/',views.add_to_cart, name='add_to_cart'),
]