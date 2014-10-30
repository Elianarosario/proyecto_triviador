from django.conf.urls import patterns, include, url
from django.contrib  import admin
from .views import *

urlpatterns = patterns('',
     url(r'^RegistroUser/$', registro_view),
    # url(r'^blog/', include('blog.urls')),

   
)
