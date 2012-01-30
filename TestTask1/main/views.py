# Create your views here.
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson
from TestTask1.main.forms import PersonForm
from TestTask1.main.models import Person

@login_required
def editPerson(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PersonForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            np = form.save(commit=False)
            np.pk = 1
            np.save()
            return HttpResponse(simplejson.dumps({'response': '', 'result': 'success'}))
            #return HttpResponseRedirect('/') # Redirect after POST
        else:
        # Заполняем словарь response ошибками формы, ключ - название поля
            response = {}
            for k in form.errors:
                # Теоретически у поля может быть несколько ошибок...
                response[k] = form.errors[k][0]
            return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
    else:
        p = Person.objects.get(pk=1)
        form = PersonForm(instance=p) # An unbound form

    c = {'form': form}
    return render_to_response("edit.html", c, context_instance=RequestContext(request))