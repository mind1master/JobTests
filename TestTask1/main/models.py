from django.db import models

#TODO: add PIL to requirements
class Request(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)


class Person(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    birth_date = models.DateField()
    bio = models.TextField(max_length=400)
    skype = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='avatar', blank=True, null=True)
