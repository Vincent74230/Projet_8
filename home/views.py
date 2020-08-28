from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . forms import UserQuestion

def index(request):
    template = loader.get_template('home/index.html')
    form = UserQuestion()
    return HttpResponse(template.render({"form":form}, request))

def mentions_legales(request):
    template = loader.get_template('home/mentions_legales.html')
    form = UserQuestion()
    return HttpResponse(template.render({"form":form}, request))
