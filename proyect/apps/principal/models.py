from django.db import models


# Create your models here.


class Categoria(models.Model):
	nombre_categoria=models.CharField(max_length=150)
	def __str__(self):
		return self.nombre_categoria



class Pregunta(models.Model):
	categoria=models.ForeignKey(Categoria)
	titulo_pregunta=models.CharField(max_length=500)
	respuesta_correcta=models.CharField(max_length=400)
	respuesta_opcional=models.TextField()
	def __str__(self):
		return self.titulo_pregunta


class Respuesta(models.Model):
	tiempo_resp=models.IntegerField()
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta
	
	
