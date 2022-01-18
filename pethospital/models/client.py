# Django
## model User
from django.contrib.auth.models import User
## models package
from django.db import models

# The user issue: https://codigofacilito.com/articulos/django-user-model

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #Campos de creación y modificación
    created_at = models.DateTimeField("Fecha de creación",auto_now_add=True)
    modified_at = models.DateTimeField("Fecha de edición",auto_now=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"