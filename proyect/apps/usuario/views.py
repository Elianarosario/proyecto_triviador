from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate, logout
#from django.contrib.session.backends.db import sessionStore 


import pdb

# Create your views here.
def registro_view(request):
	if request.method=="POST":
		formulario_registro=for_usuario(request.POST)
		if formulario_registro.is_valid():
			nuevo_usuario=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponseRedirect("/")
	else:
			formulario_registro=for_usuario()
	return render_to_response("usuario/registro_usuario.html",{'formulario':formulario_registro},context_instance=RequestContext(request))

def login_view(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if request.session['cant']>3:
			formulario_capt=for_captcha(request.POST)
			if formulario_capt.is_valid():
				pass
			else:
				datos={'formulario':formulario,'formulario_cp':formulario_capt }
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))
		if formulario.is_valid:
				usuario=request.POST['username']
				contrasena=request.POST['password']
				acceso=authenticate(username=usuario,password=contrasena)
				if acceso is not None:
					if acceso.is_active:
						login(request, acceso)
						return HttpResponseRedirect("/user/perfil/")
					else:
						login(request, acceso)
						del request.session['cant']
						return HttpResponseRedirect("/user/active/")
				else:
					request.session['cant']=request.session['cant']+1;
					con=request.session['cant']
					estado_login=True
					mensaje='Los datos ingresados son incorrectos '+str(con)
					
					if con>1:
						formulario_capt=for_captcha()
						datos={'formulario':formulario,'formulario_cp':formulario_capt ,'estado':estado_login,'mensaje':mensaje}
					else:
						datos={'formulario':formulario,'estado':estado_login,'mensaje':mensaje}
					return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))
	else:
		request.session['cant']=0
		formulario=AuthenticationForm()
	return render_to_response("usuario/login.html",{'formulario':formulario},context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")
def perfil_view(request):
	return render_to_response("usuario/perfil.html",{},context_instance=RequestContext(request))
def user_activado_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/user/perfil")
		else:
			if request.method=="POST":
				u=User.objects.get(username=usuario)
				perfil=Perfil.objects.get(user=u)
				formulario=form_perfil(request.POST,request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					u.is_active=True
					u.save()
					return HttpResponseRedirect("/user/perfil/")
			else:
				formulario=form_perfil()
			return render_to_response("usuario/activar.html",{'formulario':formulario},context_instance=RequestContext(request))
	else: 
		return HttpResponseRedirect("/login/")
def modificar_perfil(request):
	if request.user.is_authenticated():
		u=request.user
		usuario=User.objects.get(username=u)
		perfil=Perfil.objects.get(user=usuario)
		if request.method=='POST':
			formulario=form_modifPerfil(request.POST,request.FILES,instance=perfil)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/usuario/"+str(usuario.id)+"/")
		else:
			formulario=form_modifPerfil(instance=perfil)
			return render_to_response('/usuario/modificar_perfil.html',{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")



	

		