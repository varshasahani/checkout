from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Cart
import json
from .models import product_discounts,products
# Create your views here.

def products_view(request):
    mapped_products = products
    if(request.user.is_authenticated):
        user = User.objects.get(id=request.user.id)
        cart = Cart.objects.get_or_create(user=user)[0]
        cart_products = cart.products
        mapped_products = map_products_quantity(cart_products,products)

    return render(request, 'products.html',{'products':mapped_products})

@csrf_exempt
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = str(data.get('product_id'))
    quantity = int(data.get('quantity', 1))
    cart_items = request.session.get('cart', {})
    cart_items[product_id] = quantity
    request.session['cart'] = cart_items
    if(request.method == 'POST'):
        if(request.user.is_authenticated):
            user = User.objects.get(id=request.user.id)
            cart = Cart.objects.get_or_create(user=user)[0]
            cart.products[product_id] = quantity
            cart.total_price = calculate_total_price(cart.products)
            cart.save()
    return JsonResponse({'success': True, 'cart': cart_items})

def cart_details(request):
    if(request.user.is_authenticated):
        user = User.objects.get(id=request.user.id)
        cart = Cart.objects.get_or_create(user=user)[0]
        cart_products = cart.products
        total_price = cart.total_price
    else:
        cart_products = request.session.get('cart', {})
        total_price = calculate_total_price(cart_products)
    mapped_products = map_products_quantity(cart_products,products)
    print('products',mapped_products)
    return render(request, 'cart_detail.html', {'products': mapped_products, 'total_price': total_price})

def get_price(product_id, quantity):
    rules = product_discounts.get(product_id, [])
    total_price = 0
    remaining_quantity = quantity
    for rule in sorted(rules, key=lambda x: -x['quantity']):
        count = remaining_quantity // rule['quantity']
        total_price += count * rule['price']
        remaining_quantity %= rule['quantity']
    return total_price

def calculate_total_price(products):
        total_price = 0.00
        hash_map = {}
        for product, quantity in products.items():
            total_price += get_price(product, quantity)
        return total_price

def map_products_quantity(cart_products,products):
    mapped_products = []
    for product_id,quantity in cart_products.items():
        for product in products:
            if product['id'] == product_id:
                product['quantity'] = quantity
                mapped_products.append(product)
    return mapped_products