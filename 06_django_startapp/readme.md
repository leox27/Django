# Chapter 06 - Creating and Registering the First Django App

In this chapter, we will create our **first Django app**, understand the difference between a Django project and an app, understand the app folder structure, register the app inside the Django project, and test the complete setup.

---

## 1. What is a Django App?

A Django **app** is a small, independent module of a Django project that handles a specific feature or functionality.

For example, a website can have separate apps for different features:

- Blog
- User Authentication
- Payment System
- Products
- Orders
- Notifications

A single Django project can contain **multiple apps**.

Example:

```text
Django Project
│
├── Blog App
├── Authentication App
├── Payment App
└── Notification App
```

Each app can contain its own:

- Models
- Views
- Tests
- Admin configuration
- App configuration
- Database migrations

---

## 2. Project vs App

It is important to understand the difference between a **Django project** and a **Django app**.

### Django Project

A Django project is the complete website or application.

It contains the overall configuration and can contain multiple apps.

### Django App

A Django app is a component of the project that handles a particular functionality.

Example:

```text
E-Commerce Project
│
├── users
├── products
├── orders
├── payments
└── reviews
```

Here:

- `E-Commerce Project` → Django project
- `users` → Django app
- `products` → Django app
- `orders` → Django app
- `payments` → Django app
- `reviews` → Django app

A simple way to remember:

```text
Project = Complete Website / Application

App = Specific Feature / Functionality
```

---

## 3. One Project Can Have Multiple Apps

A single Django project can contain multiple applications.

For example:

```text
myproject/
│
├── manage.py
│
├── blog/
│
├── users/
│
├── payments/
│
└── products/
```

Here:

```text
myproject
    ↓
Django Project

blog
    ↓
Blog App

users
    ↓
User Authentication App

payments
    ↓
Payment App

products
    ↓
Product App
```

Multiple apps can work together inside the same Django project.

Apps can also be reused in different Django projects when designed appropriately.

---

## 4. Move Into the Django Project Directory

Before creating an app, move into the **outer project directory**.

Suppose the project was created using:

```bash
django-admin startproject myproject
```

The structure initially looks like:

```text
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

The `manage.py` file is located in the outer `myproject` directory.

Move into the outer project directory:

```bash
cd myproject
```

Now the terminal should be inside the directory containing:

```text
manage.py
```

---

## 5. Create a Django App

Django provides the `startapp` command to create a new application.

The basic syntax is:

```bash
python manage.py startapp app_name
```

For example, to create a blog app:

```bash
python manage.py startapp blog
```

On systems where `python3` is used:

```bash
python3 manage.py startapp blog
```

Here:

- `python` / `python3` → Runs the Python interpreter.
- `manage.py` → Django project's command-line utility.
- `startapp` → Command used to create a Django app.
- `blog` → Name of the app.

---

## 6. Where Should the App Be Created?

The app should normally be created in the **outer project directory**, alongside `manage.py`.

Before creating the app:

```text
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Run:

```bash
python manage.py startapp blog
```

After creating the app:

```text
myproject/
│
├── manage.py
│
├── blog/
│
└── myproject/
```

The `blog` directory is now our Django app.

---

## 7. Django App Folder Structure

A newly created Django app normally contains:

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

Each file and folder has a specific purpose.

---

## 8. `migrations/` Folder

The `migrations` folder contains Django migration files.

Migrations are used to manage changes to the database schema based on changes made to Django models.

Initially, it contains:

```text
migrations/
└── __init__.py
```

After creating models and generating migrations, additional files can appear.

Example:

```text
migrations/
├── __init__.py
└── 0001_initial.py
```

Migrations can be created using:

```bash
python manage.py makemigrations
```

Migrations can be applied to the database using:

```bash
python manage.py migrate
```

The detailed migration system will be covered in later chapters.

---

## 9. `migrations/__init__.py`

The `__init__.py` file inside the `migrations` folder allows the directory to be treated as a Python package.

Structure:

```text
migrations/
└── __init__.py
```

The file is normally empty when the app is created.

---

## 10. `__init__.py`

The `__init__.py` file is located directly inside the Django app.

Example:

```text
blog/
└── __init__.py
```

It allows the app directory to be treated as a Python package.

The file is normally empty when the app is first created.

---

## 11. `admin.py`

The `admin.py` file is used for configuring the Django admin panel.

Models can be registered here so they can be managed through Django's built-in admin interface.

Example:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

The detailed Django admin system will be covered in later chapters.

---

## 12. `apps.py`

The `apps.py` file contains the configuration of the Django app.

A newly created app normally contains:

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
```

The `AppConfig` class contains configuration information about the application.

For example:

```python
name = 'blog'
```

indicates the name of the application.

---

## 13. `models.py`

The `models.py` file is used to define the database models of the application.

A Django model generally represents a database table.

Example:

```python
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

The model can later be converted into a database table using Django migrations.

Basic process:

```text
Create Model
    ↓
makemigrations
    ↓
Migration File
    ↓
migrate
    ↓
Database Table
```

Models and databases will be covered in detail in later chapters.

---

## 14. `tests.py`

The `tests.py` file is used for writing tests for the Django application.

Tests help verify that different parts of the application work correctly.

Example:

```python
from django.test import TestCase


class BlogTest(TestCase):

    def test_example(self):
        self.assertEqual(1, 1)
```

Testing allows developers to automatically verify application behavior.

Detailed Django testing will be covered later.

---

## 15. `views.py`

The `views.py` file contains the views of the Django application.

A view contains the logic that processes a request and returns a response.

Example:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")
```

A view can later be connected to a URL.

Basic flow:

```text
Browser Request
       ↓
URL
       ↓
View
       ↓
Response
       ↓
Browser
```

URL mapping and views will be covered in the next chapter.

---

## 16. Register the App in the Django Project

Creating an app is not enough.

The app should be registered in the Django project so that Django knows that the app is part of the project.

The app is registered inside:

```text
myproject/settings.py
```

Specifically, the app is registered inside:

```python
INSTALLED_APPS
```

---

## 17. Find `INSTALLED_APPS`

Open:

```text
myproject/settings.py
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

This list contains the Django applications installed in the project.

---

## 18. Register the `blog` App

Add the `blog` app to `INSTALLED_APPS`.

Example:

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

Now Django knows that the `blog` app is installed in the project.

Save the `settings.py` file after making the change.

---

## 19. Register the App Using `AppConfig`

The app can also be registered using its configuration class.

Instead of:

```python
'blog',
```

you can use:

```python
'blog.apps.BlogConfig',
```

Example:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog.apps.BlogConfig',
]
```

The `BlogConfig` class is defined inside:

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

---

## 20. Complete Project Structure After Creating the App

After creating the `blog` app, the complete structure looks like:

```text
myproject/
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
│   └── views.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

The relationship can be remembered as:

```text
myproject/
│
├── manage.py
│
├── blog/
│   └── Django App
│
└── myproject/
    └── Project Configuration
```

---

## 21. Test the Django Setup

After creating and registering the app, test whether the project is working correctly.

Run:

```bash
python manage.py runserver
```

On macOS/Linux:

```bash
python3 manage.py runserver
```

If there are no errors, Django will start the development server.

A typical address is:

```text
http://127.0.0.1:8000/
```

Open this address in a browser:

```text
http://127.0.0.1:8000/
```

If the Django welcome page appears, the project is running successfully.

---

## 22. What Happens When the App Is Registered?

The overall process is:

```text
Create Django Project
        ↓
Create Django App
        ↓
Add App to INSTALLED_APPS
        ↓
Django Recognizes the App
        ↓
Run Development Server
        ↓
Check for Errors
        ↓
Project Runs Successfully
```

---

## 23. Stop the Development Server

To stop the Django development server, press:

```text
CTRL + C
```

This stops the server running in the terminal.

---

## 24. Important Commands

### Create a Django App

```bash
python manage.py startapp blog
```

### Create a Django App on macOS/Linux

```bash
python3 manage.py startapp blog
```

### Run the Development Server

```bash
python manage.py runserver
```

### Run the Development Server on macOS/Linux

```bash
python3 manage.py runserver
```

### Create Migration Files

```bash
python manage.py makemigrations
```

### Apply Migrations

```bash
python manage.py migrate
```

### Stop the Development Server

```text
CTRL + C
```

---

## 25. App Folder Structure Quick Revision

| File / Folder | Purpose |
|---|---|
| `migrations/` | Stores database migration files |
| `migrations/__init__.py` | Makes the migrations directory a Python package |
| `__init__.py` | Makes the Django app directory a Python package |
| `admin.py` | Configures models for Django admin |
| `apps.py` | Contains the app configuration |
| `models.py` | Defines database models |
| `tests.py` | Contains application tests |
| `views.py` | Contains view logic |

---

## 26. Project and App Relationship

```text
Django Project
│
├── Blog App
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   └── ...
│
├── Users App
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── ...
│
└── Payments App
    ├── models.py
    ├── views.py
    ├── admin.py
    └── ...
```

The project contains the overall configuration, while each app handles a specific feature.

---

## 27. Example: Blog Application

Suppose we are creating a blog website.

Create the blog app:

```bash
python manage.py startapp blog
```

The app structure will be:

```text
blog/
│
├── migrations/
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

Possible responsibilities:

```text
models.py
    ↓
Blog database models

views.py
    ↓
Blog request/response logic

admin.py
    ↓
Blog admin configuration

apps.py
    ↓
Blog app configuration

tests.py
    ↓
Blog application tests

migrations/
    ↓
Blog database schema changes
```

---

## 28. Complete Process

```text
Django Project Already Created
            ↓
Move Into Outer Project Folder
            ↓
Check for manage.py
            ↓
Run startapp Command
            ↓
Create blog App
            ↓
Understand App Folder Structure
            ↓
Open settings.py
            ↓
Find INSTALLED_APPS
            ↓
Register blog App
            ↓
Save settings.py
            ↓
Run Development Server
            ↓
Check for Errors
            ↓
Django Project Runs Successfully
```

---

## 29. Important Concepts to Remember

```text
Project
    ↓
Complete Django Website / Application

App
    ↓
Specific Feature / Functionality

One Project
    ↓
Can contain multiple Apps

startapp
    ↓
Creates a Django App

INSTALLED_APPS
    ↓
Registers the App with the Django Project

models.py
    ↓
Database Models

views.py
    ↓
Request / Response Logic

admin.py
    ↓
Admin Panel Configuration

apps.py
    ↓
App Configuration

migrations/
    ↓
Database Schema Changes

tests.py
    ↓
Application Testing
```

---

## 30. Key Takeaways

- A Django **project** is the complete application.
- A Django **app** is a smaller component responsible for a specific feature.
- One Django project can contain multiple apps.
- A Django app is created using the `startapp` command.
- The app should normally be created alongside `manage.py`.
- `migrations/` stores database migration files.
- `admin.py` is used for Django admin configuration.
- `apps.py` contains the app configuration.
- `models.py` is used to define database models.
- `tests.py` is used for writing tests.
- `views.py` contains view logic.
- The app should be added to `INSTALLED_APPS` in `settings.py`.
- The development server can be used to test the project.
- The server can be started using `runserver`.
- The server can be stopped using `CTRL + C`.

---

## What's Next?

The first Django app has now been created and registered inside the Django project.

In the next chapter, we will create our **first Django view** and perform **URL mapping** so that our app can display a custom response in the browser.