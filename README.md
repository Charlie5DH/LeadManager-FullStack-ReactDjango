## Lead Manager React App

This is the backend for the app. The backend is developed in Django, an runs as a stand alone backend. 

### Configurations

For the configuration was created a virtual environment using `pipenv`. For this we need to install `pipenv`. We also have to install Django, the `djangorestframework` library and `django-rest-knox` to manage authentications, we do this inside the virtual env.

`pip install pipenv`

`pipenv install django djangorestframework django-rest-knox`

Then, we have to start a Project (which is not the same as an application). A project in Django means to create the Django main environment, the configuration folder. Then, we create the app. The app contains the views and the URLs.

`django-admin startproject leadmanager`

`python manage.py startapp leads`

After created the models, in the `models.py` file, we have to migrate to the database. We can use the command `python manage.py makemigrations leads` to migrate the models to the database.

