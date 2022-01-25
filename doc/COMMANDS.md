## COMMANDS:

#### Create an super user:
- `python manage.py createsuperuser`
#### Create an app:
- `python manage.py startapp appname`
#### Load a json file:
- `python manage.py loaddata db.json`
#### Documents the ERD (Only DEV):
- `conda install graphviz`
- `python manage.py graph_models --pydot -a -g -o doc/pethospital/ERD.png`