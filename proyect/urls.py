from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('proyect.apps.principal.urls')),
    url(r'^', include('proyect.apps.usuario.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
  url('', include('social.apps.django_app.urls', namespace='social')),
)


