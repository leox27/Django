# Chapter 16 - Django Template Inheritance and Static Files

## 1. Introduction

In this chapter, we learn how to properly organize Django templates and static files in a project.

The main topics covered are:

- Template inheritance
- Base template
- Reusable navigation bar
- Template `{% include %}` tag
- Dynamic `{% block %}` sections
- Django static files
- CSS integration
- JavaScript integration
- Image integration
- URL reversing with `{% url %}`
- Forms with POST method
- CSRF protection
- JavaScript events
- Organizing project folders

The goal is to create a reusable structure where common HTML is written only once and individual pages inherit from it.

---

## 2. Why Template Organization Matters

A Django project can contain many pages.

If every page contains the same:

- Header
- Navigation bar
- Footer
- CSS links
- JavaScript files
- HTML structure

then the same code would have to be repeated again and again.

This creates problems:

- More code duplication
- Difficult maintenance
- More chances of mistakes
- Changes need to be made in multiple files

Template inheritance solves this problem by allowing multiple pages to share a common base template.

---

## 3. What Static Files Mean in Django

Static files are files that are generally served as-is rather than generated dynamically by Django.

Common static files include:

- CSS files
- JavaScript files
- Images
- Icons
- Fonts

Example:

```text
static/
├── css/
│   └── style.css
├── js/
│   └── scripts.js
└── images/
    └── logo.png
```

Keeping these files organized makes the project easier to maintain.

---

## 4. Creating the Practice Project

The lecture creates a new Django project named `myproject8`.

Example:

```bash
django-admin startproject myproject8
```

Move into the project directory:

```bash
cd myproject8
```

Create a `blog` application:

```bash
python manage.py startapp blog
```

On systems where `python3` is configured:

```bash
python3 manage.py startapp blog
```

Always run `startapp` from the directory containing `manage.py`.

---

## 5. Overall Project Structure

The project is organized approximately like this:

```text
myproject8/
├── manage.py
│
├── myproject8/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── blog/
│           └── about.html
│
├── templates/
│   ├── base.html
│   ├── navbar.html
│   └── home.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── scripts.js
    └── images/
        └── logo.png
```

This separates:

- Reusable project-level templates
- App-specific templates
- Static assets
- Application logic

---

## 6. Creating the Project-Level Templates Folder

Create a `templates` folder at the project root.

```text
myproject8/
└── templates/
```

This folder contains templates that can be shared across the project.

For example:

```text
templates/
├── base.html
├── navbar.html
└── home.html
```

The `base.html` file will act as the common parent template.

---

## 7. Preparing the Base Page

Create:

```text
templates/base.html
```

The base template contains the common HTML structure used by multiple pages.

Typical responsibilities include:

- HTML document structure
- Page title block
- CSS
- Navigation
- Main content block
- Footer
- JavaScript

The child pages can then inherit this structure.

---

## 8. Separating the Navigation Component

Create:

```text
templates/navbar.html
```

The navigation bar is separated into its own file so it can be reused.

For example:

```html
<nav>
    <ul>
        ...
    </ul>
</nav>
```

Instead of writing the navigation code in every page, it can be included in the base template.

---

## 9. Building the Static Directory

Create a project-level `static` directory:

```text
static/
```

Inside it, create separate folders for different asset types:

```text
static/
├── css/
├── js/
└── images/
```

This keeps different types of static resources organized.

---

## 10. Adding the Stylesheet

Inside the CSS folder, create:

```text
static/css/style.css
```

The final path is:

```text
static/
└── css/
    └── style.css
```

This stylesheet will later be loaded into the base template.

---

## 11. Preparing JavaScript Resources

Create:

```text
static/js/scripts.js
```

The structure becomes:

```text
static/
├── css/
│   └── style.css
└── js/
    └── scripts.js
```

This file can contain JavaScript functionality used by the website.

---

## 12. Storing Images Separately

Create:

```text
static/images/
```

Then place an image such as:

```text
logo.png
```

inside it.

The resulting structure is:

```text
static/
├── css/
│   └── style.css
├── js/
│   └── scripts.js
└── images/
    └── logo.png
```

---

## 13. Registering the Blog Application

Open:

```text
myproject8/settings.py
```

Add the application to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "blog",
]
```

This tells Django that the `blog` application is part of the project.

---

## 14. Configuring the Project-Level Templates

Inside `settings.py`, configure the template directory:

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

### Important points

`BASE_DIR / "templates"` tells Django where the project-level templates are located.

`APP_DIRS = True` allows Django to search for templates inside installed applications.

---

## 15. Understanding the Two Template Locations

Django can work with both project-level and app-level templates.

### Project-level

```text
templates/
├── base.html
├── navbar.html
└── home.html
```

### App-level

```text
blog/
└── templates/
    └── blog/
        └── about.html
```

The app-level structure uses the application name as a namespace.

---

## 16. Creating the Blog Template

Inside the `blog` application, create:

```text
blog/templates/blog/about.html
```

This template will represent the About page.

The `blog` folder inside `templates` helps avoid template-name conflicts between applications.

---

## 17. Creating Application URL Patterns

Create:

```text
blog/urls.py
```

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
```

The `name` values are important because they allow URLs to be referenced dynamically later.

---

## 18. Connecting App URLs to the Project

Open:

```text
myproject8/urls.py
```

Use `include()`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]
```

Now Django forwards matching requests to `blog.urls`.

---

## 19. Creating the Home View

In `blog/views.py`:

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
```

Because `home.html` is located directly inside the project-level `templates` directory, it can be referenced as:

```python
"home.html"
```

---

## 20. Rendering the About Page

Add another view:

```python
def about(request):
    return render(request, "blog/about.html")
```

The template path matches:

```text
blog/templates/blog/about.html
```

Therefore:

```python
render(request, "blog/about.html")
```

loads the About template.

---

## 21. Creating the Base Template Structure

A base template normally contains the common structure of the website.

A simplified example is:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}
            My Site
        {% endblock %}
    </title>
</head>

<body>

    {% include "navbar.html" %}

    <main class="container">
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <p>Footer</p>
    </footer>

</body>
</html>
```

The child pages will provide the actual title and page content.

---

## 22. Using Dynamic Title Blocks

The `{% block %}` tag creates an area that child templates can replace.

Example:

```django
{% block title %}
    My Site
{% endblock %}
```

A child template can replace it with:

```django
{% block title %}
    Home Page
{% endblock %}
```

This allows every page to have its own title while sharing the same base layout.

---

## 23. Understanding the Content Block

A common content section is:

```django
{% block content %}
{% endblock %}
```

Child templates can insert page-specific HTML here.

For example:

```django
{% block content %}
    <h1>Welcome to Home Page</h1>
{% endblock %}
```

The rest of the base template remains unchanged.

---

## 24. Loading Django's Static Template Tag Library

Before using the `{% static %}` tag, load Django's static template tags:

```django
{% load static %}
```

This is normally placed near the top of a template.

Without loading the tag library, Django will not recognize the `static` template tag.

---

## 25. Linking CSS with the Static Tag

Instead of hardcoding a static URL, use:

```django
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

The important part is:

```django
{% static 'css/style.css' %}
```

The path is relative to the configured static directory.

Given:

```text
static/
└── css/
    └── style.css
```

use:

```django
{% static 'css/style.css' %}
```

not:

```django
{% static 'static/css/style.css' %}
```

---

## 26. Including the Navigation Template

The `{% include %}` tag allows one template to include another template.

Example:

```django
{% include "navbar.html" %}
```

This means Django inserts the contents of `navbar.html` at that location.

The benefit is reusability.

If the navigation needs to be changed, you can update `navbar.html` instead of modifying every page.

---

## 27. Adding the Main Content Area

The base template can contain a wrapper:

```html
<div class="container">

    {% block content %}
    {% endblock %}

</div>
```

The child template only needs to provide the content.

This creates a clean separation between:

- Common layout
- Page-specific content

---

## 28. Adding a Footer to the Shared Layout

A footer can be written once in the base template:

```html
<footer>
    <p>Footer</p>
</footer>
```

Every child template that extends `base.html` will automatically receive this footer.

---

## 29. Loading JavaScript from Static Files

The JavaScript file can be loaded using the static tag:

```django
<script src="{% static 'js/scripts.js' %}"></script>
```

For:

```text
static/
└── js/
    └── scripts.js
```

the path is:

```django
{% static 'js/scripts.js' %}
```

---

## 30. Creating the Home Child Template

The Home page extends the base template:

```django
{% extends "base.html" %}
{% load static %}

{% block title %}
    Home Page
{% endblock %}

{% block content %}

    <h1>Welcome to Home Page</h1>

{% endblock %}
```

The `{% extends %}` tag establishes the inheritance relationship.

---

## 31. Understanding `{% extends %}`

The syntax is:

```django
{% extends "base.html" %}
```

It means:

> Use `base.html` as the parent template for this page.

The child template normally overrides blocks defined by the parent.

For example:

```django
{% block title %}
    Home Page
{% endblock %}
```

and:

```django
{% block content %}
    <h1>Welcome to Home Page</h1>
{% endblock %}
```

---

## 32. Adding an Image with the Static Path

Images can also be loaded using `{% static %}`.

Example:

```html
<img src="{% static 'images/logo.png' %}" alt="Home Image">
```

For:

```text
static/
└── images/
    └── logo.png
```

the correct static path is:

```django
{% static 'images/logo.png' %}
```

---

## 33. Creating a POST Form

A simple form can be created like this:

```html
<form method="post">

    {% csrf_token %}

    <input type="text" name="username">

    <input type="password" name="password">

    <button type="submit">Login</button>

</form>
```

The `method="post"` tells the browser to submit the form using HTTP POST.

---

## 34. Understanding CSRF Protection

CSRF stands for:

> Cross-Site Request Forgery

Django provides CSRF protection for forms that perform unsafe state-changing requests such as POST.

Inside a Django template form, use:

```django
{% csrf_token %}
```

This generates a hidden CSRF token that Django can validate when the form is submitted.

---

## 35. Why the CSRF Token Is Important

A POST form should generally include:

```django
{% csrf_token %}
```

when submitted to a Django view protected by CSRF middleware.

The token helps Django verify that the request is associated with the expected site/session context rather than being a forged cross-site request.

If a POST request fails CSRF validation, Django can reject it.

---

## 36. Adding JavaScript Functionality

The `scripts.js` file can contain a function such as:

```javascript
function showAlert() {
    alert("This is JavaScript in Django");
}
```

This function can then be called from an HTML element.

---

## 37. Connecting a Button to JavaScript

A button can call the function using an event handler:

```html
<button type="button" onclick="showAlert()">
    Click Me
</button>
```

When the button is clicked, the JavaScript function runs.

This demonstrates that Django can serve static JavaScript files alongside HTML templates.

---

## 38. Building the Navigation Markup

A basic navigation structure can be:

```html
<nav>
    <ul>
        <li>
            <a href="{% url 'home' %}">Home</a>
        </li>

        <li>
            <a href="{% url 'about' %}">About Us</a>
        </li>
    </ul>
</nav>
```

The important part is the use of:

```django
{% url 'home' %}
```

and:

```django
{% url 'about' %}
```

---

## 39. Why Named URLs Are Useful

Suppose the URL configuration contains:

```python
path("", views.home, name="home")
```

The URL name is:

```text
home
```

The template can then use:

```django
{% url 'home' %}
```

Similarly:

```python
path("about/", views.about, name="about")
```

can be referenced using:

```django
{% url 'about' %}
```

This avoids hardcoding URL paths throughout templates.

---

## 40. Understanding URL Reversing

Consider:

```django
<a href="{% url 'about' %}">About Us</a>
```

Django looks for a URL pattern whose name is:

```text
about
```

For:

```python
path("about/", views.about, name="about")
```

Django generates:

```text
/about/
```

If the actual URL path later changes, the template can continue using the same URL name.

This is called URL reversing.

---

## 41. Static URLs vs Named URL Patterns

These two concepts solve different problems.

### Static asset

```django
{% static 'css/style.css' %}
```

Used for:

- CSS
- JavaScript
- Images
- Other static resources

### Named application URL

```django
{% url 'about' %}
```

Used for:

- Django views
- Application pages
- Dynamic URL generation

Do not confuse `{% static %}` with `{% url %}`.

---

## 42. Creating the About Child Page

The About page can also inherit from the base template:

```django
{% extends "base.html" %}

{% block title %}
    About Us Page
{% endblock %}

{% block content %}

    <h1>About Us</h1>
    <p>This is the About Us page.</p>

{% endblock %}
```

There is no need to duplicate the entire HTML document structure.

---

## 43. Applying Basic CSS

The stylesheet can contain simple rules such as:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #fafafa;
    text-align: center;
    padding: 20px;
}

nav ul {
    list-style: none;
    padding: 10px;
    background: #333;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

h1 {
    color: darkblue;
}
```

The exact styling is not the main purpose of this chapter.

The important concept is correctly connecting the stylesheet through Django's static system.

---

## 44. Complete Template Inheritance Flow

The overall process is:

```text
Browser
   ↓
URL
   ↓
Django URL Pattern
   ↓
View Function
   ↓
Child Template
   ↓
{% extends "base.html" %}
   ↓
Base Template
   ↓
{% include "navbar.html" %}
   ↓
Static CSS / JavaScript / Images
   ↓
Final HTML Response
   ↓
Browser
```

This is the basic relationship between Django views, templates, static files, and inheritance.

---

## 45. Complete Static File Flow

For a CSS file:

```text
Template
   ↓
{% load static %}
   ↓
{% static 'css/style.css' %}
   ↓
Django generates the appropriate static URL
   ↓
Browser requests CSS
   ↓
CSS is applied to the page
```

The same concept applies to JavaScript and images.

---

## 46. Template Organization Benefits

Template inheritance provides several advantages:

- Reduces duplicate HTML
- Creates a consistent layout
- Makes maintenance easier
- Allows reusable components
- Makes individual pages smaller
- Separates common and page-specific code

For example, instead of repeating a navbar on 20 pages, keep it in:

```text
navbar.html
```

and include it once from the base layout.

---

## 47. Common Mistakes to Avoid

### Mistake 1: Forgetting `{% load static %}`

Incorrect:

```django
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

Correct:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### Mistake 2: Including `static/` in the static path

Incorrect:

```django
{% static 'static/css/style.css' %}
```

Correct:

```django
{% static 'css/style.css' %}
```

### Mistake 3: Incorrect template path

For:

```text
blog/templates/blog/about.html
```

use:

```python
render(request, "blog/about.html")
```

### Mistake 4: Missing URL name

If the template uses:

```django
{% url 'about' %}
```

the URL pattern must have:

```python
name="about"
```

### Mistake 5: Missing CSRF token

For a normal Django POST form, remember:

```django
{% csrf_token %}
```

---

## 48. Important File Roles

| File | Purpose |
| --- | --- |
| `base.html` | Common parent template |
| `navbar.html` | Reusable navigation |
| `home.html` | Home page |
| `about.html` | About page |
| `style.css` | Website styling |
| `scripts.js` | JavaScript functionality |
| `logo.png` | Image/static asset |
| `views.py` | Handles requests and returns responses |
| `urls.py` | Maps URLs to views |
| `settings.py` | Project configuration |

---

## 49. Important Django Template Tags

| Tag | Purpose |
| --- | --- |
| `{% extends %}` | Inherits another template |
| `{% block %}` | Defines replaceable template sections |
| `{% include %}` | Includes another template |
| `{% load static %}` | Loads Django's static template tag library |
| `{% static %}` | Generates URLs for static files |
| `{% url %}` | Generates URLs from named URL patterns |
| `{% csrf_token %}` | Adds CSRF token to a form |

---

## 50. Important Commands

Create a project:

```bash
django-admin startproject myproject8
```

Enter the project:

```bash
cd myproject8
```

Create an app:

```bash
python manage.py startapp blog
```

Run the development server:

```bash
python manage.py runserver
```

Check the project:

```bash
python manage.py check
```

---

## 51. Quick Revision

Remember these relationships:

```text
base.html
    ↓
{% block title %}
{% block content %}
    ↓
home.html / about.html
```

Reusable component:

```text
navbar.html
    ↓
{% include "navbar.html" %}
    ↓
base.html
```

Static resources:

```text
static/
├── css/
├── js/
└── images/
```

Static loading:

```django
{% load static %}
```

Static resource:

```django
{% static 'css/style.css' %}
```

Named URL:

```django
{% url 'home' %}
```

POST form:

```django
<form method="post">
    {% csrf_token %}
</form>
```

---

## 52. Interview Questions

### Q1. What is template inheritance in Django?

Template inheritance allows a child template to reuse a common parent template instead of duplicating HTML.

### Q2. Which tag is used for inheritance?

```django
{% extends "base.html" %}
```

### Q3. What is the purpose of `{% block %}`?

It defines sections of the parent template that child templates can override.

### Q4. What does `{% include %}` do?

It includes another template inside the current template.

### Q5. What are static files?

Static files are resources such as CSS, JavaScript, images, icons, and fonts.

### Q6. Which tag is used to reference static files?

```django
{% static 'path/to/file' %}
```

### Q7. Why is `{% load static %}` required?

It loads Django's built-in static template tag library so that the `{% static %}` tag can be used.

### Q8. What is CSRF?

CSRF means Cross-Site Request Forgery. Django provides protection against forged cross-site requests through its CSRF mechanism.

### Q9. Why do Django forms use `{% csrf_token %}`?

It provides a CSRF token that Django can validate for protected requests.

### Q10. What is the purpose of `name` in a URL pattern?

It gives the URL pattern a stable name that can be used with the `{% url %}` template tag.

### Q11. What is URL reversing?

URL reversing means generating a URL from its named URL pattern rather than hardcoding the path.

### Q12. Why separate `navbar.html`?

It makes the navigation reusable and prevents duplication across pages.

---

## 53. Final Takeaways

The most important concepts from this chapter are:

1. Use `base.html` for common page structure.
2. Use `{% extends %}` for template inheritance.
3. Use `{% block %}` for dynamic sections.
4. Use `{% include %}` for reusable template components.
5. Keep CSS, JavaScript, and images inside organized static directories.
6. Use `{% load static %}` before using `{% static %}`.
7. Use `{% static %}` for CSS, JavaScript, and images.
8. Use named URL patterns with `{% url %}` instead of hardcoding application URLs.
9. Use `{% csrf_token %}` in protected Django POST forms.
10. Keep project-level and app-level templates organized according to their purpose.

The overall idea is:

```text
Common structure → base.html
Reusable component → navbar.html
Page-specific content → child templates
Styling → static/css/
JavaScript → static/js/
Images → static/images/
Navigation → named URLs
Forms → POST + CSRF protection
```

---

## 54. What's Next

After understanding template inheritance and static files, the next step is to continue learning Django Template Language features and use them to build more dynamic pages.

The concepts learned here will also become useful when building larger Django applications where many pages share the same layout.
