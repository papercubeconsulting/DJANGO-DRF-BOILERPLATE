
## 2.2. LOCAL PROJECT SETUP:

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
#### D. Instalar las dependencias de desarrollo:
`pip install -r requirements/dev.txt`
#### E. Asegurar que se cuente con el cambio en archivo manage.py
`os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')`
#### F. Ejecutar el script de startup
`python startup/startup.py`
#### G. Ejecutar el proyecto
`python manage.py runsever`
