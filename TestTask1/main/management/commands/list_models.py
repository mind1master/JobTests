from django.core.management.base import NoArgsCommand
from django.db import models, utils

class Command(NoArgsCommand):
    help = 'Lists all models and object count'

    def handle_noargs(self, **options):
        try:
            models_list = models.get_models()
            for m in models_list:
                self.stdout.write('%s - %d objects \n' % (m, m.objects.count()))
                self.stderr.write('error: %s - %d objects \n' % (m, m.objects.count()))
        except utils.DatabaseError:
            self.stderr.write('error: Can\' get models list. Probably you didn\'t perform any syncdb.')