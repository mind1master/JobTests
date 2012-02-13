"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from TestTask1.main.models import Request
from django.conf import settings
from TestTask1.main.forms import PersonForm
from TestTask1.main.models import Person, SignalInfo
import os
import datetime


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
        p = Person.objects.all()[0]
        mdata = {'name': p.name, 'surname': p.surname,
                 'birth_date': p.birth_date,
                 'bio': p.bio, 'skype': p.skype, 'email': p.email,
                 'phone': p.phone, 'photo': p.photo}
        form = PersonForm(data=mdata)
        self.assertEqual(form.is_valid(), True)
        mdata['name'] = None
        form = PersonForm(data=mdata)
        self.assertEqual(form.is_valid(), False)


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


class TagTest(TestCase):
    def test_tag(self):
        c = Client()
        response = c.get('/')
        self.assertContains(response, '/admin/main/person/1/')
        self.assertContains(response, 'Sorry, no admin link for this.')
        self.assertNotContains(response, '/admin/auth/user/1/')
        c.login(username='admin', password='admin')
        response = c.get('/')
        self.assertContains(response, '/admin/auth/user/1/')
        self.assertNotContains(response, 'Sorry, no admin link for this.')


class CommandTest(TestCase):
    def test_list_models(self):
        import subprocess


        self.assertTrue(os.path.isfile(settings.PROJECT_PATH + '/list_models'))
        a = subprocess.Popen(
            'cd ' + settings.PROJECT_PATH + '/ && ./list_models',
            stdout=subprocess.PIPE, shell=True)
        self.assertTrue(
            os.path.isfile(settings.PROJECT_PATH + '/' +
                           datetime.date.today().strftime('%m_%d_%Y') +
                           '.dat'))
        os.remove(settings.PROJECT_PATH + '/' +
                  datetime.date.today().strftime('%m_%d_%Y') + '.dat')
        res = subprocess.Popen('cd ' + settings.PROJECT_PATH +
                               '/ && ./manage.py list_models',
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE, shell=True).communicate()
        self.assertGreater(res[0].find('class'), -1)
        self.assertGreater(res[1].find('error'), -1)


class SignalsTest(TestCase):
    def test_signals(self):
        c = Client()
        c.get('/non_existing')
        m, created = SignalInfo.objects.get_or_create(pk=1)
        self.assertFalse(created)


class PriorityTest(TestCase):
    def test_request_priority(self):
        c = Client()
        c.get('/')
        pk = Request.objects.all()[0].pk
        response = c.get('/request/{0}/inc/'.format(pk))
        self.assertEqual(response.status_code, 302)
        r = Request.objects.get(pk=pk)
        self.assertEqual(r.priority, 1)
        response = c.get('/request/{0}/dec/'.format(pk))
        self.assertEqual(response.status_code, 302)
        r = Request.objects.get(pk=pk)
        self.assertEqual(r.priority, 0)
