"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('radiator.views',
    url(r'^$', 'index', name='index'),
    url(r'^alarm/(?P<id>[^/]+)/$', 'alarm', name='alarm'),
#    url(r'^info$', 'info', name='info'),
    url(r'^light/(?P<val>[^/]+)/$', 'light_action', name='light'),
)
