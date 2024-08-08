from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from products.models import Product
from django.contrib import messages


def summary_cart(request):
    cart = Cart(request)
    cart_items = cart.get_cart_items()
    product_ids = cart_items.keys()
    products = Product.objects.filter(id__in=product_ids)
    return render(request, 'cart/cummary.html', {'products': products})


def add_cart(request, product_slug):
    if request.method == 'POST':
        _id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=_id)
        cart = Cart(request)
        if cart.checkout(product_slug):
            cart.add(product)
            messages.add_message(request, level=messages.SUCCESS, message='Successfully added to the cart')
            return redirect('detail', product_slug)
        messages.add_message(request, level=messages.ERROR, message='This product already exist in your cart')
        return redirect('detail', product_slug)
    else:
        return messages.add_message(request, level=messages.ERROR, message='Something went wrong, please try again')


def delete_cart(request):
    pass


def update_cart(request):
    pass
