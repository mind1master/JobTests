from django.conf.urls.\
defaults import patterns, include, url
from django.views.generic.detail import DetailView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main.models import Person

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', DetailView.as_view(
        model=Person,
        template_name='main.html'), {'pk': 1}),
    # url(r'^TestTask1/', include('TestTask1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
