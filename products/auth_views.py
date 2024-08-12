from django.shortcuts import render, redirect
from django.contrib import messages
from products.forms import SignUpForm
from django.contrib.auth import authenticate, login, logout


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.add_message(request, level=messages.SUCCESS,
                                 message=f'Account created '
                                         f'and logged in successfully.')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'auth/register.html', {'form': form})


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
            messages.error(request, 'Invalid username or password,'
                                    ' please try again')
            return redirect('login_page')
    else:
        return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
