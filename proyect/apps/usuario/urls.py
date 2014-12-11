from django.conf.urls import patterns, include, url
from django.contrib  import admin
from .views import *

urlpatterns = patterns('',
     url(r'^RegistroUser/$', registro_view),
     url(r'^login/$', login_view),
     url(r'^logout/$', logout_view),
     url(r'^user/perfil/$',perfil_view),
     url(r'^user/active/$',user_activado_view),
     url(r'^modificar_perfil/$',modificar_perfil),     
)
