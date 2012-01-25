# Create your views here.
from django.shortcuts import render_to_response
from main.models import Person

def index(request):
    person = Person.objects.all()[0]
    return render_to_response('main.html', {'person': person})