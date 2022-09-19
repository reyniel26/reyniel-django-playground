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

### Writing your first Django app, part 2

1. `python manage.py migrate`
  - The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app

Django follows the DRY Principles or Don't Repeat yourself

2. `python manage.py makemigrations polls`
  - After adding the polls app in installed apps in settings, run this command
  - By running **makemigrations**, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

3. `python manage.py sqlmigrate polls 0001`
  - The **sqlmigrate** command takes migration names and returns their SQL:
  - The **sqlmigrate** command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

4. `python manage.py check`
  - If you’re interested, you can also run **python manage.py check**; this checks for any problems in your project without making migrations or touching the database.

5. Running migration
  - Run **python manage.py makemigrations** to create migrations for those changes
  - Run **python manage.py migrate** to apply those changes to the database.

Playing with API

6. `python manage.py shell`

Creating an admin user

7. `python manage.py createsuperuser`

sample account that I created for this test *admin:Ironman1234*

