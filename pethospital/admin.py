# Django
from django.contrib import admin

from .models import Colaborator
class ColaboratorAdmin (admin.ModelAdmin):
    # Muestra los campos que se deben mostrar en la página del modelo
    list_display = ('pk','user', 'hour_cost','created_at', 'modified_at')
    # Muestra los campos que tendran un enlace a la página de la entidad
    list_display_links = ('pk', 'user')
    # Muestra los campos que se pueden editar en la página del modelo
    #list_editable = ['position']

    # Muestra la lista de campos con los que se puede buscar una entidad en la página del modelo
    search_fields = ('user__username',
                     'user__fist_name',
                     'user__last_name')

    # Muestra la lista de filtros que se mostrarán en la barra lateral
    list_filter = (
        'created_at',
        'modified_at',
    )

    filter_horizontal = ['roles']
    # Muestra la estructura de la página de edición/creación de la entidad
    fieldsets = (
        ('Datos Colaborador:', {
            'fields': (('user', 'hour_cost'),)
        }),
         ('Roles:', {
            'fields': ['roles']
        }),
        ('Metadata:', {
            'fields': (('created_at', 'modified_at'),)
        }),
    )

    readonly_fields = ('created_at', 'modified_at')

admin.site.register(Colaborator, ColaboratorAdmin)
