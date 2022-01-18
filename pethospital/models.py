# Django
## model User
from django.contrib.auth.models import User
## regex validator
from django.core.validators import RegexValidator
## models package
from django.db import models

# The user issue: https://codigofacilito.com/articulos/django-user-model

class StaffRole(models.Model):
    name = models.CharField("Rol", max_length=50)
    code = models.CharField("Código", max_length=50)
    role_group = models.CharField("Grupo Rol", max_length=50)
    base_hour_cost = models.FloatField("Costo unitario base (PEN)",default=0)

    def save(self, *args, **kwargs):
        self.base_hour_cost = round(self.base_hour_cost, 2)
        super(StaffRole, self).save(*args, **kwargs)

    def __str__(self):
        return '{} ({})'.format(self.name, self.code)

class StaffUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    roles = models.ManyToManyField(StaffRole,related_name="roles")
    hour_cost = models.FloatField("Costo unitario (PEN)",default=0)
    #Campos de creación y modificación
    created_at = models.DateTimeField("Fecha de creación",auto_now_add=True)
    modified_at = models.DateTimeField("Fecha de edición",auto_now=True)

    def save(self, *args, **kwargs):
        self.hour_cost = round(self.hour_cost, 2)
        super(StaffUser, self).save(*args, **kwargs)

    def __str__(self):
        return 'Colaborador ({} {})'.format(self.user.first_name, self.user.last_name)

class ClientUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #Campos de creación y modificación
    created_at = models.DateTimeField("Fecha de creación",auto_now_add=True)
    modified_at = models.DateTimeField("Fecha de edición",auto_now=True)

"""class Enterprise(models.Model):
        name = models.CharField("Razón Social", max_length=255)
        ruc_regex = RegexValidator(regex=r'^[0-9]{11}$', message="El número de RUC debe tener un formato válido.")
        ruc = models.CharField("ruc",validators=[ruc_regex],max_length=12, blank=False,unique=True)
        #Campos de creación y modificación
        created_at = models.DateTimeField("Fecha de creación",auto_now_add=True)
        modified_at = models.DateTimeField("Fecha de edición",auto_now=True)
"""