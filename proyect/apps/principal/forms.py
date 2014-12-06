#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import *

class form_Categoria(ModelForm):
	class Meta:
		model=Categoria
class form_Pregunta(ModelForm):
	titulo_pregunta=forms.CharField(required=True,label="Pregunta :")
	class Meta:
		model=Pregunta
		exclude=['categoria']
class form_Respuesta(ModelForm):
		class Meta:
			model=Pregunta
			exclude=['pregunta']
				


		