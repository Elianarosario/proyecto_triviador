from django.conf.urls import patterns, include, url
from django.contrib  import admin
from proyect.apps.usuario.views import registro_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("proyect.apps.usuario.urls")),
    url(r'^', include("proyect.apps.principal.urls")),
)

