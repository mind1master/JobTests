from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.db import connection


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
    datetime = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    app = models.CharField(max_length=256)
    action = models.CharField(max_length=256)
    object_pk = models.PositiveIntegerField()

    def get_instance(self):
        c = ContentType.objects.get(app_label=self.app, model=self.model)
        return c.get_object_for_this_type(pk=self.object_pk)

    def __unicode__(self):
        return '{0} at {1}'.format(self.header, self.datetime)


def _db_table_exists(table):
    cursor = connection.cursor()
    table_names = connection.introspection.get_table_list(cursor)
    return table in table_names


def initial_edit_callback(sender, created, instance, **kwargs):
    if (not _db_table_exists('main_signalinfo')):
        return
    post_save.disconnect(initial_edit_callback)
    post_save.connect(edit_callback)


def edit_callback(sender, created, instance, **kwargs):
    if sender == SignalInfo:
        return
    if kwargs.get('raw', True):
        return
    if created:
        action = 'created'
    else:
        action = 'edited'
    c = ContentType.objects.get_for_model(instance)
    s = SignalInfo(header='\'{0}\' was {1}'.format(instance, action),
        action=action, model=c.model, app=c.app_label, object_pk=c.pk)
    s.save()


def delete_callback(sender, instance, **kwargs):
    if (not sender == SignalInfo):
        action = 'deleted'
        c = ContentType.objects.get_for_model(instance)
        s = SignalInfo(header='\'{0}\' was {1}'.format(instance, action),
            action=action, model=c.model, app=c.app_label, object_pk=c.pk)
        s.save()


post_save.connect(initial_edit_callback)
pre_delete.connect(delete_callback)
