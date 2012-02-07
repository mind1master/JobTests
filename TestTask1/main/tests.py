"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from TestTask1.main.models import Request
from django.conf import settings
from TestTask1.main.models import Person


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class MainPageTest(TestCase):
    def test_http(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Last name')
        self.assertContains(response, 'Birth date')
        self.assertContains(response, 'Skype')
        self.assertContains(response, 'Phone')
        self.assertContains(response, 'Bio')
        self.assertContains(response, 'e-mail')
        self.assertContains(response, 'requests')
        self.assertContains(response, 'Photo')
        self.assertContains(response, 'Login')


class AuthTest(TestCase):
    def test_auth(self):
        c = Client()
        response = c.get('/login/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/logout/')
        self.assertEqual(response.status_code, 302)
        response = c.get('/edit/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(c.login(username='admin', password='admin'), True)
        response = c.get('/edit/')
        self.assertEqual(response.status_code, 200)


class FormTest(TestCase):
    def test_form(self):
        p = Person.objects.get(pk=1)
        mdata = {'name': 'TestName', 'surname': p.surname, 'birth_date': p.birth_date,
                 'bio': p.bio, 'skype': p.skype, 'email': p.email,
                 'phone': p.phone, 'photo': p.photo}
        c = Client()
        c.login(username='admin', password='admin')
        response = c.post('/edit/', mdata)
        p = Person.objects.get(pk=1)
        self.assertEqual(p.name, 'TestName')
        self.assertEqual(response.status_code, 200)


class RequestsPageTest(TestCase):
    def test_http(self):
        c = Client()
        response = c.get('/requests/')
        self.assertEqual(response.status_code, 200)
        self.equal = self.assertEqual(Request.objects.count() > 0, True)


class ContextTest(TestCase):
    def test_context(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.context['settings'], settings)
