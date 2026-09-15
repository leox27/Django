# Chapter 13 - Django Templates: Variables, Lists, Objects, Dictionaries, Comments, Default Values, and Auto Escape

## 1. Introduction to Django Templates

In the previous chapters, we learned:

- How to create a Django project.
- How to create an app.
- How to create project-level and app-level template folders.
- How to connect templates with Django apps.
- How to use template inheritance with `base.html`.

In this chapter, we start learning the **basic usage of Django Templates**.

We will learn:

- How to pass variables from a view to an HTML template.
- How to display static and dynamic values.
- How to access list elements.
- How to access dictionary values.
- How to access object attributes.
- How to access nested variables.
- How to provide default values.
- How Django template comments work.
- Basic `safe` and auto-escaping behavior.

---

## 2. What We Will Learn in This Template Series

The template topics are divided into multiple parts.

The overall flow is:

1. Set up templates.
2. Render templates from views.
3. Use variables.
4. Work with lists.
5. Work with dictionaries.
6. Access object attributes.
7. Access nested variables.
8. Use default values.
9. Understand escaping and `safe`.
10. Later learn more Django Template Language features.

The goal is to understand how **Python data from a Django view reaches HTML**.

---

## 3. Create a New Django Project

Create a new Django project using:

```bash
django-admin startproject myproject5
```

This creates a project named:

```text
myproject5
```

---

## 4. Enter the Project Directory

Move into the project directory:

```bash
cd myproject5
```

The `manage.py` file should be available in this directory.

---

## 5. Create the Blog App

Create a new Django app named `blog`:

```bash
python manage.py startapp blog
```

On systems where Python 3 is explicitly required, you may also use:

```bash
python3 manage.py startapp blog
```

The app structure will contain files such as:

```text
blog/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

## 6. Register the App in `INSTALLED_APPS`

Open:

```text
myproject5/settings.py
```

Find:

```python
INSTALLED_APPS = [
    ...
]
```

Add the `blog` app:

```python
INSTALLED_APPS = [
    ...
    "blog",
]
```

Registering the app tells Django that the `blog` application is part of the project.

---

## 7. Configure the Project-Level Templates Directory

If you are using a project-level `templates` folder, configure it in:

```text
myproject5/settings.py
```

Inside `TEMPLATES`, configure `DIRS`:

```python
"DIRS": [BASE_DIR / "templates"],
```

Also make sure:

```python
"APP_DIRS": True,
```

For example:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        ...
    },
]
```

### Important

- `DIRS` tells Django where to search for project-level templates.
- `APP_DIRS=True` allows Django to search inside installed apps for their templates.

---

## 8. Understand Project-Level and App-Level Templates

A project can contain templates at both levels.

### Project-level

```text
myproject5/
├── templates/
│   └── base.html
```

### App-level

For the `blog` app:

```text
blog/
└── templates/
    └── blog/
        └── home.html
```

The nested `blog` folder helps namespace templates and avoid naming conflicts between apps.

---

## 9. Create the Blog View

Open:

```text
blog/views.py
```

The view will prepare data and send it to the template.

For example:

```python
from datetime import datetime
from django.shortcuts import render
```

Here, `datetime` is imported to demonstrate passing a date/time value to the template.

---

## 10. Create a User Class for Demonstration

To demonstrate accessing object attributes, create a simple Python class:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

This creates two attributes:

```python
self.name
self.age
```

We can then create an object:

```python
user = User("Kumar", 30)
```

Now:

```python
user.name
```

contains:

```text
Kumar
```

and:

```python
user.age
```

contains:

```text
30
```

---

## 11. Create the Context Data

The view can prepare different types of data:

```python
def home(request):

    context = {
        "name": "Mohit Kumar",
        "age": 25,
        "skills": ["Python", "Django", "React"],
        "user": User("Kumar", 30),
        "blog": {
            "title": "Django Template Intro",
            "content": "This is bold",
            "created_at": datetime(2025, 8, 18, 10, 30),
        },
        "empty_value": None,
    }

    return render(request, "blog/home.html", context)
```

The `context` dictionary contains the data that will be available inside the template.

---

## 12. Understand the Context Dictionary

The context can contain different types of Python values.

For example:

```python
context = {
    "name": "Mohit Kumar",
    "age": 25,
    "skills": ["Python", "Django", "React"],
    "user": User("Kumar", 30),
}
```

Here:

| Key | Value Type |
| --- | --- |
| `name` | String |
| `age` | Integer |
| `skills` | List |
| `user` | Object |

These values can later be accessed from the HTML template.

---

## 13. Pass Context to the Template

The context is passed to `render()`:

```python
return render(request, "blog/home.html", context)
```

The three important parts are:

```text
request
template name
context
```

So the flow is:

```text
Python View
     ↓
Context Dictionary
     ↓
render()
     ↓
Django Template
     ↓
HTML Response
     ↓
Browser
```

---

## 14. Create the App-Level Template

Inside the `blog` app, create:

```text
blog/
└── templates/
    └── blog/
        └── home.html
```

The complete relevant structure becomes:

```text
myproject5/
│
├── manage.py
│
├── myproject5/
│   ├── settings.py
│   └── urls.py
│
└── blog/
    ├── views.py
    └── templates/
        └── blog/
            └── home.html
```

---

## 15. Create the Basic HTML Template

Inside `home.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Template Basic</title>
</head>

<body>
    <h1>Template Basic</h1>
</body>
</html>
```

This is static HTML.

The browser will receive the HTML after Django processes the template.

---

## 16. Static vs Dynamic Values

### Static value

```html
<p>Name</p>
```

The word `Name` is directly written in the HTML.

### Dynamic value

```html
<p>{{ name }}</p>
```

Here, `name` comes from the Django view's context.

For example:

```python
context = {
    "name": "Mohit Kumar"
}
```

The browser will receive:

```html
<p>Mohit Kumar</p>
```

The important concept is:

```text
{{ variable }}
```

is used to display a template variable.

---

## 17. Single Variable

Suppose the view contains:

```python
context = {
    "name": "Mohit Kumar",
    "age": 25,
}
```

In the template:

```html
<p>Static Name</p>

<p>{{ name }}</p>
<p>{{ age }}</p>
```

Output:

```text
Static Name
Mohit Kumar
25
```

The important difference is:

```html
<p>Name</p>
```

is static.

Whereas:

```html
<p>{{ name }}</p>
```

is dynamic.

---

## 18. Django Template Variable Syntax

Django template variables are normally written using double curly braces:

```django
{{ variable }}
```

Examples:

```django
{{ name }}
{{ age }}
{{ title }}
{{ content }}
```

The variable name should correspond to a value available in the template context.

---

## 19. Map the Blog URL to the View

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
]
```

This maps the empty path to the `home` view.

---

## 20. Include Blog URLs in the Main Project

Open:

```text
myproject5/urls.py
```

Import `include`:

```python
from django.urls import path, include
```

Then:

```python
urlpatterns = [
    path("", include("blog.urls")),
]
```

Now the project sends the request to the `blog` URL configuration.

---

## 21. URL-to-Template Complete Flow

The complete request flow is:

```text
Browser
   ↓
/
   ↓
myproject5/urls.py
   ↓
blog/urls.py
   ↓
views.home()
   ↓
context data
   ↓
render()
   ↓
blog/home.html
   ↓
HTML response
   ↓
Browser
```

This flow is very important for understanding Django.

---

## 22. Run the Django Development Server

Run:

```bash
python manage.py runserver
```

Or:

```bash
python3 manage.py runserver
```

Then open the development server in your browser.

For example:

```text
http://127.0.0.1:8000/
```

---

## 23. Accessing a List

Suppose the context contains:

```python
"skills": ["Python", "Django", "React"]
```

Django templates can access list elements using indexes.

Example:

```django
{{ skills.0 }}
```

Output:

```text
Python
```

The first element has index `0`.

---

## 24. List Indexing in Templates

Given:

```python
skills = ["Python", "Django", "React"]
```

The indexes are:

```text
0 → Python
1 → Django
2 → React
```

Therefore:

```django
{{ skills.0 }}
```

returns:

```text
Python
```

```django
{{ skills.1 }}
```

returns:

```text
Django
```

```django
{{ skills.2 }}
```

returns:

```text
React
```

---

## 25. Display the Complete List

To access the list itself:

```django
{{ skills }}
```

This displays the complete list representation.

For example:

```text
['Python', 'Django', 'React']
```

For displaying list items individually in real applications, template loops are generally more useful:

```django
{% for skill in skills %}
    <p>{{ skill }}</p>
{% endfor %}
```

---

## 26. Accessing Object Attributes

Suppose the view contains:

```python
user = User("Kumar", 30)
```

and the context contains:

```python
"user": user
```

The object has:

```python
user.name
user.age
```

In the Django template:

```django
{{ user.name }}
{{ user.age }}
```

Output:

```text
Kumar
30
```

---

## 27. Important Difference Between Python and Django Template Attribute Access

In Python, we normally write:

```python
user.name
```

Django templates also use dot notation:

```django
{{ user.name }}
```

This allows template code to access values and attributes in a simple way.

The template does not use Python's normal expression syntax everywhere. Django Template Language has its own rules.

---

## 28. Accessing Dictionary Values

Suppose the context contains:

```python
"blog": {
    "title": "Django Template Intro",
    "content": "This is bold",
    "created_at": datetime(2025, 8, 18, 10, 30),
}
```

You can access dictionary values using dot notation:

```django
{{ blog.title }}
```

```django
{{ blog.content }}
```

```django
{{ blog.created_at }}
```

Output may look like:

```text
Django Template Intro
This is bold
2025-08-18 10:30:00
```

---

## 29. Dictionary Access Pattern

The general pattern is:

```django
{{ dictionary.key }}
```

For example:

```django
{{ blog.title }}
```

means that Django looks for the `title` value inside `blog`.

Similarly:

```django
{{ blog.content }}
```

accesses the `content` value.

---

## 30. Working with Date and Time Values

The view can contain:

```python
from datetime import datetime
```

and:

```python
"created_at": datetime(2025, 8, 18, 10, 30)
```

The values represent:

```text
2025 → Year
8    → Month
18   → Day
10   → Hour
30   → Minute
```

The template can display it using:

```django
{{ blog.created_at }}
```

Django template filters can later be used to format dates differently.

---

## 31. Nested Variables

A variable can contain another variable or dictionary.

For example:

```python
"blog": {
    "author": {
        "name": "Mohit Kumar"
    }
}
```

Here the structure is:

```text
blog
 └── author
      └── name
```

To access `name`:

```django
{{ blog.author.name }}
```

Output:

```text
Mohit Kumar
```

---

## 32. Nested Variable Access Pattern

For nested data, continue using dot notation:

```django
{{ object.level1.level2.level3 }}
```

For example:

```django
{{ blog.author.name }}
```

The access path is:

```text
blog
  ↓
author
  ↓
name
```

This is useful when working with nested dictionaries and objects.

---

## 33. Django Template Comments

Django templates support different types of comments.

The important distinction is whether the comment remains in the generated HTML source or is completely removed during template processing.

---

## 34. HTML Comments

HTML comments are written as:

```html
<!-- This is an HTML comment -->
```

HTML comments:

- Are not displayed as normal page content.
- Remain in the generated HTML source.
- Can be seen by inspecting the page source/DOM.

Therefore, do not use HTML comments for sensitive information.

---

## 35. Django Single-Line Comments

Django Template Language provides a comment syntax:

```django
{# This is a Django comment #}
```

This comment is processed by Django and does not appear in the final rendered HTML.

Example:

```django
{# This is a comment #}

<h1>Template Basic</h1>
```

The comment will not be displayed in the browser.

---

## 36. Django Multi-Line Comments

For multiple lines, use:

```django
{% comment %}
This is a multi-line comment.
This text will not appear
in the rendered HTML.
{% endcomment %}
```

This is useful when temporarily commenting out multiple lines of template code.

---

## 37. HTML Comments vs Django Comments

| Comment Type | Syntax | Appears in Generated HTML? |
| --- | --- | --- |
| HTML comment | `<!-- -->` | Yes |
| Django single-line | `{# #}` | No |
| Django multi-line | `{% comment %}` | No |

### Recommended

For comments that are meant only for template developers, use Django Template Language comments:

```django
{# Comment #}
```

or:

```django
{% comment %}
Multi-line comment
{% endcomment %}
```

---

## 38. Understanding `safe`

Django automatically escapes HTML-sensitive content by default.

Suppose the context contains:

```python
"content": "<b>This is bold</b>"
```

If you display:

```django
{{ content }}
```

Django escapes the HTML so that the HTML tags are treated as text rather than being interpreted as HTML.

This protects against unwanted HTML/JavaScript injection.

---

## 39. Using the `safe` Filter

If the content is trusted and you intentionally want Django to render it as HTML, you can use:

```django
{{ content|safe }}
```

For example:

```python
"content": "<b>This is bold</b>"
```

Template:

```django
<p>{{ content|safe }}</p>
```

The `<b>` tag can then be interpreted as HTML.

## Security Note

Only mark content as `safe` when you trust its source.

Do not blindly use `safe` on user-generated content.

---

## 40. Auto Escaping

Django templates automatically escape many HTML-sensitive characters.

For example, content such as:

```html
<script>
```

should not normally be interpreted as executable HTML/JavaScript simply because it came from a context variable.

This behavior is called **auto-escaping**.

It is an important Django security feature.

---

## 41. `safe` vs Auto-Escaping

The basic idea is:

```text
Normal variable
      ↓
Django auto-escapes HTML
      ↓
HTML is treated safely as text
```

Using:

```django
{{ content|safe }}
```

tells Django:

```text
I trust this content and want it treated as HTML.
```

Therefore:

```text
safe = bypass normal HTML escaping for that value
```

Use it carefully.

---

## 42. Default Values for Missing or Empty Data

Sometimes a variable may contain:

```python
None
```

or may be empty.

For example:

```python
"empty_value": None
```

If the template displays:

```django
{{ empty_value }}
```

the output may be blank.

In such cases, we may want to display a meaningful fallback message.

---

## 43. Using the `default` Filter

Django provides the `default` filter:

```django
{{ empty_value|default:"No value provided" }}
```

If the value is considered false/empty, Django displays:

```text
No value provided
```

This is useful for user-friendly output.

---

## 44. `default` Example

Suppose:

```python
"empty_value": ""
```

Template:

```django
<p>{{ empty_value|default:"No value provided" }}</p>
```

Output:

```text
No value provided
```

The exact fallback message is completely customizable.

For example:

```django
{{ empty_value|default:"No data" }}
```

or:

```django
{{ empty_value|default:"Not available" }}
```

---

## 45. `default_if_none` Filter

There is an important distinction between `default` and `default_if_none`.

Use:

```django
{{ value|default_if_none:"No data" }}
```

when you specifically want the fallback to be used when the value is `None`.

Conceptually:

```text
default
    ↓
handles false/empty values

default_if_none
    ↓
handles None specifically
```

This distinction is useful when empty strings and `None` should be treated differently.

---

## 46. Example: `default` vs `default_if_none`

Consider:

```python
context = {
    "value1": "",
    "value2": None,
}
```

With:

```django
{{ value1|default:"No data" }}
```

the fallback can be displayed because the value is empty.

With:

```django
{{ value2|default_if_none:"No data" }}
```

the fallback is displayed because the value is `None`.

---

## 47. Important Template Syntax to Remember

### Display a variable

```django
{{ variable }}
```

### Access a list item

```django
{{ skills.0 }}
```

### Access an object attribute

```django
{{ user.name }}
```

### Access a dictionary value

```django
{{ blog.title }}
```

### Access nested data

```django
{{ blog.author.name }}
```

### Safe HTML

```django
{{ content|safe }}
```

### Default value

```django
{{ value|default:"No data" }}
```

### Default only for `None`

```django
{{ value|default_if_none:"No data" }}
```

---

## 48. Complete Example

### `blog/views.py`

```python
from datetime import datetime
from django.shortcuts import render


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def home(request):

    context = {
        "name": "Mohit Kumar",
        "age": 25,
        "skills": ["Python", "Django", "React"],
        "user": User("Kumar", 30),
        "blog": {
            "title": "Django Template Intro",
            "content": "<b>This is bold</b>",
            "created_at": datetime(2025, 8, 18, 10, 30),
            "author": {
                "name": "Mohit Kumar"
            }
        },
        "empty_value": None,
    }

    return render(request, "blog/home.html", context)
```

---

## 49. Complete Template Example

### `blog/templates/blog/home.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ blog.title }}</title>
</head>

<body>

    <h1>Template Basic</h1>

    <p>Static Name</p>

    <p>{{ name }}</p>

    <p>{{ age }}</p>

    <h2>List Access</h2>

    <p>{{ skills.0 }}</p>
    <p>{{ skills.1 }}</p>
    <p>{{ skills.2 }}</p>

    <h2>Object Attributes</h2>

    <p>{{ user.name }}</p>
    <p>{{ user.age }}</p>

    <h2>Blog Information</h2>

    <p>{{ blog.title }}</p>
    <p>{{ blog.content }}</p>
    <p>{{ blog.created_at }}</p>

    <h2>Nested Variable</h2>

    <p>{{ blog.author.name }}</p>

    <h2>Safe HTML</h2>

    <p>{{ blog.content|safe }}</p>

    <h2>Default Value</h2>

    <p>{{ empty_value|default:"No value provided" }}</p>

    <h2>Default If None</h2>

    <p>{{ empty_value|default_if_none:"No data" }}</p>

</body>
</html>
```

---

## 50. Important Concept: View vs Template

A Django view should generally prepare the data.

For example:

```python
context = {
    "name": "Mohit Kumar",
    "age": 25,
}
```

The template is responsible for displaying that data:

```django
<p>{{ name }}</p>
<p>{{ age }}</p>
```

Think of it as:

```text
View
 ↓
Prepare data

Template
 ↓
Present data
```

This separation makes the application easier to maintain.

---

## 51. Complete Django Template Flow

The complete process is:

```text
1. Browser sends request
        ↓
2. Project urls.py receives URL
        ↓
3. include() sends request to app urls.py
        ↓
4. App urls.py calls the view
        ↓
5. View prepares Python data
        ↓
6. Data is stored in context
        ↓
7. render() receives request + template + context
        ↓
8. Django loads the HTML template
        ↓
9. Django replaces template variables
        ↓
10. Django processes template syntax
        ↓
11. Django generates final HTML
        ↓
12. Browser receives HTML
        ↓
13. User sees the rendered page
```

---

## 52. Common Mistakes

### Mistake 1: App is not registered

Make sure:

```python
INSTALLED_APPS = [
    ...
    "blog",
]
```

---

### Mistake 2: Wrong template path

If the template is:

```text
blog/templates/blog/home.html
```

render it as:

```python
render(request, "blog/home.html", context)
```

Not:

```python
render(request, "home.html", context)
```

---

### Mistake 3: Wrong `DIRS`

For a project-level templates directory:

```python
"DIRS": [BASE_DIR / "templates"],
```

---

### Mistake 4: `APP_DIRS` disabled

For app-level template discovery, make sure:

```python
"APP_DIRS": True
```

---

### Mistake 5: Forgetting the double curly braces

Wrong:

```html
<p>name</p>
```

This displays the literal word:

```text
name
```

Correct:

```django
<p>{{ name }}</p>
```

---

### Mistake 6: Wrong variable name

If the view contains:

```python
"name": "Mohit Kumar"
```

the template must use:

```django
{{ name }}
```

not:

```django
{{ username }}
```

unless `username` also exists in the context.

---

### Mistake 7: Forgetting URL mapping

The template and view will not be reachable through the browser unless the URL is correctly mapped.

Check:

```text
project urls.py
       ↓
app urls.py
       ↓
view
```

---

## 53. Quick Revision Table

| Topic | Syntax / Example |
| --- | --- |
| Template variable | `{{ name }}` |
| List element | `{{ skills.0 }}` |
| Object attribute | `{{ user.name }}` |
| Dictionary value | `{{ blog.title }}` |
| Nested value | `{{ blog.author.name }}` |
| HTML comment | `<!-- comment -->` |
| Django single-line comment | `{# comment #}` |
| Django multi-line comment | `{% comment %} ... {% endcomment %}` |
| Safe HTML | `{{ content\|safe }}` |
| Default value | `{{ value\|default:"No data" }}` |
| Default for `None` | `{{ value\|default_if_none:"No data" }}` |
| Render template | `render(request, "blog/home.html", context)` |

---

## 54. Important Concepts to Remember

- Django templates are used to generate dynamic HTML.
- Data is usually prepared in the view.
- The data is passed to the template through a context dictionary.
- Template variables use:

```django
{{ variable }}
```

- Lists can be accessed using indexes:

```django
{{ skills.0 }}
```

- Object attributes can be accessed using dot notation:

```django
{{ user.name }}
```

- Dictionary values can also be accessed using dot notation:

```django
{{ blog.title }}
```

- Nested values can be accessed using multiple dots:

```django
{{ blog.author.name }}
```

- Django supports template-specific comments.
- `{# ... #}` is a single-line Django comment.
- `{% comment %} ... {% endcomment %}` is useful for multi-line comments.
- Django automatically escapes HTML-sensitive content by default.
- The `safe` filter can intentionally mark trusted HTML as safe.
- `default` provides fallback output for false/empty values.
- `default_if_none` provides fallback output specifically for `None`.

---

## 55. Key Takeaways

The most important things from this chapter are:

1. **Context connects Python data with the HTML template.**

2. **Variables are displayed using double curly braces.**

```django
{{ name }}
```

1. **Lists can be accessed using indexes.**

```django
{{ skills.0 }}
```

1. **Objects can be accessed using attributes.**

```django
{{ user.name }}
```

1. **Dictionary values can be accessed using dot notation.**

```django
{{ blog.title }}
```

1. **Nested data can be accessed using multiple dots.**

```django
{{ blog.author.name }}
```

1. **Django comments can be completely removed from the rendered output.**

2. **Auto-escaping provides important protection when displaying HTML-sensitive content.**

3. **Use `safe` carefully and only with trusted HTML.**

4. **Use default filters when data may be empty or `None`.**

---

## 56. What's Next?

In the upcoming Django Template chapters, we will go deeper into the **Django Template Language (DTL)**.

We will learn more about:

- Variables
- Template filters
- Template tags
- Conditions
- Loops
- Lists and dictionaries
- More advanced template operations
- Template inheritance
- Static files
- Other useful DTL features

The goal is to become comfortable enough with Django templates to build dynamic HTML pages instead of only displaying static HTML.
