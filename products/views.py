from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentModelForm, OrderModelForm, SignUpForm, UpdateProductModelForm, AddProductModelForm
from products.models import Product, Comment, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from typing import Optional
from django.contrib.auth.decorators import login_required


def home(request, _id: Optional[int] = None):  # home page it reflects all products in the website
    if _id:
        products = Product.objects.filter(category=_id)
    else:
        products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories}
    return render(request, 'products/home.html', context)


def detail(request, _id):  # detail page for products
    product = Product.objects.get(pk=_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=_id)
    comments = Comment.objects.filter(product=_id).order_by('-created_at')[
               :3]  # to get only the last 3 comments from the database
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'comments': comments,
        'products': related_products,
        'product': product
    }
    return render(request, 'products/detail.html', context)


@login_required(login_url='register')
def add_order(request, _id: Optional[int] = None):  # order a products
    product = get_object_or_404(Product, id=_id)
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            if product.quantity >= int(form.cleaned_data['quantity']):
                product.quantity -= int(form.cleaned_data['quantity'])
                product.save()
                order = form.save(commit=False)
                order.product = product
                order.save()
                messages.add_message(request, level=messages.SUCCESS, message='Your order has been submitted!')
                return redirect('detail', _id)
            messages.add_message(request, level=messages.ERROR, message='Not enough stock available.')
    else:
        form = OrderModelForm()
    context = {'form': form,
               'product': product}
    return render(request, 'products/detail.html', context)


@login_required(login_url='register')
def add_comment(request, _id):  # comments on a product
    product = Product.objects.get(pk=_id)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            messages.add_message(request, level=messages.SUCCESS, message='Your comment has been saved.')
            return redirect('detail', _id)
        messages.add_message(request, level=messages.ERROR, message='Something went wrong!')
    else:
        form = CommentModelForm()
    context = {
        'form': form,
        'product': product
    }

    return render(request, 'products/detail.html', context)


def add_product(request):
    if request.method == 'POST':
        form = AddProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, level=messages.SUCCESS, message='Your product has been added.')
            return redirect('home')
        messages.add_message(request, level=messages.ERROR, message='Something went wrong!')
    form = AddProductModelForm()
    context = {'form': form}
    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, _id):  # delete a product
    product = get_object_or_404(Product, id=_id)
    if product:
        product.delete()
        messages.add_message(request, level=messages.SUCCESS, message='Your product has been deleted.')
        return redirect('home')
    messages.add_message(request, level=messages.ERROR, message='Something went wrong!')
    return redirect('home')


@login_required
def update_product(request, _id):  # update a product
    product = get_object_or_404(Product, id=_id)
    form = UpdateProductModelForm(instance=product)
    if request.method == 'POST':
        form = UpdateProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, level=messages.SUCCESS, message='Your product has been updated.')
            return redirect('detail', _id)
        else:
            messages.add_message(request, level=messages.ERROR, message='Something went wrong!')
            return redirect('detail', _id)
    context = {
        'form': form,
    }
    return render(request, 'products/edit_product.html', context)


def about(request):  # about page
    return render(request, 'products/about.html')


def expensive(request):  # filter by expensive
    categories = Category.objects.all()
    products = Product.objects.order_by('-price')
    context = {'categories': categories,
               'products': products}
    return render(request, 'products/home.html', context)


def cheap(request):  # filter by cheap
    categories = Category.objects.all()
    products = Product.objects.order_by('price')
    context = {'categories': categories,
               'products': products}
    return render(request, 'products/home.html', context)


def ratings(request):  # filter by rating
    categories = Category.objects.all()
    products = Product.objects.order_by('-rating')
    context = {'categories': categories,
               'products': products}
    return render(request, 'products/home.html', context)


def register_user(request):  # register user
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(request, level=messages.SUCCESS,
                                 message=f'Account created for {username} and logged in successfully.')
            return redirect('home')
        else:
            messages.add_message(request, level=messages.ERROR, message=f'Invalid username or password.')
            return redirect('register')

    return render(request, 'products/register.html', {'form': form})


def login_user(request):  # login user
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


def logout_user(request):  # logout user
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
