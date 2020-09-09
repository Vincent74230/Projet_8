from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        user_question = request.POST.get('UserQuestion')
        print (user_question)
    return HttpResponse('search page')
    