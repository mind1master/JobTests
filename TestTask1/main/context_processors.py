from django.conf import settings


#noinspection PyUnusedLocal
def settings_processor(request):
    return {'settings': settings}


