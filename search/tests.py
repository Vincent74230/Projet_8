from django.test import TestCase
from django.urls import reverse
from . models import Products
from django.contrib.auth.models import User
from django.core.management import call_command
import unittest
from unittest import mock



class ExtractCustomCommandTest(TestCase):
    class MockRequestGet:
        def __init__(self, url, params=None, headers=None):
            self.status_code = 200
        def json(self):
            return {'products':
            [{'id':'5000159407236',
            'image_small_url':'https://static.openfoodfacts.org/images/products/500/015/940/7236/front_fr.19.100.jpg',
            'categories':'Sodas',
            'product_name':'Coca-Cola',
            'nutrition_grades':'e'
            },
            {'id':'5000159407237',
            'image_small_url':'https://static.openfoodfacts.org/images/products/500/015/940/7236/front_fr.19.100.jpg',
            'categories':'Sodas',
            'product_name':'Orangina',
            'nutrition_grades':'e'
            },
            {'id':'5000159407237',
            'image_small_url':'https://static.openfoodfacts.org/images/products/500/015/940/7236/front_fr.19.100.jpg',
            'categories':'Sodas',
            'product_name':'Orangina',
            'nutrition_grades':'e'
            },
            {'id':'5000159407238',
            'image_small_url':'hfeuihziuefh',
            'categories':'Sodas',
            'product_name':'Orangina',
            'nutrition_grades':'e'
            }
            ]
            }

    @mock.patch('search.management.commands.extract.requests.get', MockRequestGet)
    def test_extract(self):
        call_command('extract')
        total = Products.objects.all()
        self.assertEqual(3, len(total)) 
        self.assertEqual('Coca-Cola', total[0].name)
        self.assertEqual(None, total[2].image)

class SearchTestIndexPage(TestCase):
    def test_search_index_view(self):
        response=self.client.get(reverse('search_index'))
        self.assertEqual(response.status_code, 200)

class FavouriteTestPage(TestCase):
    def setUp(self):
        fake_user = User.objects.create_user(
            username='Vincent74230',
            password='Testpassword1',
            first_name='Vincent',
            last_name='VinceNow',
            email='vince@gmail.com'
            )
        fake_user.save()
        self.client.login(username='Vincent74230', password='Testpassword1')

    def test_favourite_page_user_is_connected(self):
        self.client.login(username='Vincent74230', password='Testpassword1')
        response = self.client.get(reverse("search_favourites"))
        self.assertEqual(response.status_code, 200)
