from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    birth_date = models.DateField()
    bio = models.TextField(max_length=300)
    skype = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)