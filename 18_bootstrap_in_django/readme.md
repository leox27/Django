# Chapter 18 -Bootstrap in Django

## 1. What is Bootstrap?

Bootstrap is a CSS framework that provides ready-made CSS classes and JavaScript components.

It helps us build responsive and professional-looking webpages faster.

Instead of writing all CSS manually, we can use Bootstrap classes such as:

- `btn`
- `btn-primary`
- `btn-success`
- `container`
- `row`
- `col`
- `card`
- `navbar`
- `alert`
- `badge`

---

## 2. Three Ways to Use Bootstrap in Django

Bootstrap can be added to a Django project mainly in three ways:

1. CDN
2. Downloaded Bootstrap files
3. `django-bootstrap5` package

---

## 3. Method 1 — Bootstrap Using CDN

CDN means **Content Delivery Network**.

Bootstrap's CSS and JavaScript files are loaded from an external CDN.

### Basic setup

In `base.html`, put the Bootstrap CSS link inside `<head>`:

```html
<head>
    <meta charset="UTF-8">

    <title>{% block title %}My Project{% endblock title %}</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>
```

Put the Bootstrap JavaScript before `</body>`:

```html
<script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js">
</script>

</body>
```

### Important

The exact Bootstrap version can change.

Always use the current CDN code from the official Bootstrap documentation when starting a new project.

### Example button

```html
<button class="btn btn-primary">
    Click Me
</button>

<button class="btn btn-success">
    Save
</button>

<button class="btn btn-danger">
    Delete
</button>
```

If Bootstrap is loaded correctly, these buttons will receive Bootstrap styling.

### Advantages

- Very quick setup
- No Bootstrap files need to be stored in the project
- Easy to start with
- Easy to switch to another Bootstrap version

### Disadvantages

- Requires internet access to load the CDN resource
- The external CDN becomes a dependency
- If the resource cannot be reached, Bootstrap may not load

---

## 4. Method 2 — Download Bootstrap Files

In this method, Bootstrap files are downloaded and stored inside the Django project's static files.

### Step 1 — Download Bootstrap

Go to the official Bootstrap website and download the Bootstrap package.

After extracting the ZIP file, you will typically find CSS and JS files.

For example:

```text
bootstrap/
│
├── css/
│   ├── bootstrap.css
│   └── bootstrap.min.css
│
└── js/
    ├── bootstrap.js
    └── bootstrap.bundle.min.js
```

### Step 2 — Copy CSS

Copy:

```text
bootstrap.min.css
```

into your Django static CSS folder.

Example:

```text
project/
│
├── static/
│   ├── css/
│   │   └── bootstrap.min.css
│   │
│   └── js/
│
├── templates/
│   └── base.html
│
└── manage.py
```

### Step 3 — Copy JavaScript

Copy:

```text
bootstrap.bundle.min.js
```

into:

```text
static/js/
```

Example:

```text
static/
├── css/
│   └── bootstrap.min.css
│
└── js/
    └── bootstrap.bundle.min.js
```

### Step 4 — Load static files

At the top of `base.html`:

```django
{% load static %}
```

### Step 5 — Link Bootstrap CSS

Inside `<head>`:

```html
<link
    rel="stylesheet"
    href="{% static 'css/bootstrap.min.css' %}"
>
```

### Step 6 — Link Bootstrap JavaScript

Before `</body>`:

```html
<script
    src="{% static 'js/bootstrap.bundle.min.js' %}">
</script>
```

### Complete basic example

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>
        {% block title %}
        My Django Project
        {% endblock title %}
    </title>

    <link
        rel="stylesheet"
        href="{% static 'css/bootstrap.min.css' %}"
    >

</head>

<body>

    {% block content %}
    {% endblock content %}

    <script
        src="{% static 'js/bootstrap.bundle.min.js' %}">
    </script>

</body>

</html>
```

### Advantage

- Does not depend on an external CDN at runtime
- Bootstrap can work without internet after the files are available locally
- You control the files stored in the project
- You can customize the downloaded source/build if required

### Disadvantage

- Bootstrap updates must be handled manually
- Project contains additional static files
- You must manage the Bootstrap version yourself

---

## 5. Method 3 — Install `django-bootstrap5`

This method uses the Python package:

```text
django-bootstrap5
```

### Step 1 — Install the package

Activate your virtual environment first.

Then run:

```bash
pip install django-bootstrap5
```

### Step 2 — Add the package to `INSTALLED_APPS`

Open:

```text
settings.py
```

Add:

```python
INSTALLED_APPS = [

    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party app
    "django_bootstrap5",

    # Your apps
]
```

### Importants

The package installed with:

```bash
pip install django-bootstrap5
```

is registered in Django as:

```python
"django_bootstrap5"
```

Do not confuse the Python package name with the Django app name.

---

## 6. Using Bootstrap Templates with `django-bootstrap5`

In your template, load the Bootstrap template tags:

```django
{% load django_bootstrap5 %}
```

You can then use the package's template tags where appropriate.

For example, with a Django form:

```django
<form method="post">

    {% csrf_token %}

    {% bootstrap_form form %}

    <button type="submit" class="btn btn-primary">
        Submit
    </button>

</form>
```

The package can help render Django forms using Bootstrap styling.

---

## 7. Important Difference Between the Three Methods

| Method | Main Idea | Internet at Runtime | Main Management |
| --- | --- | --- | --- |
| CDN | Load Bootstrap from external server | Usually required | CDN/version |
| Downloaded files | Keep Bootstrap inside project | Not required for Bootstrap files | You manage files |
| `django-bootstrap5` | Python/Django integration package | Depends on how its static assets are served | Python package |

The three approaches solve slightly different problems.

For normal Bootstrap CSS/JS usage, CDN or local static files are straightforward.

`django-bootstrap5` is especially useful when you want Bootstrap-aware Django form rendering.

---

## 8. Bootstrap Components

Bootstrap provides many ready-made components and utilities.

Common examples:

```text
Buttons
Cards
Alerts
Badges
Navbar
Modal
Carousel
Progress bars
Forms
Tables
Dropdowns
Pagination
Spinners
Toasts
```

You can copy the required component markup from Bootstrap documentation and adapt it to your Django template.

---

## 9. Bootstrap Button Example

```html
<button class="btn btn-primary">
    Primary
</button>

<button class="btn btn-secondary">
    Secondary
</button>

<button class="btn btn-success">
    Success
</button>

<button class="btn btn-danger">
    Danger
</button>

<button class="btn btn-warning">
    Warning
</button>

<button class="btn btn-info">
    Info
</button>
```

Bootstrap styles the buttons through classes.

The basic pattern is:

```html
class="btn btn-primary"
```

`btn` gives the button its Bootstrap button styling.

`btn-primary` defines the button variant.

---

## 10. Bootstrap Container

A container controls the width and spacing of page content.

```html
<div class="container">

    <h1>My Django Website</h1>

    <p>
        This content is inside a Bootstrap container.
    </p>

</div>
```

---

## 11. Bootstrap Grid

Bootstrap provides a responsive grid system.

Basic example:

```html
<div class="container">

    <div class="row">

        <div class="col">
            Column 1
        </div>

        <div class="col">
            Column 2
        </div>

        <div class="col">
            Column 3
        </div>

    </div>

</div>
```

Responsive example:

```html
<div class="container">

    <div class="row">

        <div class="col-md-4">
            Left
        </div>

        <div class="col-md-8">
            Right
        </div>

    </div>

</div>
```

---

## 12. Bootstrap Card

```html
<div class="card" style="width: 18rem;">

    <div class="card-body">

        <h5 class="card-title">
            Student
        </h5>

        <p class="card-text">
            Python Full Stack Developer
        </p>

        <a href="#" class="btn btn-primary">
            View Profile
        </a>

    </div>

</div>
```

---

## 13. Bootstrap Alert

```html
<div class="alert alert-success">
    Data saved successfully.
</div>

<div class="alert alert-danger">
    Something went wrong.
</div>

<div class="alert alert-warning">
    Please check your information.
</div>
```

---

## 14. Django + Bootstrap + Static Files

When Bootstrap files are stored locally, remember the normal Django static-file workflow.

### Template

```django
{% load static %}
```

### CSS

```html
<link
    rel="stylesheet"
    href="{% static 'css/bootstrap.min.css' %}"
>
```

### JavaScript

```html
<script
    src="{% static 'js/bootstrap.bundle.min.js' %}">
</script>
```

The important idea is:

```text
Django template
      ↓
{% load static %}
      ↓
{% static 'path/to/file' %}
      ↓
Django resolves the static-file URL
```

---

## 15. Why `base.html` Is Useful

If multiple Django pages use Bootstrap, put Bootstrap's CSS and JavaScript in `base.html`.

Example:

```text
templates/
│
├── base.html
│
└── students/
    ├── home.html
    └── profile.html
```

`base.html`:

```django
{% load static %}

<!DOCTYPE html>
<html>

<head>

    <link
        rel="stylesheet"
        href="{% static 'css/bootstrap.min.css' %}"
    >

</head>

<body>

    {% block content %}
    {% endblock content %}

    <script
        src="{% static 'js/bootstrap.bundle.min.js' %}">
    </script>

</body>

</html>
```

Child template:

```django
{% extends "base.html" %}

{% block content %}

<div class="container">

    <h1 class="text-primary">
        Student Profile
    </h1>

    <button class="btn btn-success">
        Save
    </button>

</div>

{% endblock content %}
```

Now the child template automatically receives Bootstrap from `base.html`.

---

## 16. Bootstrap and Custom CSS

Bootstrap does not prevent you from writing your own CSS.

You can use both.

Example:

```html
{% load static %}

<link
    rel="stylesheet"
    href="{% static 'css/bootstrap.min.css' %}"
>

<link
    rel="stylesheet"
    href="{% static 'css/style.css' %}"
>
```

Example custom CSS:

```css
.student-card {
    border-radius: 15px;
    padding: 20px;
}
```

HTML:

```html
<div class="student-card card">

    <div class="card-body">

        <h2 class="text-primary">
            Mayur
        </h2>

        <button class="btn btn-success">
            View
        </button>

    </div>

</div>
```

Here:

```text
Bootstrap
    +
Your CSS
    =
Complete design
```

---

## 17. Common Mistakes

## Mistake 1 — Forgetting `{% load static %}`

Wrong:

```html
<link
    rel="stylesheet"
    href="{% static 'css/bootstrap.min.css' %}"
>
```

Correct:

```django
{% load static %}
```

then:

```html
<link
    rel="stylesheet"
    href="{% static 'css/bootstrap.min.css' %}"
>
```

---

## Mistake 2 — Wrong static path

If the file is:

```text
static/css/bootstrap.min.css
```

use:

```django
{% static 'css/bootstrap.min.css' %}
```

Not:

```django
{% static 'bootstrap.min.css' %}
```

---

## Mistake 3 — Bootstrap CSS not loaded

If this:

```html
<button class="btn btn-primary">
    Test
</button>
```

looks like a normal HTML button, check whether Bootstrap CSS is correctly loaded.

---

## Mistake 4 — JavaScript component does not work

Some Bootstrap components require Bootstrap JavaScript.

For example, interactive components such as modals and dropdowns may require the Bootstrap JS bundle.

Use:

```html
<script
    src="{% static 'js/bootstrap.bundle.min.js' %}">
</script>
```

---

## 18. Virtual Environment

A virtual environment keeps project dependencies isolated.

Example:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Activate on macOS/Linux:

```bash
source venv/bin/activate
```

After activation, install packages inside that environment:

```bash
pip install django
pip install django-bootstrap5
```

This keeps project dependencies separate from the global Python installation.

---

## 19. Basic Installation Workflow

For a new Django project:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install Django:

```bash
pip install django
```

Create a project:

```bash
django-admin startproject myproject
```

Move into the project:

```bash
cd myproject
```

Create an app:

```bash
python manage.py startapp myapp
```

Run the server:

```bash
python manage.py runserver
```

---

## 20. Quick Bootstrap CDN Workflow

```text
1. Create Django project
2. Create app
3. Create base.html
4. Open Bootstrap documentation
5. Copy Bootstrap CSS CDN
6. Put CSS inside <head>
7. Copy Bootstrap JS CDN
8. Put JS before </body>
9. Use Bootstrap classes
10. Run Django server
11. Open the page
12. Check the styling
```

---

## 21. Quick Local Bootstrap Workflow

```text
1. Download Bootstrap
2. Extract ZIP
3. Copy bootstrap.min.css
4. Put it inside static/css/
5. Copy bootstrap.bundle.min.js
6. Put it inside static/js/
7. Add {% load static %}
8. Link Bootstrap CSS
9. Link Bootstrap JS
10. Run Django server
11. Test a Bootstrap component
```

---

## 22. Quick `django-bootstrap5` Workflow

```text
1. Activate virtual environment
2. Install django-bootstrap5
3. Add django_bootstrap5 to INSTALLED_APPS
4. Load django_bootstrap5 in templates
5. Use its template tags where needed
6. Run the Django server
7. Test Bootstrap styling/forms
```

Installation:

```bash
pip install django-bootstrap5
```

Settings:

```python
INSTALLED_APPS = [
    # ...
    "django_bootstrap5",
]
```

Template:

```django
{% load django_bootstrap5 %}
```

---

## 23. What You Should Remember

```text
Bootstrap = CSS framework

CDN
→ Fast setup
→ External Bootstrap files
→ Internet dependency

Downloaded files
→ Bootstrap stored in project
→ No runtime CDN dependency
→ Manual updates

django-bootstrap5
→ Python/Django package
→ Useful for Bootstrap integration
→ Especially useful with Django forms
```

---

## 24. Most Important Django Code

### CDN

```html
<link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css"
    rel="stylesheet"
>

<script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js">
</script>
```

### Local files

```django
{% load static %}

<link
    rel="stylesheet"
    href="{% static 'css/bootstrap.min.css' %}"
>

<script
    src="{% static 'js/bootstrap.bundle.min.js' %}">
</script>
```

### Package

```bash
pip install django-bootstrap5
```

```python
INSTALLED_APPS = [
    # ...
    "django_bootstrap5",
]
```

```django
{% load django_bootstrap5 %}
```

---

## 25. Interview-Level Understanding

### What is Bootstrap?

Bootstrap is a front-end CSS framework that provides reusable styles, responsive layout utilities, components, and JavaScript-powered UI components.

### Why use Bootstrap with Django?

Django handles the backend, templates, URLs, views, models, and application logic.

Bootstrap helps create the frontend UI quickly.

```text
Django
   ↓
Backend + Templates
   ↓
HTML
   ↓
Bootstrap
   ↓
Styling + Responsive UI
```

### Is Bootstrap a Python package?

Bootstrap itself is a front-end framework.

`django-bootstrap5` is a Python package that integrates Bootstrap-related functionality with Django.

### Does Django require Bootstrap?

No.

Django can work without Bootstrap.

Bootstrap is an optional frontend framework.

---

## 26. Final Cheat Sheet

```text
BOOTSTRAP
│
├── CDN
│   ├── Fast setup
│   ├── External files
│   └── Runtime internet dependency
│
├── Download
│   ├── Files stored locally
│   ├── No CDN dependency
│   └── Manual updates
│
└── django-bootstrap5
    ├── Install with pip
    ├── Add to INSTALLED_APPS
    ├── Load template tags
    └── Useful for Django/Bootstrap integration
```

## Most common Bootstrap classes

```text
btn
btn-primary
btn-success
btn-danger
btn-warning
container
row
col
col-md-4
card
card-body
alert
badge
navbar
text-primary
text-center
mt-3
mb-3
p-3
```

### Core idea

```text
Django
  +
HTML
  +
Bootstrap
  +
Custom CSS
  =
Responsive Django Web Application
```
