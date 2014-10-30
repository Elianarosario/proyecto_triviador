#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class for_usuario(UserCreationForm):
	username=forms.CharField(max_length=40,required=True,help_text=False,label="Nickname")
	password=forms.CharField(help_text=False,label="contraseña de confirmacion")
	first_name=forms.CharField(max_length=50,required=True,label="Apellido")
	last_name=forms.CharField(max_length=50,required=True,label="Nombre")
	email=forms.EmailField(max_length=100,required=True,label="Email")
	class Meta:
		model=User
		fields=("username","password","first_name","last_name","email")
	def save(self, commit=True):
		user=super(for_usuario,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user



