# Chapter 07 - Django Views and URL Mapping

In this chapter, we will start working on a **real-world Django project structure** and learn how **Views** and **URLs** work together.

So far, we have covered the basic Django setup, project structure, and app creation. Now we will start the main Django development workflow with **Views and URL Mapping**.

---

## 1. What is a Django View?

Django follows the **MVT (Model-View-Template)** architecture.

The **V** in MVT stands for **View**.
A Django **view** is responsible for processing a request and returning a response to the user.

For example, when a user enters a URL in the browser:

```text
http://127.0.0.1:8000/blog/
```

Django needs to decide:
> Which function or class should run for this URL?
The **URL configuration** maps the URL to the appropriate **View**.
The View then processes the request and returns a response.

---

## 2. View and URL Combination

Views and URLs are closely connected.
A View alone is not enough if we want the browser to access it through a URL.
The basic relationship is:

```text
User enters URL
       ↓
URL Configuration
       ↓
View
       ↓
Response
       ↓
Browser
```

For example:

```text
/blog/
   ↓
home()
   ↓
"Welcome to Blog"
```

---

## 3. Two Important Concepts

There are two major concepts in this chapter:

### View

A View can be:

- A function
- A class

A View receives a request and returns a response.

```python
def home(request):
    ...
```

or later:

```python
class HomeView:
    ...
```

### URL Configuration

URL configuration is the mapping between a URL path and a View.
For example:

```python
path("blog/", views.home)
```

This means:

```text
/blog/
   ↓
views.home
```

---

## 4. Real-World Project Setup

In real-world projects, it is a good practice to use a **separate virtual environment for each project**.

Why?

Different projects may require different versions of:

- Django
- Python packages
- Third-party libraries
- Dependencies

For example:

```text
Project 1
    ↓
Django Version A

Project 2
    ↓
Django Version B
```

A virtual environment keeps these dependencies isolated.

---

## 5. Create a Main Project Folder

Suppose we create a folder named:

```text
django-tutorial/
```

Inside it, create another folder for the project:

```text
django-tutorial/
└── dj1/
```

Move into the project folder:

```bash
cd dj1
```

This `dj1` folder will be our main working folder.

---

## 6. Create a Virtual Environment

There are different ways to create a Python virtual environment.

### Method 1: Using Python's `venv`

```bash
python -m venv venv
```

On systems where `python3` is used:

```bash
python3 -m venv venv
```

This creates:

```text
venv/
```

inside the current directory.

---

## 7. Using `virtualenv`

Another option is the `virtualenv` package.

Install it if required:

```bash
pip install virtualenv
```

Then create the environment:

```bash
virtualenv venv
```

Both approaches create an isolated Python environment.

For most beginners, Python's built-in `venv` is sufficient.

---

## 8. Activate the Virtual Environment

After creating the virtual environment, activate it.

### Windows

```bash
venv\Scripts\activate
```

After activation, you may see something similar to:

```text
(venv)
```

at the beginning of the terminal prompt.

### macOS / Linux

```bash
source venv/bin/activate
```

After activation:

```text
(venv)
```

indicates that the virtual environment is active.

---

## 9. Install Django

Once the virtual environment is activated, install Django:

```bash
pip install django
```

On systems where `pip3` is used:

```bash
pip3 install django
```

Django will now be installed inside the virtual environment.

---

## 10. Check Django Version

To verify that Django is installed:

```bash
django-admin --version
```

You can also use:

```bash
python -m django --version
```

Example:

```text
5.x.x
```

The exact version depends on the version installed in your environment.

---

## 11. Create the Django Project

Now create the Django project.

Syntax:

```bash
django-admin startproject project_name
```

For this project:

```bash
django-admin startproject dj1
```

This creates the Django project structure.

---

## 12. Project Structure

After creating the project, the structure looks like:

```text
dj1/
│
└── dj1/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

When using:

```bash
django-admin startproject dj1
```

inside the outer `dj1` directory, the project can result in a nested structure such as:

```text
dj1/
│
└── dj1/
    ├── manage.py
    └── dj1/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
```

A cleaner and commonly used structure is:

```text
django-tutorial/
│
├── venv/
│
└── dj1/
    ├── manage.py
    └── dj1/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
```

The important point is that **`manage.py` is located in the outer project directory**.

---

## 13. Move Into the Django Project Directory

Move into the directory containing `manage.py`:

```bash
cd dj1
```

Now you should be able to see:

```text
manage.py
```

This is important because most Django management commands are executed through `manage.py`.

---

## 14. Create the First Django App

Now create our first application.

Use:

```bash
python manage.py startapp blog
```

On macOS/Linux:

```bash
python3 manage.py startapp blog
```

This creates a new app named:

```text
blog
```

---

## 15. Project vs Application

At this point, understand the naming carefully.

```text
Django Project
      ↓
     dj1

Django App
      ↓
    blog
```

The project is the complete Django application, while the app handles a particular feature.

For example:

```text
dj1/
│
├── blog/
├── users/
├── payments/
└── products/
```

One project can contain multiple apps.

---

## 16. Blog App Structure

After creating the `blog` app:

```text
blog/
│
├── migrations/
│   └── __init__.py
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

For this chapter, our main focus is:

```text
views.py
```

---

## 17. Register the App

Before continuing, register the `blog` app in:

```text
dj1/settings.py
```

Find:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Add:

```python
'blog',
```

So it becomes:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
]
```

Now Django knows that the `blog` app is part of the project.

---

## 18. Registering Using `AppConfig`

The app can also be registered using its configuration class.

Instead of:

```python
'blog',
```

you can use:

```python
'blog.apps.BlogConfig',
```

The configuration class is located in:

```text
blog/apps.py
```

Example:

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
```

For this project, using:

```python
'blog',
```

is sufficient.

---

## 19. Create the First View

Open:

```text
blog/views.py
```

Initially, it may contain only:

```python
from django.shortcuts import render
```

For our first example, import `HttpResponse`:

```python
from django.http import HttpResponse
```

Now create a function called `home`:

```python
def home(request):
    return HttpResponse("Welcome to Home Page")
```

Complete `views.py`:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Home Page")
```

---

## 20. Understanding the View Function

Let's break this down:

```python
def home(request):
```

### `home`

This is the name of our View function.

### `request`

The `request` parameter represents the HTTP request received from the browser.

### `HttpResponse`

The View returns an HTTP response:

```python
return HttpResponse("Welcome to Home Page")
```

So the flow becomes:

```text
Browser
   ↓
Request
   ↓
home(request)
   ↓
HttpResponse
   ↓
Browser
```

---

## 21. What is `HttpResponse`?

`HttpResponse` is used to return an HTTP response directly from a Django View.

Example:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")
```

The browser will display:

```text
Hello, Django!
```

---

## 22. Connecting the View to a URL

Creating a View is not enough.

We need to tell Django:

> When the user visits a particular URL, run this View.

This is done using **URL mapping**.

Open:

```text
dj1/urls.py
```

The default URL configuration contains something similar to:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

---

## Method 1 - Direct URL Mapping to a View

### 23. Import the View

Suppose our app is named:

```text
blog
```

and our View is:

```python
home
```

We can import it into the project's `urls.py`:

```python
from blog import views
```

Now:

```python
from django.contrib import admin
from django.urls import path
from blog import views
```

---

### 24. Create the URL Pattern

Use `path()` to connect the URL to the View:

```python
path('blog/', views.home, name='home')
```

Complete example:

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views.home, name='home'),
]
```

Now the mapping is:

```text
/blog/
   ↓
views.home
   ↓
HttpResponse
```

---

### 25. Understanding `path()`

This line:

```python
path('blog/', views.home, name='home')
```

contains three important parts.

#### 1. URL Path

```python
'blog/'
```

This is the URL that the user enters.

#### 2. View

```python
views.home
```

This tells Django which View should execute.

### 3. Name

```python
name='home'
```

This gives the URL pattern a unique name.

---

## 26. Why Give a URL a Name?

The `name` argument is optional for the URL pattern itself, but named URLs are extremely useful in Django projects.

Example:

```python
path('blog/', views.home, name='home')
```

Now the URL has the name:

```text
home
```

Later, Django's URL reversing system can use this name instead of hard-coding the URL.

For example, in templates:

```django
{% url 'home' %}
```

This becomes especially useful when URLs change.

---

## 27. Run the Development Server

Now run:

```bash
python manage.py runserver
```

On macOS/Linux:

```bash
python3 manage.py runserver
```

Django will start the development server.

Usually:

```text
http://127.0.0.1:8000/
```

---

## 28. Test the Blog URL

The URL pattern is:

```python
path('blog/', views.home, name='home')
```

Therefore, open:

```text
http://127.0.0.1:8000/blog/
```

The browser should display:

```text
Welcome to Home Page
```

---

## 29. Why Does `/` Show Page Not Found?

If you open:

```text
http://127.0.0.1:8000/
```

you may get:

```text
Page not found (404)
```

This happens because our URL configuration currently contains:

```python
path('blog/', views.home, name='home')
```

but does not contain a pattern for:

```text
/
```

Our available paths are:

```text
/admin/
```

and:

```text
/blog/
```

So:

```text
/
   ❌ No matching URL

/admin/
   ✅ Matching URL

/blog/
   ✅ Matching URL
```

---

## 30. Add Another View

We can create another View inside:

```text
blog/views.py
```

Example:

```python
def about(request):
    a = 10 + 50
    return HttpResponse(a)
```

Complete example:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Home Page")


def about(request):
    a = 10 + 50
    return HttpResponse(a)
```

The View performs the calculation:

```python
a = 10 + 50
```

and returns:

```text
60
```

---

## 31. Map the `about` View

Importing the entire `views` module means we can use:

```python
views.about
```

Add another URL pattern:

```python
path('about/', views.about, name='about')
```

Complete example:

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

Now:

```text
/blog/
   ↓
views.home

/about/
   ↓
views.about
```

---

## 32. Test the About Page

Open:

```text
http://127.0.0.1:8000/about/
```

The browser will display:

```text
60
```

because:

```python
a = 10 + 50
```

and:

```python
return HttpResponse(a)
```

returns the result.

---

## 33. URL Path Can Be Empty

We can also map the root URL:

```python
path('', views.home, name='home')
```

Here:

```python
''
```

represents the root URL.

Therefore:

```python
path('', views.home, name='home')
```

maps:

```text
http://127.0.0.1:8000/
```

to:

```python
views.home
```

---

## 34. Root URL Example

The URL configuration can be:

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

Now:

```text
/
   ↓
home()

/about/
   ↓
about()
```

---

## Method 2 - App-Level URL Configuration

## 35. Why Use App-Level URLs?

Directly placing every app's URL inside the main project's `urls.py` can become difficult to manage when a project contains multiple apps.

Imagine:

```text
Project
│
├── blog
├── users
├── products
├── payments
└── orders
```

Each app may contain many URLs.

Instead of putting everything inside:

```text
project/urls.py
```

we can create a separate:

```text
urls.py
```

inside each app.

For example:

```text
blog/
├── views.py
├── models.py
├── urls.py
└── ...
```

This keeps app-related URL patterns inside the app.

---

## 36. Create `urls.py` Inside the Blog App

Inside:

```text
blog/
```

create:

```text
urls.py
```

The structure becomes:

```text
blog/
│
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── urls.py
```

---

## 37. Write URL Patterns Inside `blog/urls.py`

Open:

```text
blog/urls.py
```

Import `path`:

```python
from django.urls import path
```

Import the app's Views:

```python
from . import views
```

Now create `urlpatterns`:

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

Complete `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

---

## 38. Why Use `from . import views`?

The dot:

```python
.
```

means the **current package/app**.

Therefore:

```python
from . import views
```

means:

> Import the `views` module from the current Django app.

So Django looks inside:

```text
blog/views.py
```

---

## 39. Include App URLs in the Main URL Configuration

Now open:

```text
dj1/urls.py
```

Import `include`:

```python
from django.urls import path, include
```

Then include the `blog` app's URL configuration:

```python
path('', include('blog.urls'))
```

Complete example:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

---

## 40. Understanding `include()`

This line:

```python
path('', include('blog.urls'))
```

tells Django:

> For this URL prefix, look inside `blog/urls.py` for the remaining URL patterns.

The flow becomes:

```text
Browser
   ↓
Project urls.py
   ↓
include('blog.urls')
   ↓
blog/urls.py
   ↓
View
   ↓
Response
```

---

## 41. How the URL Mapping Works

Suppose `dj1/urls.py` contains:

```python
path('', include('blog.urls'))
```

and `blog/urls.py` contains:

```python
path('', views.home, name='home')
path('about/', views.about, name='about')
```

Then:

```text
/
   ↓
blog.urls
   ↓
views.home
```

and:

```text
/about/
   ↓
blog.urls
   ↓
views.about
```

---

## 42. Using an App Prefix

We can also give the app a URL prefix.

In the main `urls.py`:

```python
path('blog/', include('blog.urls'))
```

Now suppose `blog/urls.py` contains:

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

The final URLs become:

```text
/blog/
   ↓
views.home
```

and:

```text
/blog/about/
   ↓
views.about
```

This is a very common way of organizing URLs in Django projects.

---

## 43. Recommended Project Structure

For a project with a blog app:

```text
dj1/
│
├── manage.py
│
├── blog/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
└── dj1/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

The responsibility is separated:

```text
dj1/urls.py
     ↓
Project-level URL configuration

blog/urls.py
     ↓
Blog-specific URL configuration

blog/views.py
     ↓
Blog-specific View logic
```

---

## 44. Main `urls.py` vs App `urls.py`

### Project `urls.py`

Responsible for connecting applications.

Example:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

### App `urls.py`

Responsible for URLs related to that app.

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

---

## 45. Why `include()` Is Useful

Suppose the project has:

```text
blog
users
products
payments
```

The project-level URL configuration can remain simple:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('payments/', include('payments.urls')),
]
```

Each app manages its own URLs.

For example:

```text
blog/urls.py
     ↓
Blog URLs

users/urls.py
     ↓
User URLs

products/urls.py
     ↓
Product URLs
```

This makes larger projects easier to organize.

---

## Function-Based Views

## 46. Function-Based View (FBV)

The View we created is a **Function-Based View**.

Example:

```python
def home(request):
    return HttpResponse("Welcome to Home Page")
```

It is simply a Python function that:

1. Receives a request.
2. Performs some logic.
3. Returns a response.

Basic structure:

```python
def view_name(request):
    # Logic
    return response
```

---

## 47. Example of Logic Inside a View

A View can contain application logic.

Example:

```python
def about(request):
    a = 10
    b = 50

    result = a + b

    return HttpResponse(result)
```

The flow is:

```text
Request
   ↓
about(request)
   ↓
a = 10
b = 50
   ↓
result = 60
   ↓
HttpResponse(60)
   ↓
Browser
```

---

## 48. Returning HTML from a View

For basic demonstration purposes, `HttpResponse` can also return HTML.

Example:

```python
def home(request):
    return HttpResponse("<h1>Welcome to Home Page</h1>")
```

The browser will render:

```html
<h1>Welcome to Home Page</h1>
```

However, writing large amounts of HTML directly inside Views is **not a good practice**.

In real Django applications, HTML is normally placed inside **templates**.

For example:

```text
View
  ↓
Template
  ↓
HTML
  ↓
Browser
```

Templates will be covered later.

---

## Three URL Mapping Approaches Mentioned

## 49. Direct Function-Based View Mapping

A function can be imported directly:

```python
from blog.views import home

urlpatterns = [
    path('blog/', home, name='home'),
]
```

Here:

```text
/blog/
   ↓
home()
```

---

## 50. Mapping Through the `views` Module

Instead of importing the function individually:

```python
from blog import views
```

we can write:

```python
urlpatterns = [
    path('blog/', views.home, name='home'),
]
```

This approach is also commonly used.

---

## 51. Including Another URL Configuration

For larger projects, use:

```python
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
]
```

Then the app manages its own URL patterns:

```python
# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

This is the recommended organization for larger applications.

---

## Class-Based Views

## 52. Function-Based vs Class-Based Views

Django supports both:

```text
Function-Based Views
        ↓
      def
```

and:

```text
Class-Based Views
        ↓
      class
```

Example of a Function-Based View:

```python
def home(request):
    return HttpResponse("Home Page")
```

Class-Based Views will be covered separately.

The important point for now is:

```text
View
├── Function-Based View
└── Class-Based View
```

---

## Complete Working Example

## 53. `blog/views.py`

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Home Page")


def about(request):
    a = 10 + 50
    return HttpResponse(a)
```

---

## 54. `blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

---

## 55. `dj1/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

---

## 56. Final URL Flow

When the user visits:

```text
http://127.0.0.1:8000/blog/
```

the flow is:

```text
Browser
   ↓
/blog/
   ↓
dj1/urls.py
   ↓
include('blog.urls')
   ↓
blog/urls.py
   ↓
views.home
   ↓
HttpResponse
   ↓
"Welcome to Home Page"
   ↓
Browser
```

When the user visits:

```text
http://127.0.0.1:8000/blog/about/
```

the flow is:

```text
Browser
   ↓
/blog/about/
   ↓
dj1/urls.py
   ↓
include('blog.urls')
   ↓
blog/urls.py
   ↓
views.about
   ↓
10 + 50
   ↓
60
   ↓
Browser
```

---

## Complete Project Structure

## 57. Final Structure

```text
django-tutorial/
│
├── venv/
│
└── dj1/
    │
    ├── manage.py
    │
    ├── blog/
    │   ├── migrations/
    │   │   └── __init__.py
    │   │
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   └── urls.py
    │
    └── dj1/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
```

---

## Complete Development Process

## 58. Step-by-Step Flow

```text
Create Main Project Folder
        ↓
Create Virtual Environment
        ↓
Activate Virtual Environment
        ↓
Install Django
        ↓
Check Django Version
        ↓
Create Django Project
        ↓
Move Into Directory Containing manage.py
        ↓
Create Blog App
        ↓
Register Blog App
        ↓
Open blog/views.py
        ↓
Create home() View
        ↓
Return HttpResponse
        ↓
Create blog/urls.py
        ↓
Map URL to View
        ↓
Include blog.urls in Project urls.py
        ↓
Run Development Server
        ↓
Open Browser
        ↓
Test /blog/
        ↓
Test /blog/about/
```

---

## Important Commands

## 59. Create Virtual Environment

```bash
python -m venv venv
```

or:

```bash
python3 -m venv venv
```

---

## 60. Activate Virtual Environment

### Windows (venv)

```bash
venv\Scripts\activate
```

### macOS / Linux (venv)

```bash
source venv/bin/activate
```

---

## 61. Install Django

```bash
pip install django
```

or:

```bash
pip3 install django
```

---

## 62. Check Django Version

```bash
django-admin --version
```

---

## 63. Create Django Project

```bash
django-admin startproject dj1
```

---

## 64. Create Django App

```bash
python manage.py startapp blog
```

or:

```bash
python3 manage.py startapp blog
```

---

## 65. Run Development Server

```bash
python manage.py runserver
```

or:

```bash
python3 manage.py runserver
```

---

## 66. Stop Development Server

```text
CTRL + C
```

---

## Quick Revision

## 67. Views and URLs

| Concept | Meaning |
| --- | --- |
| View | Handles a request and returns a response |
| Function-Based View | View written using a Python function |
| Class-Based View | View written using a Python class |
| URL Configuration | Maps URL paths to Views |
| `path()` | Defines a URL pattern |
| `include()` | Includes another URL configuration |
| `HttpResponse` | Returns an HTTP response |
| `request` | Contains information about the incoming HTTP request |
| `urlpatterns` | List containing URL patterns |
| `name` | Gives a URL pattern a name |

---

## 68. Important Files

| File | Responsibility |
| --- | --- |
| `manage.py` | Runs Django management commands |
| `settings.py` | Project configuration |
| `project/urls.py` | Main/project-level URL configuration |
| `app/views.py` | Application View logic |
| `app/urls.py` | Application-level URL configuration |
| `app/models.py` | Database models |
| `app/admin.py` | Admin configuration |

---

## Important Syntax

## 69. Basic Function-Based View

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Django")
```

---

## 70. Direct URL Mapping

```python
from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.home, name='home'),
]
```

---

## 71. App-Level URL Configuration

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

---

## 72. Include App URLs

```python
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
]
```

---

## Key Takeaways

- Django follows the **MVT architecture**.
- The **View** is responsible for processing requests and returning responses.
- A View can be implemented as a **function or class**.
- A Function-Based View is created using a Python function.
- A View receives an HTTP `request`.
- A View can return an `HttpResponse`.
- URL configuration maps a URL path to a View.
- `path()` is used to define URL patterns.
- `name` can be used to give a URL pattern a unique name.
- `include()` allows an app's URL configuration to be connected to the main project URL configuration.
- Large Django projects should keep app-specific URLs inside the corresponding app.
- `blog/views.py` contains blog View logic.
- `blog/urls.py` contains blog URL patterns.
- `project/urls.py` can include the app's URL configuration.
- HTML can technically be returned using `HttpResponse`, but real projects generally use **templates** for HTML.
- One Django project can contain multiple apps, and each app can maintain its own URLs.
- A separate virtual environment is useful for keeping project dependencies isolated.

---

## Most Important Flow to Remember

```text
USER
  ↓
Browser URL
  ↓
Project urls.py
  ↓
include()
  ↓
App urls.py
  ↓
View
  ↓
Business Logic
  ↓
Response
  ↓
Browser
```

For a simple example:

```text
http://127.0.0.1:8000/blog/
                ↓
        dj1/urls.py
                ↓
     include('blog.urls')
                ↓
        blog/urls.py
                ↓
          views.home
                ↓
      HttpResponse(...)
                ↓
            Browser
```
