from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):
	user=models.OneToOneField(User,unique=True)
	avatar=ImageWithThumbsField(upload_to="img_user", sizes=((50,50),(80,80)))