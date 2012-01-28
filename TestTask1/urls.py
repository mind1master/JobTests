from django.conf.urls.\
defaults import patterns, include, url
from django.views.generic import DetailView, ListView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main.models import Person, Request


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', DetailView.as_view(
        model=Person,
        template_name='main_page.html'), {'pk': 1}),
    url(r'^requests/$', ListView.as_view(
        queryset=Request.objects.order_by('time')[:10],
        context_object_name='requests_list',
        template_name='requests.html'
    )),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/', 'template_name': 'login.html'}),
    url(r'^edit/$', 'TestTask1.main.views.editPerson'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
