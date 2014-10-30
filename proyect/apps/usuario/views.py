from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from django.contrib.auth.forms import UserCreationForm 
import pdb

# Create your views here.
def registro_view(request):
	if request.method=="POST":
		formulario_registro=for_usuario(request.POST)
		if formulario_registro.is_valid():
			formulario_registro.save()
			return HttpResponse("REGISTRADO")
	else:
			formulario_registro=for_usuario()
	return render_to_response("usuario/registro_usuario.html",{'formulario':formulario_registro},context_instance=RequestContext(request))

