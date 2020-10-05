from django.test import TestCase
from django.urls import reverse



class IndexPageTest(TestCase):
    def test_index_page_user_not_authenticated(self):
        response=self.client.get(reverse('user_account'))
        self.assertEqual(response.status_code, 302)

class LogoutTest(TestCase):
    def test_user_logout_redirect(self):
        response=self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
'''
    def setUp(self):
        user=
'''
class SignInTest(TestCase):
    def test_sign_in(self):
        response=self.client.get('/user_account/sign_in')
        self.assertEqual(response.status_code, 200)

    def test_sign_in_post(self):
        response= self.client.post('/user_account/sign_in', {
            'username':'Vince74',
            'last_name':'NOWACZYK',
            'first_name':'Vincent',
            'email':'vince@gmail.com',
            'password':'Radeon74'
            })
        self.assertEqual(response.status_code, 200)