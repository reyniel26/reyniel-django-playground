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

The following are just my notes to summarize what I learn. No copyright intended.

### Writing your first Django app, part 1

1. `django-admin startproject mysite`
    - `django-admin startproject mysite .` - this will create manage.py and package in your directory

2. `python manage.py runserver` - Run the server
    - `python manage.py runserver 8080` - Run the server in port 8080
    - `python manage.py runserver 0:8000` - listen to all public ip

**Note:** A project is a collection of configuration and apps for a particular website.
A project can contain multiple apps. An app can be in multiple projects.

3. `python manage.py startapp polls` - create an app in the project
    - Write first view
    - Step 1: Write code in polls/views.py
    - Step 2: Create urls.py in polls directory
    - Step 3: Write code in polls/urls.py
    - Step 4: The next step is to point the root URLconf at the polls.urls module.In mysite/urls.py
    - Step 5: Write code in mysite/urls.py

**Note:** The `include()` function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The `path()` function is passed four arguments, two required: route and view, and two optional: kwargs, and name. At this point, it’s worth reviewing what these arguments are for.

### Writing your first Django app, part 2

1. `python manage.py migrate`
    - The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app

**Note:** Django follows the DRY Principles or Don't Repeat yourself

2. `python manage.py makemigrations polls`
    - After adding the polls app in installed apps in settings, run this command
    - By running **makemigrations**, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

3. `python manage.py sqlmigrate polls 0001`
    - The **sqlmigrate** command takes migration names and returns their SQL:
    - The **sqlmigrate** command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

4. `python manage.py check`
    - If you’re interested, you can also run `python manage.py check`; this checks for any problems in your project without making migrations or touching the database.

5. Running migration
    - Run `python manage.py makemigrations` to create migrations for those changes
    - Run `python manage.py migrate` to apply those changes to the database.

Playing with API

6. `python manage.py shell`

Creating an admin user

7. `python manage.py createsuperuser`

    - sample account that I created for this test *admin:Ironman1234*

### Writing your first Django app, part 3

Routine:
1. Create View in views.py
2. Wire it to the urls.py
3. Create template *templates/folder/html file*

- *django.shortcuts* module is very usefull
- Use `{% url %}` template tag , format is {% url name data %}

### Writing your first Django app, part 4

- `forloop.counter` in templates
- for post request, it must have `{% csrf_token %}`
- Always return an *HttpResponseRedirect* after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
- `reverse()` This function helps avoid having to hardcode a URL in the view function
- **Best Practice Alert!!!:** Race condition is where 2 python process try to execute to alter the database such as increment something. To avoid error caused by this incident see the [Avoiding race conditions using F()](https://docs.djangoproject.com/en/4.1/ref/models/expressions/#avoiding-race-conditions-using-f)

Use generic views: Less code is better

1. Convert the URLconf.
2. Delete some of the old, unneeded views.
3. Introduce new views based on Django’s generic view

- *ListView*
- *DetailView*
- For generic views, the `template_name` attribute is used to tell Django to use a specific template name instead of the autogenerated default template name.

### Writing your first Django app, part 5

Basic testing strategies
- **“test-driven development”** - write the test before writing the code

Writing our first test
1. We identify a bug
2. Create a test to expose the bug
    - You can create automated test in test.py of each app
    - `from django.test import TestCase`
3. Running tests
    - `python manage.py test polls`- python manage.py *(app name)* polls , will run the test for polls only or specified app
    - `python manage.py test` - will run all test
4. Fixing the bug
5. Run the test again

Test a view
- The Django test client
    - `from django.test.utils import setup_test_environment`- **setup_test_environment()** installs a template renderer which will allow us to examine some additional attributes on responses such as response.context that otherwise wouldn’t be available. Note, this method does not create test database
    - `from django.test import Client`

django.test.TestCase
- `self.assertIs()`
- `self.assertEqual()`
- `self.assertContains()`
- `self.assertQuerysetEqual()`

**Note:** The database is reset for each test method, so the first question is no longer there, and so again the index shouldn’t have any questions in it.

**Best Practice Alert!!!:**
- a separate TestClass for each model or view
- a separate test method for each set of conditions you want to test
- test method names that describe their function

### Writing your first Django app, part 6

- `django.contrib.staticfiles`
- create static folder inside your app
- create sample css `polls/static/polls/style.css`. Because of how the **AppDirectoriesFinder** staticfile finder works, you can refer to this static file in Django as polls/style.css, similar to how you reference the path for templates.

> **Note:** Static file namespacing
>> Just like templates, we might be able to get away with putting our static files directly in polls/static (rather than creating another polls subdirectory), but it would actually be a bad idea. Django will choose the first static file it finds whose name matches, and if you had a static file with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them. That is, by putting those static files inside another directory named for the application itself.

- `{% static %}`  template tag generates the absolute URL of static files.

### Writing your first Django app, part 7

1. Customize the admin form

**Best Practice Alert!!!:**
- You’ll follow this pattern – create a model admin class, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.

2. Customize the admin change list

- `@admin.display` - decorator to improve display of particular column or function
- `list_display = ()`
-  `list_filter = []`
- `search_fields = []`

Customize the admin look and feel
- Overide the admin html templates
1. Create template folder in root, and create admin folder inside
2. Update the **TEMPLATES** in `site/settings.py`
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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
```
3. Copy the template you want to override, for example *base_site.html*. To locate the location of the html you can run this code, `py -c "import django; print(django.__path__)"`. Then go to **django/contrib/admin/templates**


### Some pointers to consider
Visit https://docs.djangoproject.com/en/4.1/intro/whatsnext/

