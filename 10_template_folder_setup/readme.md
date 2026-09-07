# Chapter 10 - Django Templates and Project-Level Template Setup

## 1. Introduction

Django follows the **MVT (Model-View-Template)** architecture.

So far, we have learned about:

- **Model** → Deals with data and database
- **View** → Handles request and response
- **Template** → Handles the frontend/UI

In this chapter, we will learn:

- What is a Django Template?
- Why do we need Templates?
- Template folder structure
- Project-level Templates
- App-level Templates
- How to create a project-level Template
- How to configure the Template directory in `settings.py`
- How to render an HTML file from a View

---

## 2. What Is a Django Template?

A Django Template is generally an **HTML file** used to display the frontend of a web application.

For example:

```text
home.html
```

can contain:

```html
<h1>Hello World</h1>
<p>This is my first Django project.</p>
```

Templates can contain:

- HTML
- CSS
- Static content
- Dynamic data
- Django Template Language (DTL)
- Variables
- Template tags
- Template logic

The main purpose of a Template is to control what the user sees on the frontend.

---

## 3. Why Do We Need Templates?

Previously, we returned HTML directly from the View:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello World</h1>")
```

This works for small examples.

However, real HTML pages can contain hundreds or thousands of lines of code.

For example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>

    <header>
        ...
    </header>

    <main>
        ...
    </main>

    <footer>
        ...
    </footer>

</body>
</html>
```

Writing large amounts of HTML directly inside Python Views is difficult to:

- Read
- Maintain
- Modify
- Design
- Reuse

Therefore, Django provides **Templates**.

Instead of writing HTML inside the View:

```python
return HttpResponse("<h1>Hello World</h1>")
```

we can create:

```text
templates/home.html
```

and render that HTML file from the View.

---

## 4. Main Purpose of Templates

The Template is mainly responsible for the **presentation layer**.

In simple terms:

```text
View
  ↓
Template
  ↓
HTML
  ↓
Browser
  ↓
User Interface
```

Anything that needs to be displayed to the user can be handled through Templates.

For example:

- Headings
- Paragraphs
- Buttons
- Forms
- Tables
- Images
- Navigation bars
- CSS
- Dynamic data

---

## 5. Static Data vs Dynamic Data

Templates can display both **static** and **dynamic** data.

### Static Data

Static content does not change dynamically.

Example:

```html
<h1>Welcome to My Website</h1>
```

### Dynamic Data

Dynamic data can change depending on the request or application data.

For example:

```html
<h1>Hello {{ username }}</h1>
```

If the View sends:

```python
username = "Mohit"
```

the Template can display:

```text
Hello Mohit
```

Django Templates therefore allow us to combine HTML with dynamic data.

---

## 6. Types of Django Template Structures

Templates can generally be organized at two levels:

1. **Project-level Templates**
2. **App-level Templates**

---

## 7. Project-Level Templates

A project-level Template directory is a **centralized Template folder** used by the project.

Example:

```text
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── templates/
    └── home.html
```

The `templates` folder is located at the project root.

The advantage is that Templates can be centrally organized and configured for the project.

---

## 8. App-Level Templates

An app-level Template structure keeps Templates inside a particular Django application.

A common structure is:

```text
blog/
├── migrations/
├── templates/
│   └── blog/
│       └── home.html
├── views.py
├── models.py
└── ...
```

This keeps the Templates associated with the application.

For example:

```text
blog/templates/blog/home.html
```

can be used for the `blog` application.

App-level Template setup will be covered separately.

---

## 9. Project-Level vs App-Level Templates

| Feature | Project-Level | App-Level |
| --- | --- | --- |
| Location | Project root | Inside an app |
| Structure | Centralized | App-specific |
| Scope | Common project Templates | Specific application |
| Example | `templates/home.html` | `blog/templates/blog/home.html` |
| Useful for | Common/shared Templates | App-specific Templates |

---

## 10. Creating a New Django Project

Create a new Django project:

```bash
django-admin startproject myproject3
```

Move inside the project:

```bash
cd myproject3
```

The basic structure will look like:

```text
myproject3/
├── manage.py
└── myproject3/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

For this chapter, we will work with the project-level Template setup.

---

## 11. Create the `templates` Folder

At the project root, create a folder named:

```text
templates
```

The structure becomes:

```text
myproject3/
├── manage.py
├── templates/
└── myproject3/
    ├── settings.py
    ├── urls.py
    └── ...
```

The `templates` directory will contain our HTML files.

---

## 12. Create `home.html`

Inside the `templates` folder, create:

```text
home.html
```

So the structure becomes:

```text
myproject3/
├── manage.py
├── templates/
│   └── home.html
└── myproject3/
    ├── settings.py
    ├── urls.py
    └── ...
```

For now, create a simple HTML page:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Web Page</title>
</head>

<body>

    <h1>Hello World</h1>

    <p>This is my first Django project.</p>

</body>
</html>
```

---

## 13. Configure Templates in `settings.py`

Now open:

```text
myproject3/settings.py
```

Find:

```python
TEMPLATES = [
    {
        ...
    },
]
```

Inside the configuration, you will find:

```python
"DIRS": [],
```

We need to tell Django where our project-level Templates are located.

Use:

```python
"DIRS": [os.path.join(BASE_DIR, "templates")],
```

---

## 14. Import `os`

If the project uses the `os.path.join()` approach shown in this lesson, add:

```python
import os
```

at the top of `settings.py`.

Then configure:

```python
"DIRS": [os.path.join(BASE_DIR, "templates")],
```

This tells Django:

> Look for Templates inside the `templates` directory located under `BASE_DIR`.

---

## 15. Understanding `BASE_DIR`

Django's `settings.py` already contains a `BASE_DIR` definition.

Conceptually:

```text
BASE_DIR
   ↓
Project Base Directory
   ↓
templates/
```

So:

```python
os.path.join(BASE_DIR, "templates")
```

creates the path to:

```text
BASE_DIR/templates
```

This allows Django to locate the project-level Template folder.

---

## 16. Understanding `DIRS`

The `DIRS` setting tells Django about additional directories where it should search for Templates.

Example:

```python
"DIRS": [
    os.path.join(BASE_DIR, "templates")
],
```

This means Django should search:

```text
BASE_DIR/templates/
```

for Template files.

---

## 17. Understanding `APP_DIRS`

Inside the `TEMPLATES` configuration, Django also has:

```python
"APP_DIRS": True,
```

`APP_DIRS` tells Django to look for Templates inside installed applications' Template directories.

For example:

```text
blog/
└── templates/
    └── blog/
        └── home.html
```

This is especially useful for **app-level Templates**.

Therefore:

```python
"DIRS"
```

and:

```python
"APP_DIRS"
```

serve different purposes.

| Setting | Purpose |
| --- | --- |
| `DIRS` | Additional/project-level Template directories |
| `APP_DIRS` | Template directories inside installed apps |

---

## 18. Create a View

For this demonstration, create a View file in the project root.

Example:

```text
myproject3/
├── manage.py
├── templates/
│   └── home.html
├── views/
│   └── views.py
└── myproject3/
    ├── settings.py
    └── urls.py
```

> In a normal Django project, Views are generally placed inside an application rather than directly in the project root. This structure is used here only to demonstrate how Template rendering works.

---

## 19. Import `render`

Inside the View file:

```python
from django.shortcuts import render
```

`render()` is used to render a Template and return an HTTP response.

Create the View:

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
```

Here:

```python
render(request, "home.html")
```

means:

> Render the `home.html` Template and return it as the response.

---

## 20. How `render()` Works

The `render()` function connects the View with the Template.

The basic syntax is:

```python
render(request, template_name)
```

Example:

```python
return render(request, "home.html")
```

The flow becomes:

```text
Browser
   ↓
URL
   ↓
View
   ↓
render()
   ↓
home.html
   ↓
HTML Response
   ↓
Browser
```

---

## 21. Connect the View to `urls.py`

Open:

```text
myproject3/urls.py
```

Import the View:

```python
from django.urls import path
from views import views
```

Then define the URL:

```python
urlpatterns = [
    path("", views.home, name="home"),
]
```

Now the root URL:

```text
/
```

will call:

```python
views.home
```

---

## 22. Complete Project Structure

The project can look like:

```text
myproject3/
├── manage.py
│
├── templates/
│   └── home.html
│
├── views/
│   └── views.py
│
└── myproject3/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Again, the `views/` structure above is only for demonstrating the project-level setup.

In practical Django development, Views are normally organized inside Django apps.

---

## 23. `home.html`

Example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Web Page</title>
</head>

<body>

    <h1>Hello World</h1>

    <p>This is my first Django project.</p>

</body>
</html>
```

---

## 24. `views.py`

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
```

---

## 25. `urls.py`

```python
from django.contrib import admin
from django.urls import path
from views import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
]
```

---

## 26. Run the Development Server

Run:

```bash
python manage.py runserver
```

Or:

```bash
python3 manage.py runserver
```

Django will start the development server.

Usually:

```text
http://127.0.0.1:8000/
```

Open the URL in your browser.

You should see:

```text
Hello World

This is my first Django project.
```

---

## 27. Adding CSS Directly to the Template

Because `home.html` is an HTML file, we can write CSS in it.

For example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Web Page</title>

    <style>
        h1 {
            color: red;
        }
    </style>
</head>

<body>

    <h1>Hello World</h1>

    <p>This is my first Django project.</p>

</body>
</html>
```

After refreshing the browser, the heading will appear red.

Later, we will learn how to handle CSS, JavaScript, images, and other static files properly using Django's **static files system**.

---

## 28. Why HTML Belongs in Templates

Instead of doing this:

```python
def home(request):
    return HttpResponse(
        "<h1>Hello World</h1>"
        "<p>This is my first project.</p>"
    )
```

we use:

```python
def home(request):
    return render(request, "home.html")
```

and keep the HTML inside:

```text
templates/home.html
```

This gives us a cleaner separation:

```text
Python Logic
     ↓
    View
     ↓
HTML Presentation
     ↓
  Template
```

---

## 29. Project-Level Template Flow

The complete process is:

```text
1. Create Django project
        ↓
2. Create templates folder
        ↓
3. Create home.html
        ↓
4. Configure TEMPLATES["DIRS"]
        ↓
5. Create View
        ↓
6. Import render()
        ↓
7. Render home.html
        ↓
8. Connect View with URL
        ↓
9. Run server
        ↓
10. Open browser
        ↓
11. Django returns HTML page
```

---

## 30. Template Request Flow

```text
Browser
   │
   │ GET /
   ▼
Project urls.py
   │
   ▼
views.home()
   │
   ▼
render(request, "home.html")
   │
   ▼
Django Template Engine
   │
   ▼
templates/home.html
   │
   ▼
HTML Response
   │
   ▼
Browser
```

---

## 31. Important Difference: `HttpResponse` vs `render()`

### Using `HttpResponse`

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello World</h1>")
```

Useful for:

- Simple responses
- Testing
- Very small examples

### Using `render()`

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
```

Useful for:

- HTML pages
- Large HTML files
- Dynamic data
- Django Templates
- Real web applications

---

## 32. Common Mistakes

## Mistake 1: Wrong Template Directory

If your structure is:

```text
templates/
└── home.html
```

then your `DIRS` should point to:

```python
os.path.join(BASE_DIR, "templates")
```

---

## Mistake 2: Forgetting `import os`

If using:

```python
os.path.join(BASE_DIR, "templates")
```

you need:

```python
import os
```

---

## Mistake 3: Wrong Template Name

If the file is:

```text
home.html
```

use:

```python
return render(request, "home.html")
```

not:

```python
return render(request, "homepage.html")
```

---

## Mistake 4: Incorrect URL Mapping

Make sure the URL points to the correct View:

```python
path("", views.home, name="home")
```

---

## Mistake 5: Forgetting `render`

Import:

```python
from django.shortcuts import render
```

before using:

```python
render(request, "home.html")
```

---

## 33. Important Concepts to Remember

### Template

An HTML file used to present content to the user.

### `render()`

Connects a View with a Template and returns the rendered response.

### `DIRS`

Defines additional directories where Django searches for Templates.

### `APP_DIRS`

Allows Django to search for Templates inside installed applications.

### `BASE_DIR`

Represents the base directory of the Django project.

### Project-Level Template

A centralized Template directory configured for the project.

### App-Level Template

A Template directory organized inside a specific Django application.

---

## 34. Quick Revision Table

| Concept | Meaning |
| --- | --- |
| MVT | Model-View-Template architecture |
| Template | HTML presentation layer |
| `home.html` | Example Template file |
| `render()` | Renders a Template |
| `DIRS` | Additional Template directories |
| `APP_DIRS` | Searches app Template directories |
| `BASE_DIR` | Base project directory |
| Project-level Template | Centralized project Template |
| App-level Template | Application-specific Template |
| `include()` | Connects URL configurations |
| Development server | Used to run the Django application locally |

---

## 35. Key Takeaways

- Django follows the **MVT architecture**.
- `T` in MVT stands for **Template**.
- Templates are generally HTML files.
- Templates are responsible for the presentation/UI layer.
- HTML should not normally be written directly inside Views for large pages.
- `render()` is commonly used to render Templates.
- Django Templates can contain both static and dynamic data.
- Templates can be organized at the **project level** or **app level**.
- Project-level Templates are useful for centralized Template management.
- The `DIRS` setting tells Django about additional Template directories.
- `APP_DIRS=True` allows Template discovery inside installed apps.
- `BASE_DIR` can be used to construct the Template directory path.
- CSS can be written inside an HTML Template, although external static files are normally preferred for larger projects.
- Views are generally kept inside Django apps in practical projects.

---
