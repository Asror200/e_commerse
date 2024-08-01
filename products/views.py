from django.shortcuts import render, redirect
from .forms import CommentModelForm, OrderModelForm, SignUpForm
from products.models import Product, Comment, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from typing import Optional


# home page it reflects all products in the website
def home(request, _id: Optional[int] = None):
    if _id:
        products = Product.objects.filter(category=_id)
    else:
        products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories}
    return render(request, 'products/home.html', context)


# detail page for products
def detail(request, _id):
    product = Product.objects.get(pk=_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=_id)
    comments = Comment.objects.filter(product=_id).order_by('-created_at')[:3]  #to get only the last 3 comments from the database
    categories = Category.objects.all()
    new_comment = None
    new_order = None
    if request.method == 'POST':
        comment_form = CommentModelForm(request.POST)
        order_form = OrderModelForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
            messages.success(request, 'Your comment has been saved.')
            return redirect('detail', product.id)
        if order_form.is_valid():
            quantity = order_form.cleaned_data['quantity']
            if product.quantity >= int(quantity):
                product.quantity -= int(quantity)
                product.save()

                new_order = order_form.save(commit=False)
                new_order.product = product
                new_order.save()
                messages.success(request, 'Your order has been submitted!')
                return redirect('detail', _id=_id)
            else:
                messages.error(request, 'Not enough stock available.')
    context = {
        'new_comment': new_comment,
        'new_order': new_order,
        'categories': categories,
        'comments': comments,
        'products': related_products,
        'product': product
    }
    return render(request, 'products/detail.html', context)


# comment for products
# def add_order(request, _id: Optional[int] = None):
#     product = Product.objects.get(id=_id)
#
#     if request.method == 'POST':
#         form = OrderModelForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.product = product
#             order.save()
#             return redirect('home')
#     else:
#         form = OrderModelForm()
#     context = {'form': form,
#                'product': product}
#     return render(request, 'products/detail.html', context)
#
#
# def add_comment(request, _id):
#     product = Product.objects.get(pk=_id)
#     if request.method == 'POST':
#         form = CommentModelForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.product = product
#             comment.save()
#             return redirect('detail', _id)
#     else:
#         form = CommentModelForm()
#     context = {
#             'form': form,
#             'product': product
#         }
#
#     return render(request, 'products/detail.html', context)
#

def about(request):
    return render(request, 'products/about.html')


def expensive(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-price')
    context = {'categories': categories,
               'products': products}
    return render(request, 'products/home.html', context)


def cheap(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('price')
    context = {'categories': categories,
               'products': products}
    return render(request, 'products/home.html', context)


def ratings(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-rating')
    context = {'categories': categories,
               'products': products}
    return render(request, 'products/home.html', context)


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username} and logged in successfully.')
            return redirect('home')
        else:
            messages.success(request, f'Invalid username or password.')
            return redirect('register')
    else:
        return render(request, 'products/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password, please try again')
            return redirect('login')
    else:
        return render(request, 'products/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
