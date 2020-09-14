from django.shortcuts import render
from django.http import HttpResponse
from . models import Products


def index(request):
    context={}
    if request.method == 'POST':
        user_question = request.POST.get('UserQuestion')

        context = {'UserQuestion':user_question}



    return render(request, 'search/index.html', context)
