# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from TestTask1.main.forms import PersonForm
from TestTask1.main.models import Person

@login_required
def editPerson(request):
    p = Person.objects.get(pk=1)
    if request.method == 'POST': # If the form has been submitted...
        form = PersonForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            np = form.save(commit=False)
            if (np.photo.name == None):
                np.photo = p.photo
            np.pk = 1
            np.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = PersonForm(instance=p) # An unbound form

    c = {'form': form, 'profile': p}
    return render_to_response("edit.html", c, context_instance=RequestContext(request))