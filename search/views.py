from django.shortcuts import render, get_object_or_404
from django.http import Http404
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
    
    product = get_object_or_404(Products, barcode=UserChoice)
    try:
        infos = openfoodfacts.products.get_product(UserChoice)
        infos = infos['product']
        context = {'product':product, 'infos':infos}
    except:
        raise Http404("La page demandée n'existe pas")

    return render (request, 'search/detail.html', context)

def register_substitute(request, UserChoice, UserId):
    if request.user.is_authenticated:
        user = User.objects.filter(id=UserId)
        user = user[0]
        favourite_product = Products.objects.filter(barcode=UserChoice)
        favourite_product = favourite_product[0]
        favourite_product.favourites.add(user)
        return render(request, 'search/register_fav_ok.html', {})
    else:
        return render(request, 'search/access_denied.html', {})

def favourites(request, UserId):
    if request.user.is_authenticated:
        fav = Products.objects.filter(favourites=UserId)
        user_favourites=[]
        for element in fav:
            user_favourites.append(element)
        context={'user_favourites':user_favourites}
        return render (request, 'search/my_food.html', context)

    else:
        return render(request, 'search/access_denied.html', {})
