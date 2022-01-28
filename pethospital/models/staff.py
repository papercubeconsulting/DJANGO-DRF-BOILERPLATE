# Django
## model User
from django.contrib.auth.models import User
## models package
from django.db import models

## utils import
from pethospital.utils import get_profile_photo_path

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

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    roles = models.ManyToManyField(StaffRole,related_name="roles")
    hour_cost = models.FloatField("Costo unitario (PEN)",default=0)
    profile_image = models.ImageField("Imagen de perfil",upload_to=get_profile_photo_path,blank=True)
    #Campos de creación y modificación
    created_at = models.DateTimeField("Fecha de creación",auto_now_add=True)
    modified_at = models.DateTimeField("Fecha de edición",auto_now=True)

    def save(self, *args, **kwargs):
        self.hour_cost = round(self.hour_cost, 2)
        super(Staff, self).save(*args, **kwargs)

    def __str__(self):
        return 'Colaborador ({} {})'.format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Staff"