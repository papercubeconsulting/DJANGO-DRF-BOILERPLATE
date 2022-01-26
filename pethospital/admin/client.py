# Django
from django.contrib import admin

# Custom models
from pethospital.models import Client

class ClientAdmin (admin.ModelAdmin):
    # Muestra los campos que se deben mostrar en la página del modelo
    list_display = ('pk','user','document_type','document_number','validated','created_at','modified_at')
    # Muestra los campos que tendran un enlace a la página de la entidad
    list_display_links = ('pk','user')
    # Muestra los campos que se pueden editar en la página del modelo

    # Muestra la lista de campos con los que se puede buscar una entidad en la página del modelo
    search_fields = ('user__username',
                    'user__fist_name',
                    'user__last_name',
                    'document_number')

    # Muestra la lista de filtros que se mostrarán en la barra lateral
    list_filter = (
        'validated',
        'created_at',
        'modified_at'
    )

    # Muestra la estructura de la página de edición/creación de la entidad
    fieldsets = (
        ('Datos Cliente:', {
            'fields': (('user','validated'),('document_type','document_number'),)
        }),
        ('Metadata:', {
            'fields': (('created_at','modified_at'),)
        }),
    )

    readonly_fields = ('created_at','modified_at')

admin.site.register(Client, ClientAdmin)
