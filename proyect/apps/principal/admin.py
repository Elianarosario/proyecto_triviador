import models
from django.contrib import admin
from .models import *
admin.site.register(Categoria)
admin.site.register(Pregunta)
admin.site.register(Respuesta)

# Register your models here.
