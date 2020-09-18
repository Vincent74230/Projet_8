from django.shortcuts import render
from django.http import HttpResponse
from . models import Products



def index(request):
    context={}
    if request.method == 'POST':
        user_question = request.POST.get('UserQuestion')
        try:
            result = Products.objects.filter(name__iexact=user_question)
            result = result[0]
            categories = result.category
            cat = categories.split(',')
            cat = cat[0]
            substitutes = Products.objects.filter(category__icontains=cat)
            substitutes = substitutes.filter(nutriscore='c')
            substitutes_list = []
            for element in substitutes:
                element = element.image
                substitutes_list.append(element)

            print(substitutes_list)

            context = {'UserQuestion':result.name, 'Image':result.image, 'substitutes':substitutes_list}
        except IndexError:
            context={'UserQuestion':'Pas de résultats... Tapez une autre demande'}




    return render(request, 'search/index.html', context)
