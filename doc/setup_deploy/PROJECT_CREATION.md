
## 2.1. PROJECT CREATION:

#### NOTA: Yo ejecuto el proyecto local en OS Windows. Además de ello uso Anaconda para el desarrollo de proyectos en Python disponible en: (https://www.anaconda.com/products/individual)

<p align="center">
<br/>
<img src="https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png" alt="anaconda"  style="height:100px;">
<br/>
<br/>
</p>

#### A. Aperture el Anaconda Prompt o entre a Anaconda desde CMD con el comando:
`C:/Users/User/anaconda3/Scripts/activate`
#### B. Es [buena práctica](https://medium.com/@m.monroyc22/configurar-entorno-virtual-python-a860e820aace) crear un entorno visual usando el comando:
`conda create -n venv_project python=3.6`
#### C. Activar el entorno virtual usando el comando:
`conda activate venv_project`
#### D. Instalar las dependencias base:
`pip install django gunicorn psycopg2-binary django-environ`
#### E. Documentar las dependencias con:
`pip freeze>requirements/stage.txt`
#### F. Iniciar un nuevo proyecto en django
`django-admin startproject project_name .`
#### G. Modificar los settings del proyecto
#### H. Efectuar las migraciones
`python manage.py makemigrations`
`python manage.py migrate`
#### I. Ejecutar el proyecto
`python manage.py runsever`
