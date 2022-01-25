"""pethospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from rest_framework_jwt.views import refresh_jwt_token

#* cambio de titulos del sitio de administración
admin.site.site_header = "Administración Pethospital"
admin.site.site_title = "Portal de Administración - Pethospital"
admin.site.index_title = "Bienvenido al Portal de Administración - Pethospital"

urlpatterns = [
    #* [GROUP] BASIC DJANGO
    path('admin/', admin.site.urls),
    #* [GROUP] API
    # Se agregan enpoints de rest-auth (https://django-rest-auth.readthedocs.io/en/latest/installation.html)
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/token/refresh/', refresh_jwt_token),
]
