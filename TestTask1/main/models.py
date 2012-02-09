from django.db import models, utils
from django.db.models.signals import post_save, pre_delete

class Request(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)

    def __unicode__(self):
        return 'Request at {0}: {1}'.format(self.time, self.header)

    class Meta:
        ordering = ["priority", "time"]


class Person(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    birth_date = models.DateField()
    bio = models.TextField(max_length=400)
    skype = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='avatar', blank=True, null=True)


class SignalInfo(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=256)

    def __unicode__(self):
        return '{0} at {1}'.format(self.body, self.time)


def edit_callback(sender, created, raw, instance, **kwargs):
    if (sender == SignalInfo):
        return
    if (raw):
        return
    if (created):
        action = 'created'
    else:
        action = 'edited'
    s = SignalInfo(body='\'{0}\' was {1}'.format(instance, action))
    try:
        s.save()
    except utils.DatabaseError:
        print 'Table is not created!'


def delete_callback(sender, instance, **kwargs):
    if (not sender == SignalInfo):
        s = SignalInfo(body='\'{0}\' was {1}'.format(instance, 'deleted'))
        s.save()

post_save.connect(edit_callback)
pre_delete.connect(delete_callback)