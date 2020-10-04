from django.test import TestCase
from django.urls import reverse
import unittest
from unittest import mock

class TestIndex(TestCase):
    def test_index_page_user_not_authenticated(self):
        response=self.client.get(reverse('user_account'))
        self.assertEqual(response.status_code, 302)

class TestLogout(TestCase):
    def test_user_logout_redirect(self):
        response=self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)