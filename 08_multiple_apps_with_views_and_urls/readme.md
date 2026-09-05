# Chapter 08 - Working with Multiple Applications, Views & URL Mapping

In this chapter, we learn how to work with **multiple Django applications** inside a single project.

The main focus is on:

- Creating a Django project
- Creating multiple applications
- Registering applications in `INSTALLED_APPS`
- Creating views inside different applications
- Creating separate `urls.py` files for each application
- Connecting application URLs with the main project
- Using `include()` for modular URL configuration
- Understanding how multiple applications work together

---

## 1. What We Have Learned So Far

Before this chapter, we learned:

1. How to create a Django project
2. How to create a Django application
3. How to create views
4. How to map URLs with views

Now we will learn how to work with **multiple applications inside one Django project**.

For example, a real-world project may contain:

```text
Project
│
├── Blog App
├── Shop App
├── Authentication App
├── Payment App
└── User App
```

Each application handles a specific feature.

---

## 2. What is the Modular Concept?

Django allows us to divide a large project into multiple smaller applications.

For example:

```text
my_project/
│
├── blog/
├── shop/
├── users/
└── payments/
```

Each application can contain its own:

- Views
- URLs
- Models
- Templates
- Forms
- Tests

This makes the project:

- Organized
- Maintainable
- Reusable
- Easier to debug
- Easier to scale

---

## 3. Project vs Application

It is important to understand the difference.

### Project

The **project** is the complete Django website/application.

Example:

```text
my_project
```

### Application

An **app** handles a particular feature of the project.

Example:

```text
blog
shop
```

So one project can contain multiple apps:

```text
my_project
│
├── blog
└── shop
```

---

## 4. Creating a New Django Project

First, go to your working directory.

For example:

```text
django-tutorial/
```

Create a new Django project:

```bash
django-admin startproject my_project1
```

This creates:

```text
my_project1/
```

The project structure will look approximately like:

```text
my_project1/
│
├── manage.py
│
└── my_project1/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 5. Virtual Environment

For real-world projects, it is recommended to use a **virtual environment**.

Different projects may require different package versions.

For example:

```text
Project 1 → Django 5.x
Project 2 → Django 4.x
Project 3 → Django 6.x
```

A virtual environment keeps project dependencies isolated.

### Create a Virtual Environment

Using Python's built-in `venv`:

```bash
python -m venv venv
```

or:

```bash
python3 -m venv venv
```

---

## 6. Alternative: Using `virtualenv`

Another way is to use the `virtualenv` package.

Install it:

```bash
pip install virtualenv
```

Create the environment:

```bash
virtualenv venv
```

Both approaches create an isolated Python environment.

---

## 7. Activating the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, you will usually see something similar to:

```text
(venv)
```

at the beginning of your terminal.

---

## 8. Installing Django

If Django is not already installed inside the virtual environment:

```bash
pip install django
```

or:

```bash
pip3 install django
```

Check the Django version:

```bash
django-admin --version
```

You can also use:

```bash
python -m django --version
```

---

## 9. Creating Multiple Applications

Our project will contain two applications:

```text
blog
shop
```

Make sure you are in the directory containing `manage.py`.

Create the first app:

```bash
python manage.py startapp blog
```

Create the second app:

```bash
python manage.py startapp shop
```

On systems where `python3` is required:

```bash
python3 manage.py startapp blog
python3 manage.py startapp shop
```

Now the project will look like:

```text
my_project1/
│
├── manage.py
│
├── my_project1/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── blog/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
└── shop/
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

---

## 10. Registering Applications in `INSTALLED_APPS`

After creating the applications, register them in:

```text
my_project1/settings.py
```

Find:

```python
INSTALLED_APPS = [
    ...
]
```

Add:

```python
INSTALLED_APPS = [
    ...
    "blog",
    "shop",
]
```

Now Django knows that these applications are part of the project.

### Why Register Apps?

Registration becomes especially important when working with:

- Models
- Migrations
- Templates
- Static files
- Admin
- App configuration

For best practice, register your apps from the beginning.

---

## 11. Creating Views in the `blog` App

Open:

```text
blog/views.py
```

Import `HttpResponse`:

```python
from django.http import HttpResponse
```

Create a home view:

```python
def home(request):
    return HttpResponse("Blog Home Page")
```

Create another view:

```python
def about(request):
    return HttpResponse("Blog About Page")
```

So `blog/views.py` becomes:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Blog Home Page")


def about(request):
    return HttpResponse("Blog About Page")
```

---

## 12. Creating Views in the `shop` App

Now open:

```text
shop/views.py
```

Add:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Shop Home Page")


def product(request):
    return HttpResponse("Shop Products Page")
```

Now we have:

### Blog

```text
blog/views.py
```

```python
home()
about()
```

### Shop

```text
shop/views.py
```

```python
home()
product()
```

Notice that both applications can have a function named `home()`.

This is completely fine because they belong to different Python modules.

---

## 13. Why Should Each App Have Its Own `urls.py`?

By default, a newly created Django app does not contain a `urls.py`.

We can create it manually.

Create:

```text
blog/urls.py
```

and:

```text
shop/urls.py
```

This allows each application to manage its own URL patterns.

Instead of putting every URL inside the project's main `urls.py`, we can divide them according to applications.

---

## 14. Creating `blog/urls.py`

Open:

```text
blog/urls.py
```

Add:

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]
```

### Explanation

```python
from django.urls import path
```

Imports Django's `path()` function.

```python
from . import views
```

Imports the `views.py` file from the current application.

The `.` means:

```text
current package/application
```

---

## 15. Blog URL Patterns

We created two URL patterns:

```python
path("", views.home, name="blog-home")
```

and:

```python
path("about/", views.about, name="blog-about")
```

So the structure is:

```text
blog/
│
├── views.py
└── urls.py
```

`urls.py` connects URLs to functions inside `views.py`.

---

## 16. Creating `shop/urls.py`

Open:

```text
shop/urls.py
```

Add:

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="shop-home"),
    path("products/", views.product, name="shop-products"),
]
```

Now the Shop app has its own URL configuration.

---

## 17. Connecting App URLs to the Main Project

Now open:

```text
my_project1/urls.py
```

Import:

```python
from django.urls import path, include
```

The important function here is:

```python
include()
```

`include()` allows us to include another URL configuration.

---

## 18. Main Project `urls.py`

The main project URL configuration can look like:

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
]
```

Now the main project delegates URLs to individual applications.

---

## 19. How `include()` Works

This is one of the most important concepts in this chapter.

Suppose we write:

```python
path("blog/", include("blog.urls"))
```

Django receives a URL beginning with:

```text
/blog/
```

and then checks:

```text
blog/urls.py
```

Similarly:

```python
path("shop/", include("shop.urls"))
```

means URLs beginning with:

```text
/shop/
```

are handled by:

```text
shop/urls.py
```

---

## 20. Complete URL Flow

The complete flow is:

```text
Browser
   ↓
Main Project urls.py
   ↓
include("blog.urls")
   ↓
blog/urls.py
   ↓
views.home()
   ↓
HttpResponse
   ↓
Browser
```

For Shop:

```text
Browser
   ↓
Main Project urls.py
   ↓
include("shop.urls")
   ↓
shop/urls.py
   ↓
views.product()
   ↓
HttpResponse
   ↓
Browser
```

---

## 21. Understanding URL Prefixes

Suppose the main project contains:

```python
path("blog/", include("blog.urls"))
```

and `blog/urls.py` contains:

```python
path("", views.home, name="blog-home")
```

The final URL becomes:

```text
/blog/
```

If `blog/urls.py` contains:

```python
path("about/", views.about, name="blog-about")
```

the final URL becomes:

```text
/blog/about/
```

Similarly, if the main project contains:

```python
path("shop/", include("shop.urls"))
```

and `shop/urls.py` contains:

```python
path("", views.home, name="shop-home")
```

the final URL is:

```text
/shop/
```

And:

```python
path("products/", views.product, name="shop-products")
```

becomes:

```text
/shop/products/
```

---

## 22. URL Mapping Table

| Application | App URL Pattern | Final URL | View |
| --- | --- | --- | --- |
| Blog | `""` | `/blog/` | `blog.views.home` |
| Blog | `"about/"` | `/blog/about/` | `blog.views.about` |
| Shop | `""` | `/shop/` | `shop.views.home` |
| Shop | `"products/"` | `/shop/products/` | `shop.views.product` |

---

## 23. Why `include()` is Preferred for Multiple Apps

Imagine a project has:

```text
blog
shop
users
payments
orders
```

Without `include()`, the main `urls.py` could become very large:

```python
urlpatterns = [
    ...
    # Blog URLs
    # Shop URLs
    # User URLs
    # Payment URLs
    # Order URLs
]
```

Instead, we can keep URLs separated:

```text
blog/urls.py
shop/urls.py
users/urls.py
payments/urls.py
orders/urls.py
```

Then the main project only needs:

```python
urlpatterns = [
    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
    path("users/", include("users.urls")),
    path("payments/", include("payments.urls")),
    path("orders/", include("orders.urls")),
]
```

This makes the project much more modular.

---

## 24. URL Names Should Be Unique

Inside the URL configuration, we can give names:

```python
path("", views.home, name="blog-home")
```

For Shop:

```python
path("", views.home, name="shop-home")
```

Both views are named `home`, but their URL names are different:

```text
blog-home
shop-home
```

Using clear and unique names is a good practice, especially in larger projects.

---

## 25. Testing the Project

Run the development server:

```bash
python manage.py runserver
```

or:

```bash
python3 manage.py runserver
```

Django will normally start at:

```text
http://127.0.0.1:8000/
```

---

## 26. Test the Blog App

### Blog Home

Open:

```text
http://127.0.0.1:8000/blog/
```

Output:

```text
Blog Home Page
```

### Blog About

Open:

```text
http://127.0.0.1:8000/blog/about/
```

Output:

```text
Blog About Page
```

---

## 27. Test the Shop App

### Shop Home

Open:

```text
http://127.0.0.1:8000/shop/
```

Output:

```text
Shop Home Page
```

### Shop Products

Open:

```text
http://127.0.0.1:8000/shop/products/
```

Output:

```text
Shop Products Page
```

---

## 28. Complete Project Structure

After completing this chapter:

```text
my_project1/
│
├── manage.py
│
├── my_project1/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── blog/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── shop/
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

---

## 29. Complete Code

### `blog/views.py`

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Blog Home Page")


def about(request):
    return HttpResponse("Blog About Page")
```

### `blog/urls.py`

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]
```

---

### `shop/views.py`

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("Shop Home Page")


def product(request):
    return HttpResponse("Shop Products Page")
```

### `shop/urls.py`

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="shop-home"),
    path("products/", views.product, name="shop-products"),
]
```

---

### `my_project1/urls.py`

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
]
```

---

### `my_project1/settings.py`

```python
INSTALLED_APPS = [
    ...
    "blog",
    "shop",
]
```

---

## 30. Functional View vs `include()` Approach

There are different ways to connect URLs and views.

### Direct View Mapping

For example:

```python
from blog import views

urlpatterns = [
    path("blog/", views.home, name="blog-home"),
]
```

This directly maps a project URL to a view.

### Using `include()`

A more modular approach is:

```python
from django.urls import path, include

urlpatterns = [
    path("blog/", include("blog.urls")),
]
```

Then the Blog app manages its own URLs:

```python
# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]
```

For projects with multiple applications, `include()` keeps URL configuration organized.

---

## 31. Important Concept: URL Configuration Belongs to Different Levels

There are two levels of URL configuration.

### Project-Level URL Configuration

Located at:

```text
my_project1/urls.py
```

Responsible for connecting application URL configurations.

Example:

```python
path("blog/", include("blog.urls"))
```

### Application-Level URL Configuration

Located at:

```text
blog/urls.py
```

Responsible for connecting URLs to views inside that application.

Example:

```python
path("about/", views.about, name="blog-about")
```

---

## 32. Real-World Architecture

A real-world Django project can look like:

```text
project/
│
├── project/
│   ├── settings.py
│   └── urls.py
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
└── payments/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── ...
```

The main project URL configuration remains simple:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
    path("users/", include("users.urls")),
    path("payments/", include("payments.urls")),
]
```

This is the basic idea behind **modular Django applications**.

---

## 33. Complete Process / Flow

The complete process can be remembered as:

```text
1. Create Django Project
        ↓
2. Create Multiple Apps
        ↓
3. Register Apps in INSTALLED_APPS
        ↓
4. Create Views in Each App
        ↓
5. Create urls.py in Each App
        ↓
6. Map App URLs → Views
        ↓
7. Use include() in Project urls.py
        ↓
8. Run Development Server
        ↓
9. Test URLs in Browser
```

---

## 34. Important Commands

### Create Project

```bash
django-admin startproject my_project1
```

### Create App

```bash
python manage.py startapp blog
```

```bash
python manage.py startapp shop
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate on Windows

```bash
venv\Scripts\activate
```

### Activate on macOS/Linux

```bash
source venv/bin/activate
```

### Install Django

```bash
pip install django
```

### Check Django Version

```bash
django-admin --version
```

### Run Server

```bash
python manage.py runserver
```

---

## 35. Quick Revision

| Concept | Meaning |
| --- | --- |
| Project | Complete Django website/application |
| App | Independent module for a specific feature |
| Multiple Apps | Multiple feature-specific modules in one project |
| `views.py` | Contains request-handling logic |
| `urls.py` | Maps URL paths to views |
| `include()` | Includes another URL configuration |
| `INSTALLED_APPS` | Registers applications with Django |
| `HttpResponse` | Sends a basic HTTP response |
| `path()` | Defines a URL pattern |
| URL Name | Gives a reusable name to a URL pattern |
| Modular Architecture | Dividing project functionality into separate apps |

---

## 36. Key Takeaways

- A Django **project can contain multiple applications**.
- Each application should ideally handle a specific feature.
- Apps can have their own `views.py` and `urls.py`.
- A newly created Django app does not automatically contain `urls.py`; we can create it manually.
- Applications should be registered in `INSTALLED_APPS`.
- `views.py` contains the request-handling logic.
- `urls.py` maps URL paths to views.
- `include()` connects an application's URL configuration with the main project's URL configuration.
- Application-level URL configurations make large projects more organized.
- URL prefixes such as `blog/` and `shop/` help separate application routes.
- URL names should be clear and preferably unique.
- `HttpResponse` can be used for simple responses while learning views.
- In real projects, HTML is generally placed in templates rather than directly inside `HttpResponse`.
- Modular URL configuration becomes increasingly important as the number of applications grows.

---

## 37. Chapter Summary

In this chapter, we moved from a simple Django application to a **multi-application Django project**.

We created:

```text
my_project1
│
├── blog
└── shop
```

We then:

```text
Project
   ↓
Multiple Apps
   ↓
Views
   ↓
App-level URLs
   ↓
include()
   ↓
Main Project URLs
   ↓
Browser
```

The most important concept from this chapter is:

```python
path("blog/", include("blog.urls"))
```

and:

```python
path("shop/", include("shop.urls"))
```

This allows each Django application to manage its own URL configuration while the main project connects everything together.

---
