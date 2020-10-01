from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from . models import Products
from django.contrib.auth.models import User
import openfoodfacts


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
                substitutes_list.append(element)

            context = {'UserQuestion':result.name, 'Image':result.image, 'substitutes':substitutes_list}
        except IndexError:
            context={'UserQuestion':'Pas de résultats... Tapez une autre demande'}

    return render(request, 'search/index.html', context)

def detail(request, UserChoice):
    product = Products.objects.filter(barcode=UserChoice)
    product=product[0]
    infos = openfoodfacts.products.get_product(UserChoice)
    infos = infos['product']

    context = {'product':product, 'infos':infos}

    return render (request, 'search/detail.html', context)

def register_substitute(request, UserChoice, UserId):
    user = User.objects.filter(id=UserId)
    user = user[0]
    favourite_product = Products.objects.filter(barcode=UserChoice)
    favourite_product = favourite_product[0]
    favourite_product.favourites.add(user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def favourites(request, UserId):
    fav = Products.objects.filter(favourites=UserId)
    user_favourites=[]
    for element in fav:
        user_favourites.append(element)
    context={'user_favourites':user_favourites}

    return render (request, 'search/my_food.html', context)
