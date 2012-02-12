# Create your views here.
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.utils import simplejson
from django.views.generic.list import ListView
from TestTask1.main.forms import PersonForm
from TestTask1.main.models import Person, Request

@login_required
def editPerson(request):
    p = Person.objects.get(pk=1)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES) #
        if form.is_valid():
            np = form.save(commit=False)
            if (np.photo.name == None):
                np.photo = p.photo
            np.pk = 1
            np.save()
            return HttpResponse(simplejson.dumps({'response': np.photo.url, 'result': 'success'}))
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
    else:
        form = PersonForm(instance=p) # An unbound form

    c = {'form': form, 'profile': p}
    return render_to_response("edit.html", c, context_instance=RequestContext(request))


class RequestList(ListView):
    queryset = Request.objects.order_by('-priority', 'time')
    context_object_name = 'requests_list'
    template_name = 'requests.html'
    paginate_by = 10


def changePriorityView(request, pk, action):
    r = Request.objects.get(pk=pk)
    if action == 'inc':
        r.priority = r.priority + 1
    else:
        r.priority = r.priority - 1
    r.save()
    queryset = Request.objects.order_by('-priority', 'time')
    for index, item in enumerate(queryset):
        if r.pk == item.pk:
            break

    return redirect('/requests/{0}'.format((index / 10) + 1))