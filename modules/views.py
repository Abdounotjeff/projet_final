from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('loginPage')
        else:
            # Debugging: Print form errors to the console
            print(form.errors)
            messages.error(request, 'Form validation failed. Please correct the errors.')
    else:  # For GET requests
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'pages/registerPage.html', context)


def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'pages/loginPage.html', context={})

def products(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products': products})

def detail(request):
    return render(request, 'pages/detail.html')

def cart(request):
    return render(request, 'pages/cart.html')

def logout(request):
    return render(request, 'pages/logout.html')

def search(request):
    return render(request, 'pages/search.html')

