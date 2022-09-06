# reyniel-django-playground
My Django playground. The place where I can do want ever I want, I can test what ever I want, just to learn Django.


## Very important note
Hide the secret key , you can do the following code in settings.py
```
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'somesecret')
```

## Some notes:
Source link : https://www.djangoproject.com/start/
### Writing your first Django app, part 1

1. `django-admin startproject mysite`
  - `django-admin startproject mysite .` - this will create manage.py and package in your directory

2. `python manage.py runserver` - Run the server
  - `python manage.py runserver 8080` - Run the server in port 8080
  - `python manage.py runserver 0:8000` - listen to all public ip

Note: A project is a collection of configuration and apps for a particular website.
A project can contain multiple apps. An app can be in multiple projects.

3. `python manage.py startapp polls` - create an app in the project
  - Write first view
  - Step 1: Write code in polls/views.py
  - Step 2: Create urls.py in polls directory
  - Step 3: Write code in polls/urls.py
  - Step 4: The next step is to point the root URLconf at the polls.urls module.In mysite/urls.py
  - Step 5: Write code in mysite/urls.py

Note: The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name. At this point, it’s worth reviewing what these arguments are for.


