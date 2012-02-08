from django.conf.urls.\
defaults import patterns, include, url
from django.views.generic import DetailView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from main.models import Person
from main.views import RequestList


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^requests/(?P<page>\d+)/$', RequestList.as_view()),
                       url(r'^$', DetailView.as_view(
                           model=Person,
                           template_name='main_page.html'), {'pk': 1}),
                       url(r'^requests/$', RequestList.as_view()),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                               {'next_page': '/', 'template_name': 'login.html'}),
                       url(r'^edit/$', 'TestTask1.main.views.editPerson'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
if settings.DEBUG:
# static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
