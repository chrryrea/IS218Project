from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .cart import Cart
from .forms import CartAddProductForm

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        messages.success(request, f'{product.name} added to your cart')
    return redirect('products:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'{product.name} removed from your cart')
    return redirect('products:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    # Use the app-specific template path to avoid ambiguity
    return render(request, 'cart/detail.html', {'cart': cart})
