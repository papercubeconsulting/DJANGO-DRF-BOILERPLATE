# Django
## models package
from django.db import models

class DocumentType(models.Model):
    description = models.CharField("Descripción", max_length=50)
    short_description = models.CharField("Descripción corta", max_length=50)
    code = models.CharField("Código", max_length=50)

    def __str__(self):
        return '{} ({})'.format(self.description, self.code)

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"