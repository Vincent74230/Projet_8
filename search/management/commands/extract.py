"""
Custom django-admin command, fetches and login datas from OFF server
"""
from django.core.management.base import BaseCommand, CommandError
from search.models import Products
import requests
from requests.exceptions import HTTPError, ConnectionError


CATEGORIES = ['fr:Pâtes à tartiner','Ice creams and sorbets','Sodas','Crisps']
NUTRISCORES = ['a', 'b', 'c', 'd', 'e']


class Command(BaseCommand):#Custom django-admin command, fetches and login datas from OFF server
    help = 'Fetches datas from openfoodfacts database and logs into server database'

    def handle(self, *args, **options):
        CLEAR_PRODUCTS = Products.objects.all()

        CLEAR_PRODUCTS.delete()

        for category in CATEGORIES:
            for nutriscore in NUTRISCORES:
                try:
                    payload = {
                        'action':'process',
                        'json':1,
                        'tagtype_0':'categories',
                        'tag_contains_0':'contains',
                        'tag_0':category,
                        'tagtype_1':'nutrition_grades',
                        'tag_contains_1':'contains',
                        'tag_1':nutriscore,
                        'countries':'France',
                        'page_size':500,
                        'sort_by':'unique_scans_n'
                        }
                    response = requests.get('https://world.openfoodfacts.org/cgi/search.pl',
                        params=payload, headers={'User-Agent':'Apptest - GNU/Linux - Version 0.1'})
                    response = response.json()
                    response = response['products']
                except HTTPError as err:
                    print("Openfoodfacts server might be busy or has crashed, or check your connection : {}\n".format(err))
                
                except ConnectionError as con_err:
                    print ("Openfoodfacts server in not reachable, check your connexion {}".format(con_err))

                for item in response:
                    try:
                        query = Products(barcode=item['id'], category=category, name=item['product_name'], nutriscore=item['nutrition_grades'])
                        query.save()
                    except KeyError:
                        pass
            print ("Extraction of {} category, done.".format(category))
        print("Extraction DONE. Dabatbase up-to-date")
