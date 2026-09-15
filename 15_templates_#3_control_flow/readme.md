# Chapter 15 - Django Template Control Flow and Built-in Template Tags

## 1. Introduction

Django templates provide several built-in tags that allow us to control how data is displayed.

In this chapter, we learn:

- `if`
- `elif`
- `else`
- `for`
- `empty`
- `with`
- `cycle`
- `firstof`
- `now`
- `verbatim`
- `autoescape`
- Template parsing behavior
- Loop variables such as `forloop.counter`

These features make templates more dynamic and useful.

---

## 2. Basic Project Setup

Assume the project contains:

```text
myproject7/
├── manage.py
├── myproject7/
│   ├── settings.py
│   └── urls.py
├── blog/
│   ├── views.py
│   └── urls.py
└── templates/
    └── blog/
        └── blog_list.html
```

The project-level `templates` directory should be configured in `settings.py`:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
    },
]
```

---

## 3. Creating the View

Import `datetime` and create a view:

```python
from datetime import datetime
from django.shortcuts import render


def blog_list(request):
    blogs = [
        {
            "title": "Django Basic",
            "is_featured": True,
            "author": "Mohit Kumar",
        },
        {
            "title": "Django Advanced",
            "is_featured": False,
            "author": "Anu Chaudhary",
        },
        {
            "title": "Django REST Framework",
            "is_featured": False,
            "author": "",
        },
    ]

    context = {
        "blogs": blogs,
        "today": datetime.now(),
        "html_code": "<h1>Welcome to my page</h1>",
    }

    return render(
        request,
        "blog/blog_list.html",
        context
    )
```

The `render()` function receives:

```text
request
template name
context
```

The context contains the data that will be available in the template.

---

## 4. Connecting the View to the URL

In `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
]
```

In the project's `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    path("blog/", include("blog.urls")),
]
```

Now visit:

```text
http://127.0.0.1:8000/blog/
```

---

## 5. Template Variable Basics

Inside:

```text
templates/blog/blog_list.html
```

a normal variable can be displayed using:

```django
{{ blogs }}
```

A dictionary/list value can be accessed using dot notation:

```django
{{ blogs.0.title }}
```

This accesses the title of the first blog.

---

## 6. The `if` Tag

The `if` tag is used to execute template content only when a condition is true.

Syntax:

```django
{% if condition %}
    Content
{% endif %}
```

Example:

```django
{% if blogs.0.is_featured %}
    <h2>Featured Blog</h2>
{% endif %}
```

If `is_featured` is `True`, the content is displayed.

---

## 7. The `if-else` Condition

We can provide an alternative using `else`.

Syntax:

```django
{% if condition %}
    Content when true
{% else %}
    Content when false
{% endif %}
```

Example:

```django
{% if blogs.0.is_featured %}
    <h2>Featured Blog</h2>
{% else %}
    <h2>Not a Featured Blog</h2>
{% endif %}
```

---

## 8. Using `elif`

Django also supports `elif`.

Example:

```django
{% if blogs.0.is_featured %}
    <p>Featured</p>
{% elif blogs.0.title %}
    <p>Blog Available</p>
{% else %}
    <p>No Blog Available</p>
{% endif %}
```

The conditions are checked from top to bottom.

---

## 9. How `if-else` Works

The basic flow is:

```text
Start
  ↓
Check condition
  ↓
Is condition True?
  ├── Yes → Execute if block
  │
  └── No → Execute else block
  ↓
End
```

For example:

```text
is_featured = True
        ↓
    if condition
        ↓
       True
        ↓
Featured Blog
```

---

## 10. The `for` Loop

The `for` tag is used to iterate over a list or other iterable value.

Syntax:

```django
{% for item in items %}
    {{ item }}
{% endfor %}
```

Example:

```django
<ul>
    {% for blog in blogs %}
        <li>{{ blog.title }}</li>
    {% endfor %}
</ul>
```

If there are three blogs, the loop executes three times.

---

## 11. Accessing Dictionary Values in a Loop

Because each blog is a dictionary, we can access its fields using dot notation.

```django
{% for blog in blogs %}
    <p>{{ blog.title }}</p>
    <p>{{ blog.author }}</p>
{% endfor %}
```

The loop variable:

```text
blog
```

represents the current item.

---

## 12. Using `forloop.counter`

Django provides special loop variables through `forloop`.

The most common one is:

```django
{{ forloop.counter }}
```

It starts from:

```text
1
```

Example:

```django
{% for blog in blogs %}
    <p>
        {{ forloop.counter }}.
        {{ blog.title }}
    </p>
{% endfor %}
```

Output:

```text
1. Django Basic
2. Django Advanced
3. Django REST Framework
```

### Important

Python list indexing starts from `0`, but:

```django
forloop.counter
```

starts from `1`.

---

## 13. Useful `forloop` Variables

Django provides several useful variables inside a `for` loop.

| Variable | Meaning |
| --- | --- |
| `forloop.counter` | Current iteration starting at 1 |
| `forloop.counter0` | Current iteration starting at 0 |
| `forloop.revcounter` | Remaining iterations starting at 1 |
| `forloop.revcounter0` | Remaining iterations starting at 0 |
| `forloop.first` | `True` on first iteration |
| `forloop.last` | `True` on last iteration |
| `forloop.parentloop` | Access outer loop when nested |

---

## 14. The `empty` Clause

The `empty` clause can be used with a `for` loop.

It displays alternative content when the list contains no items.

Syntax:

```django
{% for item in items %}
    {{ item }}
{% empty %}
    No items available.
{% endfor %}
```

Example:

```django
<ul>
    {% for blog in blogs %}
        <li>{{ blog.title }}</li>
    {% empty %}
        <li>No blogs available.</li>
    {% endfor %}
</ul>
```

If `blogs` is empty:

```python
blogs = []
```

the output becomes:

```text
No blogs available.
```

---

## 15. `for` Loop with `empty` Flow

The flow is:

```text
Check blogs
     ↓
Is the collection empty?
     ├── No → Run for loop
     │
     └── Yes → Run empty block
```

This is useful for:

- Empty search results
- Empty product lists
- Empty blog lists
- Empty notifications
- Empty database querysets

---

## 16. The `with` Tag

The `with` tag creates a local variable for a value or expression.

Syntax:

```django
{% with variable=value %}
    {{ variable }}
{% endwith %}
```

Example:

```django
{% with total=blogs|length %}
    <p>Total Blogs: {{ total }}</p>
{% endwith %}
```

Here:

```django
blogs|length
```

is calculated once and stored in:

```text
total
```

---

## 17. Why Use `with`?

The `with` tag can make templates:

- Easier to read
- Less repetitive
- Cleaner
- More convenient when the same expression is used multiple times

Example without `with`:

```django
<p>Total: {{ blogs|length }}</p>
<p>There are {{ blogs|length }} blogs.</p>
```

Using `with`:

```django
{% with total=blogs|length %}
    <p>Total: {{ total }}</p>
    <p>There are {{ total }} blogs.</p>
{% endwith %}
```

---

## 18. The `cycle` Tag

The `cycle` tag is useful when we want to alternate between values during a loop.

For example, we can alternate row styles:

```text
Light Blue
Light Green
Light Blue
Light Green
```

Syntax:

```django
{% cycle "lightblue" "lightgreen" %}
```

---

## 19. Using `cycle` in a Table

Example:

```html
<table border="1">
    {% for blog in blogs %}
        <tr style="background-color: {% cycle 'lightblue' 'lightgreen' %};">
            <td>{{ forloop.counter }}</td>
            <td>{{ blog.title }}</td>
            <td>{{ blog.author }}</td>
        </tr>
    {% endfor %}
</table>
```

The cycle changes its value on every iteration.

Output conceptually:

```text
Row 1 → lightblue
Row 2 → lightgreen
Row 3 → lightblue
Row 4 → lightgreen
```

---

## 20. Why Use `cycle`?

`cycle` is useful for:

- Alternating table row colors
- Alternating CSS classes
- Repeating visual patterns
- Making long lists easier to read

The important idea is:

```text
Value 1
   ↓
Value 2
   ↓
Value 1
   ↓
Value 2
```

---

## 21. The `firstof` Tag

The `firstof` tag displays the first variable that evaluates to a usable value.

Syntax:

```django
{% firstof variable1 variable2 variable3 %}
```

Example:

```django
{% firstof blog.author "Anonymous" %}
```

If `blog.author` is available, it is displayed.

Otherwise:

```text
Anonymous
```

is displayed.

---

## 22. Practical `firstof` Example

Suppose:

```python
blog = {
    "author": "",
}
```

Then:

```django
{% firstof blog.author "Anonymous" %}
```

will display:

```text
Anonymous
```

If:

```python
blog = {
    "author": "Mohit Kumar",
}
```

the same template displays:

```text
Mohit Kumar
```

This makes `firstof` useful for fallback values.

---

## 23. The `now` Tag

The `now` tag displays the current date and/or time.

Syntax:

```django
{% now "FORMAT" %}
```

Example:

```django
<p>{% now "d M Y" %}</p>
```

Possible output:

```text
15 Sep 2026
```

The exact output depends on the current date.

---

## 24. Formatting with `now`

We can specify different formats.

Example:

```django
{% now "d/m/Y" %}
```

Date:

```text
15/09/2026
```

Time:

```django
{% now "H:i:s" %}
```

Possible output:

```text
14:30:25
```

Useful format characters include:

| Format | Meaning |
| --- | --- |
| `d` | Day |
| `m` | Month number |
| `M` | Short month name |
| `Y` | Four-digit year |
| `H` | 24-hour |
| `i` | Minutes |
| `s` | Seconds |

---

## 25. `verbatim` Tag

Django normally interprets template syntax such as:

```django
{{ variable }}
```

and:

```django
{% if condition %}
```

Sometimes we want Django to display this syntax as plain text instead of processing it.

The `verbatim` tag is used for this purpose.

Syntax:

```django
{% verbatim %}
    {{ variable }}
{% endverbatim %}
```

The template syntax inside the block is not interpreted by Django.

---

## 26. Example of `verbatim`

```django
{% verbatim %}
    <p>{{ blog.title }}</p>
{% endverbatim %}
```

The browser receives the template syntax as text rather than Django replacing:

```django
{{ blog.title }}
```

with an actual value.

This can be useful when displaying:

- Template examples
- Code snippets
- Documentation
- Template syntax itself

---

## 27. Template Parsing and `verbatim`

Normally Django parses template syntax.

For example:

```django
{{ blog.title }}
```

is recognized as a template variable.

With:

```django
{% verbatim %}
{{ blog.title }}
{% endverbatim %}
```

Django skips normal template interpretation for that section.

Conceptually:

```text
Normal template
      ↓
Django parses syntax
      ↓
Variable gets evaluated
```

With `verbatim`:

```text
verbatim block
      ↓
Django does not interpret template syntax normally
      ↓
Syntax is displayed as text
```

---

## 28. Autoescaping in Django

Django templates use automatic HTML escaping by default.

This is an important security feature.

Suppose the context contains:

```python
html_code = "<h1>Welcome</h1>"
```

Displaying:

```django
{{ html_code }}
```

does not normally render the `<h1>` as HTML.

Instead, Django escapes the HTML characters.

Conceptually:

```text
<h1>Welcome</h1>
```

becomes escaped HTML such as:

```text
&lt;h1&gt;Welcome&lt;/h1&gt;
```

The browser therefore treats it as text rather than executing it as an HTML element.

---

## 29. Why Autoescaping Is Important

Automatic escaping helps protect templates from HTML injection and common cross-site scripting (XSS) risks when untrusted content is displayed.

For example, if a user submits HTML or JavaScript as input, Django's default escaping helps prevent that input from being interpreted as executable HTML/JavaScript.

Therefore:

```text
Autoescaping ON
        ↓
HTML is escaped
        ↓
Safer rendering of untrusted content
```

---

## 30. The `safe` Filter

The `safe` filter tells Django that a value should be treated as safe HTML.

Example:

```django
{{ html_code|safe }}
```

If:

```python
html_code = "<h1>Welcome</h1>"
```

then the `<h1>` can be interpreted as HTML.

### Important Security Rule

Do **not** use `safe` on untrusted user input.

For example, avoid:

```django
{{ user_input|safe }}
```

when `user_input` comes directly from users.

Doing so can create security vulnerabilities such as XSS.

Use `safe` only when you understand and trust the source of the HTML.

---

## 31. The `autoescape` Tag

Django also provides the `autoescape` tag to control automatic escaping inside a specific template section.

Syntax:

```django
{% autoescape off %}
    {{ html_code }}
{% endautoescape %}
```

With autoescaping disabled, HTML contained in the variable may be rendered as HTML.

It can also explicitly be enabled:

```django
{% autoescape on %}
    {{ html_code }}
{% endautoescape %}
```

---

## 32. Why `autoescape off` Should Be Used Carefully

Disabling autoescaping can allow HTML from variables to be interpreted by the browser.

This becomes dangerous when the variable contains untrusted user input.

For example:

```text
User input
    ↓
autoescape off
    ↓
HTML/JavaScript may be interpreted
    ↓
Potential XSS vulnerability
```

Therefore, automatic escaping should normally remain enabled.

---

## 33. Default Autoescaping Behavior

For normal Django HTML templates, automatic escaping is enabled by default.

This means Django protects template output by escaping special HTML characters.

The important principle is:

```text
Default → Autoescaping ON
```

Do not disable it unless there is a clear and controlled reason.

---

## 34. Difference Between `safe` and `autoescape off`

These two approaches are related but have different scopes.

### `safe`

```django
{{ value|safe }}
```

Marks one value as safe.

### `autoescape off`

```django
{% autoescape off %}
    {{ value }}
{% endautoescape %}
```

Disables automatic escaping for the template block.

In general, using `safe` on a specific trusted value is more targeted than disabling autoescaping for a larger section.

---

## 35. Complete Template Example

A simple template combining the concepts can look like this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Template Control Flow</title>
</head>

<body>

    <h1>Blog List</h1>

    <h2>If-Else</h2>

    {% if blogs.0.is_featured %}
        <p>Featured Blog: {{ blogs.0.title }}</p>
    {% else %}
        <p>No Featured Blog</p>
    {% endif %}

    <hr>

    <h2>For Loop</h2>

    <ul>
        {% for blog in blogs %}
            <li>
                {{ forloop.counter }}.
                {{ blog.title }}
                - {{ blog.author }}
            </li>
        {% empty %}
            <li>No blogs available.</li>
        {% endfor %}
    </ul>

    <hr>

    <h2>With</h2>

    {% with total=blogs|length %}
        <p>Total Blogs: {{ total }}</p>
    {% endwith %}

    <hr>

    <h2>Cycle</h2>

    <table border="1">
        {% for blog in blogs %}
            <tr style="background-color: {% cycle 'lightblue' 'lightgreen' %};">
                <td>{{ forloop.counter }}</td>
                <td>{{ blog.title }}</td>
                <td>{{ blog.author }}</td>
            </tr>
        {% endfor %}
    </table>

    <hr>

    <h2>Firstof</h2>

    <p>
        Author:
        {% firstof blogs.2.author "Anonymous" %}
    </p>

    <hr>

    <h2>Current Date</h2>

    <p>
        {% now "d M Y" %}
    </p>

    <hr>

    <h2>Verbatim</h2>

    {% verbatim %}
        {{ blog.title }}
    {% endverbatim %}

    <hr>

    <h2>Autoescape</h2>

    <p>Default:</p>
    <p>{{ html_code }}</p>

    <p>Trusted HTML:</p>
    <p>{{ html_code|safe }}</p>

</body>
</html>
```

---

## 36. Complete Request-Response Flow

The complete process is:

```text
Browser requests /blog/
        ↓
Project urls.py
        ↓
blog/urls.py
        ↓
blog_list view
        ↓
Create context
        ↓
render()
        ↓
blog_list.html
        ↓
Django processes template tags
        ↓
if / for / with / cycle / firstof / now
        ↓
Autoescaping is applied
        ↓
HTML response
        ↓
Browser
```

---

## 37. Common Mistakes

### Wrong view name

If the view is:

```python
def blog_list(request):
```

the URL should reference:

```python
views.blog_list
```

not a different function name.

### Forgetting closing tags

Started:

```django
{% if condition %}
```

must end with:

```django
{% endif %}
```

Started:

```django
{% for blog in blogs %}
```

must end with:

```django
{% endfor %}
```

Started:

```django
{% with total=blogs|length %}
```

must end with:

```django
{% endwith %}
```

---

## 38. Common Template Tag Closings

| Opening tag | Closing tag |
| --- | --- |
| `{% if %}` | `{% endif %}` |
| `{% for %}` | `{% endfor %}` |
| `{% with %}` | `{% endwith %}` |
| `{% verbatim %}` | `{% endverbatim %}` |
| `{% autoescape %}` | `{% endautoescape %}` |

`else` and `elif` do not have their own closing tags.

They are part of the `if` block.

---

## 39. Quick Revision Table

| Tag | Main Purpose |
| --- | --- |
| `if` | Conditional logic |
| `elif` | Additional condition |
| `else` | Alternative condition |
| `for` | Iterate over data |
| `empty` | Handle an empty collection |
| `with` | Store an expression in a local variable |
| `cycle` | Alternate between values |
| `firstof` | Display first usable value |
| `now` | Display current date/time |
| `verbatim` | Prevent normal template parsing |
| `autoescape` | Control automatic HTML escaping |

---

## 40. Important Examples for Revision

### If-Else

```django
{% if blog.is_featured %}
    Featured
{% else %}
    Not Featured
{% endif %}
```

### For Loop

```django
{% for blog in blogs %}
    {{ blog.title }}
{% endfor %}
```

### Empty

```django
{% for blog in blogs %}
    {{ blog.title }}
{% empty %}
    No blogs available.
{% endfor %}
```

### With

```django
{% with total=blogs|length %}
    {{ total }}
{% endwith %}
```

### Cycle

```django
{% cycle "lightblue" "lightgreen" %}
```

### Firstof

```django
{% firstof blog.author "Anonymous" %}
```

### Now

```django
{% now "d M Y" %}
```

### Verbatim

```django
{% verbatim %}
    {{ blog.title }}
{% endverbatim %}
```

### Autoescape

```django
{% autoescape off %}
    {{ html_code }}
{% endautoescape %}
```

---

## 41. Interview Questions

### Q1. What is the purpose of the `if` tag?

It is used to conditionally display content in a Django template.

### Q2. How do you write an `else` block?

```django
{% else %}
```

inside an `if` block.

### Q3. How do you close an `if` block?

```django
{% endif %}
```

### Q4. How do you iterate over a list?

Using the `for` tag:

```django
{% for item in items %}
    {{ item }}
{% endfor %}
```

### Q5. What is the purpose of `empty`?

It displays fallback content when the collection being iterated over contains no items.

### Q6. What does `forloop.counter` return?

It returns the current loop iteration starting from `1`.

### Q7. What is the difference between `forloop.counter` and `forloop.counter0`?

```text
counter  → starts at 1
counter0 → starts at 0
```

### Q8. What is the purpose of `with`?

It stores an expression in a local template variable.

### Q9. What is `cycle` used for?

It alternates between specified values, such as alternating table row colors.

### Q10. What does `firstof` do?

It displays the first variable from the supplied list that has a usable value.

### Q11. What does the `now` tag do?

It displays the current date and/or time according to the specified format.

### Q12. What is the purpose of `verbatim`?

It prevents Django from interpreting template syntax inside the block.

### Q13. Is autoescaping enabled by default?

Yes. Django templates normally enable automatic HTML escaping.

### Q14. Why is autoescaping important?

It helps prevent untrusted HTML from being interpreted as executable HTML/JavaScript and reduces XSS risk.

### Q15. What does the `safe` filter do?

It marks a value as safe HTML so Django does not escape it in the normal way.

### Q16. Why should `safe` be used carefully?

Because marking untrusted input as safe can allow malicious HTML or JavaScript to be rendered.

---

## 42. Key Takeaways

- Django templates support basic control flow through template tags.
- `if`, `elif`, and `else` handle conditions.
- `for` is used to iterate over collections.
- `empty` provides fallback content for empty collections.
- `forloop.counter` starts from `1`.
- `with` creates a convenient local variable.
- `cycle` can alternate values, such as table row styles.
- `firstof` provides fallback values.
- `now` displays the current date/time.
- `verbatim` prevents Django from processing template syntax inside its block.
- Django normally enables autoescaping by default.
- `safe` should only be used with trusted HTML.
- `autoescape off` should be used very carefully because it can introduce security risks.
- Proper closing tags are essential for block-based template tags.

---
