# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from main.forms import PersonForm
from main.models import Person

@login_required
def editPerson(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PersonForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            np = form.save(commit=False)
            np.pk = 1
            np.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        p = Person.objects.get(pk=1)
        form = PersonForm(instance=p) # An unbound form

    c = {'form': form}
    return render_to_response("edit.html", c, context_instance=RequestContext(request))