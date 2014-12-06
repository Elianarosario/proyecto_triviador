from django.conf.urls import patterns, include, url
from django.contrib  import admin
from .views import *

urlpatterns = patterns('',
     	url(r'^$', inicio_view),
	    url(r'^registro/Categoria/$',registro_Categoria, name='Categoria'),
	    url(r'^Categoria/agregar_pregunta/(\d+)/$',agregar_preguntas, name='agregar_preguntas'),
	    url(r'^Categoria/editar/(\d+)/$',Ver_preguntas, name='editar_pregunta'),
	    url(r'^pregunta/editar/(\d+)/$',Editar_pregunta, name='edit_pregunta'),
	    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),
	    #url(r'^registro/pregunta/$',registro_pregunta, name='Pregunta'),
)
