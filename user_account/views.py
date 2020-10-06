from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'user_account/index.html', context)
    else:
        return redirect('/home')

def register_page(request):
    Registration = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Votre compte a bien été créé" + user)
            return redirect ('login')
        else:

    context = {'RegisterForm':Registration}
    return render(request, 'user_account/register_page.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, "Votre nom d'utilisateur ou mote de passe est incorrect")

    context = {}
    return render(request, 'user_account/login.html', context)


@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')
