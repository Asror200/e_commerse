from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, OrderForm, SignUpForm
from products.models import Product, ProductComment, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# home page it reflects all products in the website
def home(request):
    products = Product.objects.all()  # order_by('-rating')
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories}
    return render(request, 'products/home.html', context)


def category_list(request, _id):
    category = Category.objects.get(pk=_id)
    categories = Category.objects.all()
    products = category.products.all()
    context = {'categories': categories,
               'products': products}
    return render(request, 'products/home.html', context)


# detail page for products
def detail(request, _id):
    product = Product.objects.get(pk=_id)
    products = Product.objects.filter(category=product.category).exclude(id=_id)
    comments = ProductComment.objects.filter(product=product.id)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'comments': comments,
        'products': products,
        'product': product
    }
    return render(request, 'products/detail.html', context)


# comment for products
def product_comment(request, product_id):
    product = Product.objects.get(pk=product_id)
    comments = ProductComment.objects.filter(product=product)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product.id
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
