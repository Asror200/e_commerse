from django.shortcuts import render, redirect, get_object_or_404
from .form import CommentForm, OrderForm
from products.models import Product, ProductComment, Order


# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/home.html', context)


def detail(request, _id):
    product = Product.objects.get(pk=_id)
    context = {'product': product}
    return render(request, 'products/detail.html', context)


def product_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = ProductComment.objects.filter(product=product)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = CommentForm()

    return render(request, 'products/detail.html', {
        'product': product,
        'comments': comments,
        'form': form,
    })


def product_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'products/detail.html', {
        'product': product,
        'form': form,
    })


def order_success(request):
    return render(request, 'products/order_success.html')