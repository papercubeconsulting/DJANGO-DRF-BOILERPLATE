"""
Django settings for pethospital project.
"""
import environ
import os

# import base settings
from .base import *

# Take environment variables from .env file
env = environ.Env()
environ.Env.read_env(BASE_DIR / 'config/settings/.dev.env')

# SECRET KEY for Django App
SECRET_KEY = env('DJANGO_SECRET_KEY')

# DJANGO EBUG VARIABLE
DEBUG = env('DJANGO_DEBUG_VARIABLE')

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Application definition
DEV_DJANGO_APPS=['django_extensions']

INSTALLED_APPS = BASE_INSTALLED_APPS + DEV_DJANGO_APPS

MIDDLEWARE = BASE_MIDDLEWARES

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db('BD_URL'),
}

# GRAPH MODELS
GRAPH_MODELS = {
    'all_applications':True,
    'group_models':True,
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# * Sobre el guardado de archivos en el servidor (https://stackoverflow.com/questions/5517950/django-media-url-and-media-root)
# * Working with static files (https://docs.djangoproject.com/en/3.1/howto/static-files/)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'data'