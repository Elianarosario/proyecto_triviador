from django.conf.urls import patterns, include, url
from django.contrib  import admin
from .views import *

urlpatterns = patterns('',
     	url(r'^$', inicio_view),
	    url(r'^registro/Categoria/$',registro_Categoria, name='Categoria'),
	    url(r'^Categoria/registro_pregunta/(\d+)/$',agregar_preguntas, name='agregar_preguntas'),
	    url(r'^categoria/add/(\d+)/$',ver_preguntas, name='ver_pregunta'),
	    url(r'^pregunta/editar/(\d+)/$',Editar_pregunta, name='editar_pregunta'),
	    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),    
)
