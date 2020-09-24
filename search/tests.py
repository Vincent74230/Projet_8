from django.test import TestCase
from search.management.commands.extract import Command
from django.core.management.base import BaseCommand, CommandError
from . models import Products
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
            }
            ]
            }

    @mock.patch('search.management.commands.extract.requests.get', MockRequestGet)
    def test_extract(self):
        call_command('extract')
        total = Products.objects.all()
        self.assertEqual(2, len(total)) 
        self.assertEqual('Coca-Cola', total[0].name)
