from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.
class Perfil(models.Model):
	user=models.OneToOneField(User,unique=True)
	avatar=ImageWithThumbsField(upload_to="img_user", sizes=((50,50),(80,80)))

class Categoria(models.Model):

	nombre_cat=models.CharField(max_length=150)
	def __str__(self):
		return self.nombre_cat


class Pregunta(models.Model):
	nombre_cat= models.ForeignKey(Categoria)
	titulo_pregunta=models.CharField(max_length=150)
	respuesta_1=models.CharField(max_length=200)
	respuesta_2=models.CharField(max_length=200)
	respuesta_3=models.CharField(max_length=200)
	respuesta_correcta=models.CharField(max_length=200)
	def __str__(self):
		return self.titulo_preg

class Respuesta(models.Model):
	resultado= models.IntegerField("0-> incorrecto, 1 -> correcto")
	pregunta=models.ForeignKey(Pregunta)
	reswpuesta




		

