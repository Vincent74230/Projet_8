from django.shortcuts import render
from . forms import UserQuestion

def index(request):
    form = UserQuestion()
    return render(request, 'home/index.html', {'form':form})

def mentions_legales(request):
    return render(request, 'home/mentions_legales.html', {})
