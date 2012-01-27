"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from TestTask1.main.models import Request
from django.conf import settings


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
        self.assertContains(response, '<img>')
        self.assertContains(response, 'Login')


class FormTest(TestCase):
    def test_form(self):
        c = Client()
        response = c.get('/login/')
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
