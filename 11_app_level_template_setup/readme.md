# Chapter 11 - Setting Up Templates Inside Django Apps

## 1. Introduction

In the previous chapter, we learned how to create and use a **project-level templates folder**.

In this chapter, we will learn how to create and use **templates inside individual Django apps**.

For example, a Django project can contain multiple apps:

- `blog`
- `shop`
- `accounts`
- `products`

Each app can have its own templates.

### What We Will Learn

- Create a Django project
- Create multiple apps
- Register apps in `INSTALLED_APPS`
- Configure project-level template settings
- Create templates inside an app
- Create `views.py`
- Create app-level `urls.py`
- Connect app URLs with project URLs using `include()`
- Connect views with templates
- Run and test multiple app templates

---

## 2. Project and App Structure

A Django **project** is the main container of the entire website/application.

An **app** is a separate component that handles a particular feature.

For example:

```text
myproject/
├── blog/
├── shop/
└── myproject/
```

Here:

- `myproject` → Main Django project
- `blog` → Blog application
- `shop` → Shop application

A single Django project can contain multiple applications.

---

## 3. Create a Django Project

Create a new Django project using:

```bash
django-admin startproject myproject4
```

Then move inside the project directory:

```bash
cd myproject4
```

The project contains `manage.py`, which is used to execute Django management commands.

---

## 4. Create Multiple Apps

Create the `blog` app:

```bash
python manage.py startapp blog
```

Create the `shop` app:

```bash
python manage.py startapp shop
```

Now the project contains two applications:

```text
myproject4/
├── blog/
├── shop/
├── myproject4/
└── manage.py
```

### Important

Always run `startapp` from the directory containing `manage.py`.

---

## 5. Register Apps in `INSTALLED_APPS`

After creating an app, Django needs to know that the app exists.

Open:

```text
myproject4/settings.py
```

Find:

```python
INSTALLED_APPS = [
    ...
]
```

Add both applications:

```python
INSTALLED_APPS = [
    ...
    "blog",
    "shop",
]
```

### Why Register Apps?

Registering an app allows Django to recognize and load that application.

If an app is not properly registered, Django may not discover its templates, models, migrations, and other app-related components correctly.

---

## 6. Configure the Templates Directory

In `settings.py`, Django's `TEMPLATES` configuration contains:

```python
TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        ...
    },
]
```

Here:

- `DIRS` → Defines additional/project-level template directories.
- `BASE_DIR / "templates"` → Points to the `templates` folder in the project root.
- `APP_DIRS = True` → Allows Django to search for templates inside installed apps.

### Important: `APP_DIRS`

For app-level templates, keeping:

```python
"APP_DIRS": True,
```

is important.

---

## 7. Create a Project-Level `templates` Folder

Create a `templates` folder in the project's base/root directory:

```text
myproject4/
├── blog/
├── shop/
├── myproject4/
├── templates/
└── manage.py
```

Inside it, create:

```text
templates/
└── base.html
```

---

## 8. Create `base.html`

Create:

```text
templates/base.html
```

Example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Main Page Title</title>
</head>
<body>

    <h1>Welcome to My Project</h1>
    <p>This is the base template for Django project.</p>

</body>
</html>
```

This is a **project-level template**.

Later, we can connect this base template with templates inside our apps using template inheritance.

---

## 9. Create a View for the Blog App

Open:

```text
blog/views.py
```

Import `render`:

```python
from django.shortcuts import render
```

Create a view:

```python
def post_list(request):
    return render(request, "blog/post_list.html")
```

### Understanding the View

```python
def post_list(request):
```

- `post_list` is the view function.
- `request` contains information about the incoming HTTP request.

Then:

```python
return render(request, "blog/post_list.html")
```

tells Django to render the template:

```text
blog/post_list.html
```

---

## 10. Create the Blog App Template Folder

Inside the `blog` app, create:

```text
blog/
└── templates/
```

Inside `templates`, create another folder named after the app:

```text
blog/
├── templates/
│   └── blog/
```

Then create:

```text
post_list.html
```

Final structure:

```text
blog/
├── migrations/
├── templates/
│   └── blog/
│       └── post_list.html
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

### Why `templates/blog/`?

This creates a namespace for the app's templates.

For example:

```text
blog/templates/blog/post_list.html
```

can be referenced as:

```python
"blog/post_list.html"
```

This is especially useful when multiple apps contain templates with the same filename.

---

## 11. Create `post_list.html`

Create:

```text
blog/templates/blog/post_list.html
```

Example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog Page</title>
</head>
<body>

    <h1>Welcome to My Blog Page</h1>
    <p>This is the blog page for my Django project.</p>

</body>
</html>
```

---

## 12. Create URLs for the Blog App

Inside the `blog` app, create:

```text
blog/urls.py
```

Add:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
]
```

### URL Flow

When Django receives:

```text
/blog/
```

the project URL configuration will send the request to the `blog` app.

Then:

```python
path("", views.post_list, name="post_list")
```

calls:

```python
post_list()
```

which renders:

```text
blog/post_list.html
```

---

## 13. Create a View for the Shop App

Open:

```text
shop/views.py
```

Add:

```python
from django.shortcuts import render


def product_list(request):
    return render(request, "shop/product_list.html")
```

Here:

- `product_list` → View function
- `request` → HTTP request
- `"shop/product_list.html"` → Template to render

---

## 14. Create the Shop App Template Folder

Inside the `shop` app, create:

```text
shop/
└── templates/
    └── shop/
```

Then create:

```text
product_list.html
```

Final structure:

```text
shop/
├── migrations/
├── templates/
│   └── shop/
│       └── product_list.html
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

## 15. Create `product_list.html`

Create:

```text
shop/templates/shop/product_list.html
```

Example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Product Page</title>
</head>
<body>

    <h1>Welcome to My Product Page</h1>
    <p>This is the product page for my Django project.</p>

</body>
</html>
```

---

## 16. Create URLs for the Shop App

Create:

```text
shop/urls.py
```

Add:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
]
```

Now the `shop` app has its own URL configuration.

---

## 17. Connect App URLs with the Main Project

Open the main project's:

```text
myproject4/urls.py
```

Import `include`:

```python
from django.urls import path, include
```

Then connect both applications:

```python
urlpatterns = [
    path("admin/", admin.site.urls),

    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
]
```

### What Does `include()` Do?

`include()` connects an app's URL configuration with the project's main URL configuration.

For example:

```python
path("blog/", include("blog.urls"))
```

means:

> Requests beginning with `/blog/` should be handled by `blog/urls.py`.

Similarly:

```python
path("shop/", include("shop.urls"))
```

means:

> Requests beginning with `/shop/` should be handled by `shop/urls.py`.

---

## 18. Complete URL Flow

### Blog Request

Suppose the browser requests:

```text
/blog/
```

The flow is:

```text
Browser
   ↓
myproject4/urls.py
   ↓
path("blog/", include("blog.urls"))
   ↓
blog/urls.py
   ↓
views.post_list
   ↓
blog/templates/blog/post_list.html
   ↓
HTML Response
   ↓
Browser
```

### Shop Request

For:

```text
/shop/
```

the flow is:

```text
Browser
   ↓
myproject4/urls.py
   ↓
path("shop/", include("shop.urls"))
   ↓
shop/urls.py
   ↓
views.product_list
   ↓
shop/templates/shop/product_list.html
   ↓
HTML Response
   ↓
Browser
```

---

## 19. Run the Development Server

Start the server:

```bash
python manage.py runserver
```

You will get a local development URL similar to:

```text
http://127.0.0.1:8000/
```

---

## 20. Test the Blog App

Open:

```text
http://127.0.0.1:8000/blog/
```

Django will:

1. Receive the request.
2. Check the main `urls.py`.
3. Match the `blog/` path.
4. Include `blog.urls`.
5. Match the empty path `""`.
6. Call `post_list`.
7. Render `blog/post_list.html`.
8. Return the HTML response.

You should see the Blog page.

---

## 21. Test the Shop App

Open:

```text
http://127.0.0.1:8000/shop/
```

Django will:

1. Receive the request.
2. Check the main `urls.py`.
3. Match the `shop/` path.
4. Include `shop.urls`.
5. Match the empty path `""`.
6. Call `product_list`.
7. Render `shop/product_list.html`.
8. Return the HTML response.

You should see the Product page.

---

## 22. Why Use App-Level Templates?

App-level templates are useful when a project contains multiple applications.

For example:

```text
Project
│
├── Blog App
│   └── Blog Templates
│
├── Shop App
│   └── Shop Templates
│
└── Account App
    └── Account Templates
```

This keeps each application's files organized.

### Advantages

- Better project organization
- App-specific templates stay with the app
- Easier maintenance
- Easier reuse of applications
- Avoids template filename conflicts when namespacing is used

---

## 23. Recommended App Template Structure

A common Django structure is:

```text
app_name/
├── templates/
│   └── app_name/
│       ├── template1.html
│       ├── template2.html
│       └── template3.html
├── views.py
├── models.py
├── urls.py
└── ...
```

For example:

```text
blog/
├── templates/
│   └── blog/
│       ├── post_list.html
│       └── post_detail.html
├── views.py
├── urls.py
└── models.py
```

---

## 24. Why Use the App Name Inside `templates/`?

Suppose both apps contain a file named:

```text
index.html
```

Without namespacing:

```text
blog/templates/index.html
shop/templates/index.html
```

it can become difficult to clearly identify which template should be loaded.

Instead, use:

```text
blog/templates/blog/index.html
shop/templates/shop/index.html
```

Then render them explicitly:

```python
return render(request, "blog/index.html")
```

and:

```python
return render(request, "shop/index.html")
```

This technique is called **template namespacing**.

---

## 25. Project-Level vs App-Level Templates

### Project-Level

```text
myproject4/
├── templates/
│   └── base.html
└── ...
```

Configured through:

```python
"DIRS": [BASE_DIR / "templates"],
```

### App-Level

```text
blog/
└── templates/
    └── blog/
        └── post_list.html
```

Discovered through:

```python
"APP_DIRS": True,
```

provided the app is installed.

---

## 26. Complete Project Structure

After completing this chapter, the project can look like:

```text
myproject4/
│
├── blog/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── blog/
│   │       └── post_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── shop/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── shop/
│   │       └── product_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── myproject4/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   └── base.html
│
└── manage.py
```

---

## 27. Important Code Summary

### `settings.py`

```python
INSTALLED_APPS = [
    ...
    "blog",
    "shop",
]

TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        ...
    },
]
```

### `blog/views.py`

```python
from django.shortcuts import render


def post_list(request):
    return render(request, "blog/post_list.html")
```

### `blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
]
```

### `shop/views.py`

```python
from django.shortcuts import render


def product_list(request):
    return render(request, "shop/product_list.html")
```

### `shop/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
]
```

### Main `urls.py`

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

## 28. Important Commands

### Create Project

```bash
django-admin startproject myproject4
```

### Move Into Project

```bash
cd myproject4
```

### Create Blog App

```bash
python manage.py startapp blog
```

### Create Shop App

```bash
python manage.py startapp shop
```

### Run Server

```bash
python manage.py runserver
```

### Stop Server

```text
CTRL + C
```

---

## 29. Common Mistakes

### Mistake 1: Forgetting to Register the App

Incorrect:

```python
INSTALLED_APPS = [
    ...
]
```

Correct:

```python
INSTALLED_APPS = [
    ...
    "blog",
    "shop",
]
```

---

### Mistake 2: Setting `APP_DIRS` to `False`

For app-level template discovery, use:

```python
"APP_DIRS": True,
```

---

### Mistake 3: Wrong Template Path

If the file is:

```text
blog/templates/blog/post_list.html
```

use:

```python
return render(request, "blog/post_list.html")
```

Not:

```python
return render(request, "post_list.html")
```

---

### Mistake 4: Forgetting `urls.py` Inside the App

If you use:

```python
include("blog.urls")
```

the `blog` app needs a corresponding:

```text
blog/urls.py
```

---

### Mistake 5: Forgetting `include`

Main project URL configuration should contain:

```python
from django.urls import path, include
```

and:

```python
path("blog/", include("blog.urls"))
```

---

### Mistake 6: Incorrect Template Folder Structure

Recommended:

```text
blog/
└── templates/
    └── blog/
        └── post_list.html
```

Then:

```python
return render(request, "blog/post_list.html")
```

---

## 30. Complete Working Flow

The complete process is:

```text
1. Create Django project
        ↓
2. Create blog and shop apps
        ↓
3. Register both apps in INSTALLED_APPS
        ↓
4. Configure project-level templates directory
        ↓
5. Keep APP_DIRS = True
        ↓
6. Create project-level templates/base.html
        ↓
7. Create blog/templates/blog/
        ↓
8. Create post_list.html
        ↓
9. Create blog view
        ↓
10. Create blog/urls.py
        ↓
11. Create shop/templates/shop/
        ↓
12. Create product_list.html
        ↓
13. Create shop view
        ↓
14. Create shop/urls.py
        ↓
15. Include blog.urls and shop.urls in main urls.py
        ↓
16. Run the server
        ↓
17. Open /blog/
        ↓
18. Open /shop/
        ↓
19. Django renders the respective templates
```

---

## 31. Quick Revision Table

| Concept | Purpose |
| --- | --- |
| `startproject` | Creates a Django project |
| `startapp` | Creates a Django application |
| `INSTALLED_APPS` | Registers applications |
| `TEMPLATES` | Configures Django's template engine |
| `DIRS` | Specifies additional template directories |
| `APP_DIRS` | Enables template discovery inside installed apps |
| `templates/` | Stores templates |
| `views.py` | Contains view functions |
| `render()` | Loads a template and returns an HTTP response |
| `urls.py` | Maps URLs to views |
| `include()` | Connects app URLs to project URLs |
| `blog/post_list.html` | Namespaced blog template |
| `shop/product_list.html` | Namespaced shop template |

---

## 32. Key Takeaways

- A Django project can contain multiple apps.
- Each app can have its own templates.
- App-level templates are commonly stored inside:

```text
app_name/templates/app_name/
```

- `APP_DIRS = True` enables Django to search installed apps for templates.
- Every app should be registered in `INSTALLED_APPS`.
- Each app can have its own `urls.py`.
- `include()` connects app URLs with the main project URLs.
- `render()` connects a view with a template.
- Template namespacing helps avoid conflicts between templates having the same filename.
- Project-level templates are useful for shared templates such as `base.html`.
- App-level templates are useful for app-specific pages such as blog and product pages.

---

## 33. What's Next

In the next chapter, we will learn how to connect the **main `base.html` template** with templates inside our apps.

Instead of writing the same:

```html
<html>
<head>
...
</head>
<body>
...
</body>
</html>
```

in every template, we can create it once in `base.html` and reuse it using **Django Template Inheritance**.

The important concepts will be:

- `{% extends %}`
- `{% block %}`
- Template inheritance
- Reusing `base.html`
- Connecting project-level templates with app-level templates
