# Django
# model User
from django.contrib.auth.models import User
# models package
from django.db import models

# custom model
from pethospital.models import DocumentType

# validators
from pethospital.utils import validate_document_number

# The user issue: https://codigofacilito.com/articulos/django-user-model

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document_type = models.ForeignKey(DocumentType,verbose_name="Tipo de documento",null=True,on_delete=models.SET_NULL)
    document_number = models.CharField("Número de documento",max_length=12,default="")
    validated = models.BooleanField("Validado por operaciones",default=False)
    # Campos de creación y modificación
    created_at = models.DateTimeField("Fecha de creación",auto_now_add=True)
    modified_at = models.DateTimeField("Fecha de edición",auto_now=True)

    def clean(self, *args, **kwargs):
        validate_document_number(self)
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Cliente Nº{}'.format(self.id)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
