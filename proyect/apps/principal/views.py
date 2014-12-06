from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import *
from .models import *

# Create your views here.
def inicio_view(request):
	usuarios=User.objects.all()
	return render_to_response("principal/inicio.html",{'usuarios':usuarios},context_instance=RequestContext(request))

def registro_Categoria(request):
	titulo="Regitro de categorias"
	cateorias=Categoria.objects.all()
	if request.method=="POST":
		formulario=form_Categoria(request.POST)
		if formulario.is_valid():
			formulario.save()
			estado=True
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'temas':temas}
			return render_to_response("principal/registro_categoria.html",datos,context_instance=RequestContext(request))
	else:
		formulario=form_Categoria()
	datos={'titulo':titulo,'formulario':formulario,'Categoria':Categoria}
	return render_to_response("principal/registro_categoria.html",datos,context_instance=RequestContext(request))

def agregar_preguntas(request,id):
	tema=Tema.objects.get(id=int(id))
	titulo="Registrar preguntas a la categoria "+Categoria.nombre_categoria
	titulo2="Registrar las respuestas"
	if request.method=="POST":
		formulario=form_Pregunta(request.POST)
		formulario2=form_Respuesta(request.POST)
		if formulario.is_valid() and formulario2.is_valid():
			pregunta=formulario.save(commit=False)
			pregunta.categoria=categorias
			pregunta.save()
			respuesta=formulario2.save(commit=False)
			respuesta.pregunta=pregunta
			respuesta.save()
			estado=True
			formulario=form_pregunta()
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return render_to_response("principal/registro_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=form_Pregunta()
		formulario2=form_Respuesta()
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}
	return render_to_response("principal/registro_preguntas.html",datos,context_instance=RequestContext(request))
def Ver_preguntas(request,id):
	Categoria=Categoria.objects.get(id=int(id))
	preguntas=Pregunta.objects.filter(categoria=categoria)
	datos={'categoria':categoria,'preguntas':preguntas}
	return render_to_response("principal/ver_preguntas.html",datos,context_instance=RequestContext(request))

def Editar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	titulo="Editar pregunta"
	titulo2="Editar las respuestas"
	if request.method=="POST":
		formulario=form_pregunta(request.POST,instance=pregunta)
		formulario2=form_respuesta(request.POST,instance=respuesta)
		if formulario.is_valid() and formulario2.is_valid():
			formulario.save()
			formulario2.save()
			estado=True
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return render_to_response("principal/registro_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=fpregunta(instance=pregunta)
		formulario2=frespuesta(instance=respuesta)
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}
	return render_to_response("principal/registro_preguntas.html",datos,context_instance=RequestContext(request))

def eliminar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	id=pregunta.tema.id
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	pregunta.delete()
	respuesta.delete()
	return HttpResponseRedirect("/categoria/editar/"+str(id)+"/")