from django.test import TestCase
from django.urls import reverse


class TestPages(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse("home:index"))
        self.assertEqual(response.status_code, 200)

    def test_mentions_legales(self):
        response = self.client.get(reverse("home:mentions"))
        self.assertEqual(response.status_code, 200)
