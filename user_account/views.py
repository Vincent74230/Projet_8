from django.shortcuts import render, redirect
from . forms import UserQuestion, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    context = {"form":UserQuestion}
    return render(request, 'user_account/index.html', context)

def register_page(request):
    Registration = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
    context = {'RegisterForm':Registration}
    return render(request, 'user_account/register_page.html', context)

def login_page(request):
    Login = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')

    context = {'LoginForm':Login}
    return render(request, 'user_account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
