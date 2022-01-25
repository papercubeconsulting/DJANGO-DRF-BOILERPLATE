

## 2.3. DJANGO SETUP
- #### DEBE TENER INSTALADO DJANGO EN SU ENTORNO VIRTUAL, PARA INSTALARLO USE EN UN ENTORNO VIRTUAL EL COMANDO:
`pip install django`

<p align="center"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/1200px-Django_logo.svg.png" alt="django" style="height:80px;">
</p>

- #### PUEDE USAR EL SIGUIENTE COMANDO PARA VERIFICAR LOS PAQUETES INSTALADOS EN SU ENTRONO VIRTUAL:
`pip freeze`
#### NOTA LOS PAQUETES USUALES QUE SE INSTALAN CON DJANGO POR DEFECTO SON:
`asgiref, certifi, django, pytz, sqlparse, wincertstore`
- #### PARA CREAR UN NUEVO PROYECTO CON DJANGO USE EL COMANDO:
`django-admin startproject project_name`
- #### PARA CREAR UN NUEVO PROYECTO CON DJANGO USE EL COMANDO:
`django-admin startproject project_name`
- #### PARA EJECUTAR EL PROYECTO COMO PRUEBA EN LOCAL USAR (IGNORE LOS MENSAJES DE ERROR):
`python manage.py runserver`

## 2.4. DJANGO DEPLOY
#### DEFINICIONES:
#### [GUNICORN](https://gunicorn.org/): Se encarga de gestionar las peticiones al servidor que tienen que ser gestionadas por django 
#### [NGINX](https://www.nginx.com/): Es el servidor web que gestiona las peticiones junto con gunicorn, incluso es el que gestiona el envío de archivos estáticos.
#### [DOCKER](https://www.docker.com/): Proyecto de código abierto que automatiza el despliegue de aplicaciones mediante el uso de contenedores.

- #### PARA EFECTUAR EL DESPLIEGUE USTED DEBE VERIFICAR QUE TENGA INSTALADO EN SU OS (DOCKER Y DOCKER COMPOSE) USANDO LOS SIGUIENTES COMANDOS EN SU SHELL:
`docker version` 
`docker-compose --version`
- #### TENER EN CUENTA QUE POR SEGURIDAD LA APLICACIÓN EN UN ENTORNO DE PRODUCCIÓN DEBE TENER CAMBIADO EL FLAG DEBUG EN settings.py
`DEBUG = True`
- #### ALLOWED_HOSTS DEL MISMO ARCHIVO DEBE CONTENER LA IP O EL DOMINIO QUE SE USARÁ EN PRODUCCIÓN. SE PUEDE DAR ACCESO A TODAS LAS IPS CON *
`ALLOWED_HOSTS = ['IP']`
`ALLOWED_HOSTS = ['*']`
- #### ASEGURARSE DE QUE LA CONFIGURACIÓN DE LA BASE DE DATOS EN EL MISMO ARCHIVO CORRESPONDA A LO REQUERIDO
`DATABASES ={ ... }`
- #### LA RUTA A LA CARPETA DE ARCHIVOS ESTÁTICOS SE CONFIGURO EN settings.py COMO:
`STATIC_URL = '/static/'`
`STATIC_ROOT = '/code/static/'`
- #### DEBE CREAR EL FOLDER CONFIG CON LOS FOLDERS PARA LA CONFIGURACIÓN DE NGINX Y GUNICORN CON LOS ARCHIVOS DE CONFIGURACIÓN conf.py y local.conf
- #### ASEGURESE DE TENER INSTALADO EN EL ENTORNO VIRTUAL GUNICORN Y PSYCOPG2 (PAQUETE PARA MANEJAR PostgreSQL), PARA INSTALARLO USE EL COMANDO:
`pip install gunicorn`
`pip install psycopg2`
- #### CREE EL ARCHIVO requirements.txt USANDO EL COMANDO:
`pip freeze>requirements.txt`
- #### CREAR LOS ARCHIVOS Dockerfile y docker-compose.yaml SEGÚN EL EJEMPLO DADO EN ESTE REPOSITORIO
- #### COLECCIONAR LOS ARCHIVOS ESTÁTICOS USANDO LOS COMANDOS:
`docker-compose run django_app python manage.py migrate`
`docker-compose run django_app python manage.py collectstatic`
- #### COMPONER EL PROYECTO CON DOCKER COMPOSE:
`docker-compose up --build`
