from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from radiator import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'alarm', views.AlarmViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'radiator.views.index', name='index'),
    url(r'^alarm/(?P<id>[^/]+)/$', 'radiator.views.alarm', name='alarm'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
