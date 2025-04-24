
from django.urls import path
from . import views

urlpatterns = [
    path('',views.products, name='products'),
    path('cart_details/',views.cart_details, name='cart_details'),
    path('cart/add/',views.add_to_cart, name='add_to_cart'),
    # path('cart/remove/',views.remove_from_cart, name='remove_from_cart'),
]