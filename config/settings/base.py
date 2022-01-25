"""
Django settings for pethospital project. (BASE)
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

## * [SECTION] APPs
DEFAULT_DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PART_APPS = [
    'rest_framework', # Default rest framework app (https://www.django-rest-framework.org/)
    'rest_framework.authtoken', # Token authentication https://www.django-rest-framework.org/api-guide/authentication/
    'django_filters', # Django filters rest framework integration (https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html)
    'rest_auth', # Django rest auth (https://django-rest-auth.readthedocs.io/en/latest/installation.html)
]

CUSTOM_APP = ['pethospital']

BASE_INSTALLED_APPS = DEFAULT_DJANGO_APPS + THIRD_PART_APPS + CUSTOM_APP

## * [SECTION] MIDDLEWAREs
DEFAULT_DJANGO_MIDDLEWARES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
BASE_MIDDLEWARES = DEFAULT_DJANGO_MIDDLEWARES

## * [SECTION] URLs
ROOT_URLCONF = 'config.urls'

## * [SECTION] TEMPLATEs
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # * Para configurar templates en Django (https://docs.djangoproject.com/en/3.1/topics/templates/)
        # * templates cambio de contraseña (https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html)
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

## * [SECTION] REST FRAMEWORK Config
REST_FRAMEWORK = {
    # Default authentication classes (https://www.django-rest-framework.org/api-guide/settings/#default_authentication_classes)
    # Authentication classes (https://www.django-rest-framework.org/api-guide/authentication/#authentication)
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    # Default permission to use apis (https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy)
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # Default filter backend methods (https://www.django-rest-framework.org/api-guide/settings/#default_filter_backends)
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

## * [SECTION] REST AUTH Config
REST_SESSION_LOGIN = False # Disable session login in Login API view (https://django-rest-auth.readthedocs.io/en/latest/configuration.html)
REST_USE_JWT = True # To use JWT with REST AUTH (https://django-rest-auth.readthedocs.io/en/latest/installation.html#jwt-support-optional)
OLD_PASSWORD_FIELD_ENABLED = False # Set it to True if you want to have old password verification on password change endpoint (https://django-rest-auth.readthedocs.io/en/latest/configuration.html)

## * [SECTION] JWT AUTH Config
# For more details review (https://jpadilla.github.io/django-rest-framework-jwt/)
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_ALLOW_REFRESH': True, #to enable refresh
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True, #5 min default
    'JWT_AUTH_HEADER_PREFIX': 'Bearer'
}

## * [SECTION] WSGI Config
WSGI_APPLICATION = 'config.wsgi.application'

## * [SECTION] Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

## * [SECTION] Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-PE'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'