from django.shortcuts import render_to_response
from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.
class Perfil(models.Model):
	user=models.OneToOneField(User,unique=True)
	avatar=ImageWithThumbsField(upload_to="img_user", sizes=((50,50),(80,80)))

# creando los modelos para el juego Trivia

			


	



