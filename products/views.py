from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .forms import CommentModelForm, OrderModelForm, SignUpForm, UpdateProductModelForm, AddProductModelForm
from products.models import Product, Comment, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from typing import Optional
from django.contrib.auth.decorators import login_required


def home(request, category_slug: Optional[str] = None):  # home page it reflects all products in the website
    cart = Cart(request)
    """ 
    it is for showing quantity of product in your cart
    """
    product_quantity = cart.product_quantity()
    categories = Category.objects.all()
    search = request.GET.get('search')
    filter_type = request.GET.get('filter', '')
    if category_slug:
        if filter_type == 'expensive':
            products = Product.objects.filter(category__slug=category_slug).order_by('-price')
        elif filter_type == 'cheap':
            products = Product.objects.filter(category__slug=category_slug).order_by('price')
        elif filter_type == 'rating':
            products = Product.objects.filter(category__slug=category_slug).order_by('-rating')
        else:
            products = Product.objects.filter(category__slug=category_slug).order_by('-created_at')
    else:
        if filter_type == 'expensive':
            products = Product.objects.order_by('-price')
        elif filter_type == 'cheap':
            products = Product.objects.order_by('price')
        elif filter_type == 'rating':
            products = Product.objects.order_by('-rating')
        else:
            products = Product.objects.all().order_by('-created_at')
    if search:
        products = products.filter(name__icontains=search)
    context = {'products': products,
               'categories': categories,
               'product_quantity': product_quantity,
               }
    return render(request, 'products/home.html', context)


def detail(request, product_slug):  # detail page for products
    cart = Cart(request)
    _id = Product.objects.get(slug=product_slug)
    """ 
    it is for showing quantity of product in your cart
    """
    product_quantity = cart.product_quantity()
    product = Product.objects.get(pk=_id.id)
    related_products = Product.objects.filter(category=product.category).exclude(id=_id.id)
    search = request.GET.get('search')
    if search:
        """searching comment by word in comments"""
        comments = Comment.objects.filter(comment__icontains=search, product=_id.id)
    else:
        """ to get only the last 3 comments from the database """
        comments = Comment.objects.filter(product=_id.id).order_by('-created_at')[:3]
    categories = Category.objects.all()
    context = {
        'product_quantity': product_quantity,
        'categories': categories,
        'comments': comments,
        'products': related_products,
        'product': product
    }
    return render(request, 'products/detail.html', context)


@login_required(login_url='register')
def add_order(request, product_slug: Optional[str] = None):  # order a products
    product = get_object_or_404(Product, slug=product_slug)
    # product = get_object_or_404(Product, id=_id.id)
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
                return redirect('detail', product.slug)
            messages.add_message(request, level=messages.ERROR, message='Not enough stock available.')
    else:
        form = OrderModelForm()
    context = {'form': form,
               'product': product}
    return render(request, 'products/detail.html', context)


def add_comment(request, product_slug):  # comments on a product
    product = Product.objects.get(slug=product_slug)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            messages.add_message(request, level=messages.SUCCESS, message='Your comment has been saved.')
            return redirect('detail', product_slug)
        messages.add_message(request, level=messages.ERROR, message='Something went wrong!')
    else:
        form = CommentModelForm()
    context = {
        'form': form,
        'product': product
    }

    return render(request, 'products/detail.html', context)


@login_required(login_url='register')
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
def delete_product(request, product_slug):  # delete a product
    product = get_object_or_404(Product, slug=product_slug)
    if product:
        product.delete()
        messages.add_message(request, level=messages.SUCCESS, message='Your product has been deleted.')
        return redirect('home')
    messages.add_message(request, level=messages.ERROR, message='Something went wrong!')
    return redirect('home')


@login_required
def update_product(request, product_slug):  # update a product
    product = get_object_or_404(Product, slug=product_slug)
    form = UpdateProductModelForm(instance=product)
    if request.method == 'POST':
        form = UpdateProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, level=messages.SUCCESS, message='Your product has been updated.')
            return redirect('detail', product_slug)
        else:
            messages.add_message(request, level=messages.ERROR, message='Something went wrong!')
            return redirect('detail', product_slug)
    context = {
        'form': form,
    }
    return render(request, 'products/edit_product.html', context)


def about(request):  # about page
    return render(request, 'products/about.html')


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
                                 message=f'Account created for {username} '
                                         f'and logged in successfully.')
            return redirect('home')
        else:
            messages.add_message(request, level=messages.ERROR,
                                 message=f'Invalid username or password.')
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
            messages.error(request, 'Invalid username or password,'
                                    ' please try again')
            return redirect('login')
    else:
        return render(request, 'products/login.html')


def logout_user(request):  # logout user
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def shopping_cart(request):
    pass
