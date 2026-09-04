# Chapter 05 - Understanding Django Project Structure

In this chapter, we will understand the **Django project folder structure** in detail. We will learn the purpose of the outer project folder, inner project folder, `manage.py`, `settings.py`, `urls.py`, `asgi.py`, `wsgi.py`, and other important files and folders.

---

## 1. Creating a Django Project

A Django project can be created using the `startproject` command.

```bash
django-admin startproject myproject
```

After running the command, Django creates the basic project structure.

---

## 2. Basic Django Project Structure

The initial Django project structure looks like this:

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

There are two folders with the same name:

```text
myproject/
│
├── manage.py
│
└── myproject/
```

Although they have the same name, they have different purposes.

- The **outer `myproject` folder** is the project root or container.
- The **inner `myproject` folder** contains the actual Django project configuration.

---

## 3. Outer Project Folder

The outer project folder is the **root directory or container** of the Django project.

For example:

```text
myproject/
```

It contains:

```text
myproject/
│
├── manage.py
│
└── myproject/
```

As the project grows, additional Django applications, templates, static files, and other project-related files can be organized inside the project directory.

A typical project may later look like:

```text
myproject/
│
├── manage.py
│
├── app1/
├── app2/
├── templates/
├── static/
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 4. `manage.py`

`manage.py` is a Django command-line utility used to perform various project management tasks.

It allows us to execute Django commands from the terminal.

Some common commands are:

```bash
python manage.py runserver
```

```bash
python manage.py startapp app_name
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

The general structure is:

```bash
python manage.py <command>
```

For example:

```bash
python manage.py runserver
```

Here:

- `python` → Runs the Python interpreter.
- `manage.py` → Django project management utility.
- `runserver` → Django command used to start the development server.

On macOS/Linux, you may use:

```bash
python3 manage.py runserver
```

---

## 5. Inner Project Folder

The inner project folder contains the **actual Django project configuration**.

Example:

```text
myproject/
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

This folder is a Python package and contains the main configuration files required by Django.

---

## 6. `__init__.py`

The `__init__.py` file indicates that the directory is a Python package.

Example:

```text
myproject/
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

In a newly created Django project, the file is normally empty.

Example:

```python
# __init__.py
```

You generally do not need to add anything to this file when creating a basic Django project.

---

## 7. `settings.py`

The `settings.py` file contains the main **configuration and settings** of the Django project.

Example:

```text
myproject/
│
└── myproject/
    └── settings.py
```

Important configurations inside `settings.py` include:

- Installed applications.
- Middleware.
- Database configuration.
- Templates.
- Static files.
- Time zone.
- Language.
- Security settings.
- Other Django project configurations.

For example:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

Database configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

Time zone:

```python
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"
```

The `settings.py` file acts as the central configuration file of the Django project.

---

## 8. `INSTALLED_APPS`

`INSTALLED_APPS` is defined inside `settings.py`.

It contains the Django applications that are enabled in the project.

Example:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

When we create our own Django application, it can later be added to `INSTALLED_APPS`.

Example:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "blog",
]
```

---

## 9. Middleware

Middleware is also configured inside `settings.py`.

Example:

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

Middleware can handle things such as:

- Security.
- Sessions.
- Authentication.
- CSRF protection.
- Messages.
- Common HTTP processing.

Middleware will be studied in more detail in later chapters.

---

## 10. Database Configuration

The database configuration is defined inside `settings.py`.

A default Django project commonly uses SQLite:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

Other databases such as PostgreSQL, MySQL, and Oracle can also be configured.

---

## 11. Templates Configuration

Templates are also configured through `settings.py`.

Example:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

Later, the `DIRS` option can be used to specify a project-level templates directory.

Example:

```python
"DIRS": [BASE_DIR / "templates"],
```

---

## 12. Language and Time Zone

Language and time zone settings are also defined in `settings.py`.

Example:

```python
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
```

These settings control language, internationalization, and time zone behavior.

---

## 13. `urls.py`

The `urls.py` file is responsible for **URL routing**.

Example:

```text
myproject/
│
└── myproject/
    └── urls.py
```

A newly created Django project normally contains an admin URL:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```

The URL:

```text
/admin/
```

is mapped to Django's admin site.

---

## 14. URL Mapping

URL patterns connect URLs to views.

For example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
]
```

This means:

```text
/home/
```

is connected to:

```python
views.home
```

The basic concept is:

```text
URL
 ↓
URL Pattern
 ↓
View
 ↓
Response
```

URL routing will be covered in detail in later chapters.

---

## 15. `asgi.py`

`asgi.py` stands for:

```text
ASGI
↓
Asynchronous Server Gateway Interface
```

It provides an entry point for running a Django project with an ASGI-compatible server.

A typical `asgi.py` file looks like:

```python
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "myproject.settings"
)

application = get_asgi_application()
```

ASGI is designed to support asynchronous web applications and modern asynchronous communication.

It can be used with ASGI-compatible deployment servers.

---

## 16. `wsgi.py`

`wsgi.py` stands for:

```text
WSGI
↓
Web Server Gateway Interface
```

It provides an entry point for running a Django project with a WSGI-compatible server.

A typical `wsgi.py` file looks like:

```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "myproject.settings"
)

application = get_wsgi_application()
```

WSGI is commonly used for traditional synchronous Django applications.

---

## 17. ASGI vs WSGI

The basic difference can be remembered as:

```text
ASGI
↓
Asynchronous
↓
Supports asynchronous applications

WSGI
↓
Synchronous
↓
Traditional synchronous web applications
```

Both provide an entry point between Django and a compatible application server.

```text
Client
   ↓
Web Server
   ↓
ASGI / WSGI
   ↓
Django
   ↓
Application
```

The detailed deployment process will be covered later.

---

## 18. `__pycache__` Folder

When Python files are executed, Python may create a `__pycache__` directory.

Example:

```text
myproject/
│
├── __pycache__/
│
├── manage.py
│
└── myproject/
    ├── __pycache__/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

The `__pycache__` directory contains Python bytecode cache files.

Example:

```text
__pycache__/
    settings.cpython-xxx.pyc
    urls.cpython-xxx.pyc
```

These files are generated for Python's internal use.

They are not the main source-code files of the Django project.

They are normally excluded from Git repositories using `.gitignore`.

---

## 19. `db.sqlite3`

When SQLite is configured as the default database, Django uses a file named:

```text
db.sqlite3
```

Example:

```text
myproject/
│
├── db.sqlite3
├── manage.py
└── myproject/
```

The SQLite database file is normally created after running database migrations:

```bash
python manage.py migrate
```

The database stores application data such as:

- Users.
- Sessions.
- Authentication data.
- Django admin data.
- Application data created through models.

The database configuration is controlled from:

```text
settings.py
```

For a new project, `db.sqlite3` may not exist until migrations are run.

---

## 20. Running the Django Project

To start the Django development server, first move into the directory containing `manage.py`.

```bash
cd myproject
```

Then run:

### Windows

```bash
python manage.py runserver
```

### macOS/Linux

```bash
python3 manage.py runserver
```

Django will start its development server.

---

## 21. Default Development Server Address

By default, Django usually starts the development server on:

```text
http://127.0.0.1:8000/
```

You can open this address in your browser.

Another equivalent local address is:

```text
http://localhost:8000/
```

The development server is intended for local development and testing.

It should not be treated as a production deployment server.

---

## 22. Change the Development Server Port

Django normally uses port:

```text
8000
```

You can specify another port.

For example:

```bash
python manage.py runserver 8080
```

The server will then run at:

```text
http://127.0.0.1:8080/
```

Another example:

```bash
python manage.py runserver 9000
```

The server will run at:

```text
http://127.0.0.1:9000/
```

The general syntax is:

```bash
python manage.py runserver <port>
```

---

## 23. Stop the Development Server

To stop the Django development server, press:

```text
CTRL + C
```

This stops the server running in the terminal.

---

## 24. Run Django on the Local Network

Django's development server can also be configured to listen on a network interface so that other devices on the same network can access it.

Use:

```bash
python manage.py runserver 0.0.0.0:8000
```

For another port:

```bash
python manage.py runserver 0.0.0.0:8080
```

Here:

```text
0.0.0.0
```

means Django listens on available network interfaces.

Other devices connected to the same network can access the server using the computer's local IP address.

For example:

```text
http://192.168.1.10:8000/
```

The exact IP address depends on the local network.

---

## 25. Three Common Ways to Run the Development Server

### Method 1 - Default Port

```bash
python manage.py runserver
```

Address:

```text
http://127.0.0.1:8000/
```

### Method 2 - Custom Port

```bash
python manage.py runserver 8080
```

Address:

```text
http://127.0.0.1:8080/
```

### Method 3 - Local Network

```bash
python manage.py runserver 0.0.0.0:8000
```

Other devices on the same network can access it using:

```text
http://<your-local-ip>:8000/
```

Example:

```text
http://192.168.1.10:8000/
```

---

## 26. Complete Project Structure

After running the project and creating additional files, the structure may look like:

```text
myproject/
│
├── manage.py
│
├── db.sqlite3
│
├── __pycache__/
│
└── myproject/
    │
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    ├── wsgi.py
    │
    └── __pycache__/
```

Later, after creating Django applications, the structure can grow:

```text
myproject/
│
├── manage.py
├── db.sqlite3
│
├── app1/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── templates/
│
├── static/
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

The Django application structure will be covered in the next chapter.

---

## 27. Project Structure Overview

```text
Django Project
│
├── Outer Project Folder
│   │
│   ├── manage.py
│   ├── Django Apps
│   ├── Templates
│   ├── Static Files
│   └── Database
│
└── Inner Project Folder
    │
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 28. Important Files and Their Responsibilities

| File/Folder | Purpose |
|-------------|---------|
| `manage.py` | Runs Django management commands |
| `__init__.py` | Makes the directory a Python package |
| `settings.py` | Contains project configuration |
| `urls.py` | Defines URL routing |
| `asgi.py` | ASGI application entry point |
| `wsgi.py` | WSGI application entry point |
| `__pycache__/` | Contains Python bytecode cache |
| `db.sqlite3` | SQLite database file |

---

## 29. Important Commands

### Create a Django Project

```bash
django-admin startproject myproject
```

### Enter the Project Directory

```bash
cd myproject
```

### Start the Development Server

```bash
python manage.py runserver
```

### Start the Development Server on macOS/Linux

```bash
python3 manage.py runserver
```

### Start the Server on Port 8080

```bash
python manage.py runserver 8080
```

### Start the Server for Local Network Access

```bash
python manage.py runserver 0.0.0.0:8000
```

### Run Database Migrations

```bash
python manage.py migrate
```

### Create a Django Application

```bash
python manage.py startapp app_name
```

### Stop the Server

```text
CTRL + C
```

---

## 30. Django Project Startup Flow

```text
django-admin startproject myproject
                ↓
       Django Project Created
                ↓
       Outer Project Folder
                ↓
       Inner Project Folder
                ↓
         Project Configuration
                ↓
         python manage.py runserver
                ↓
       Django Development Server
                ↓
        http://127.0.0.1:8000/
                ↓
          Django Application
```

---

## 31. Important Concepts to Remember

```text
Outer Folder
    ↓
Project Container / Root Directory

Inner Folder
    ↓
Actual Django Project Configuration

manage.py
    ↓
Runs Django Management Commands

settings.py
    ↓
Project Configuration

urls.py
    ↓
URL Routing

asgi.py
    ↓
ASGI Entry Point

wsgi.py
    ↓
WSGI Entry Point

__init__.py
    ↓
Python Package File

__pycache__
    ↓
Python Bytecode Cache

db.sqlite3
    ↓
SQLite Database File
```

---

## 32. Key Takeaways

- The outer project folder acts as the **root/container** of the Django project.
- The inner project folder contains the **actual Django project configuration**.
- `manage.py` is used to execute Django management commands.
- `settings.py` contains the main project configuration.
- `urls.py` is responsible for URL routing.
- `asgi.py` provides an ASGI application entry point.
- `wsgi.py` provides a WSGI application entry point.
- `__init__.py` identifies the directory as a Python package.
- `__pycache__` contains Python bytecode cache files.
- `db.sqlite3` is the default SQLite database file when SQLite is configured.
- `db.sqlite3` is normally created after running migrations.
- `python manage.py runserver` starts the Django development server.
- Django normally uses port `8000` for the development server.
- A custom port can be specified using `runserver <port>`.
- `0.0.0.0` can be used to make the development server accessible on the local network.
- The Django development server is intended for development and testing, not production deployment.

---

## 33. Quick Revision

```text
Django Project
│
├── Outer Folder
│   └── Project Container
│
├── manage.py
│   └── Django Command-Line Utility
│
└── Inner Folder
    │
    ├── __init__.py
    │   └── Python Package
    │
    ├── settings.py
    │   └── Project Configuration
    │
    ├── urls.py
    │   └── URL Routing
    │
    ├── asgi.py
    │   └── ASGI Entry Point
    │
    └── wsgi.py
        └── WSGI Entry Point
```

---

## What's Next?

In the next chapter, we will create our **first Django application** using the `startapp` command and understand the folder structure and files created inside a Django app.
