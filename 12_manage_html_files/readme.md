# Chapter 12 - Django Template Inheritance and Connecting Project Templates with App Templates

## 1. Introduction

In the previous chapter, we learned how to create templates inside individual Django apps.

In this chapter, we will learn how to connect the **main project-level `base.html` template** with templates inside our apps.

The main purpose is to:

- Reuse common HTML code
- Avoid repeating the same HTML structure
- Create dynamic titles and content
- Keep common HTML in one place
- Allow different apps to use the same base layout

This concept is called **Django Template Inheritance**.

---

## 2. Why Do We Need Template Inheritance?

Suppose we have two apps:

```text
blog
shop
```

Without template inheritance, both pages might contain the same HTML structure:

```html
<!DOCTYPE html>
<html>
<head>
    <title>...</title>
</head>
<body>

    <h1>Welcome to My Project</h1>

    ...

</body>
</html>
```

The same code would have to be written in multiple templates.

For example:

```text
blog/post_list.html
shop/product_list.html
```

Both may contain:

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

This creates unnecessary **code repetition**.

---

## 3. The Solution: `base.html`

Instead of writing the common HTML structure in every template, we create one common template:

```text
templates/
└── base.html
```

Then individual app templates can **extend** this template.

The structure becomes:

```text
base.html
    ↓
    ├── blog/post_list.html
    └── shop/product_list.html
```

The common HTML remains inside `base.html`.

Each app only provides the content that is different.

---

## 4. What Is Template Inheritance?

Template inheritance allows one template to use the structure of another template.

The parent template contains the common structure.

For example:

```text
base.html
```

is the parent template.

The child templates are:

```text
blog/post_list.html
shop/product_list.html
```

The child templates extend the parent:

```django
{% extends "base.html" %}
```

This allows us to reuse the HTML structure defined in `base.html`.

---

## 5. Create the Base Template

Our project-level template should be located at:

```text
templates/base.html
```

The `templates` folder should be at the project root/base directory:

```text
myproject4/
├── blog/
├── shop/
├── myproject4/
├── templates/
│   └── base.html
└── manage.py
```

It should **not** be placed inside the inner project configuration directory if we are using:

```python
"DIRS": [BASE_DIR / "templates"]
```

---

## 6. Configure the Project-Level Templates Directory

In:

```text
myproject4/settings.py
```

make sure the `TEMPLATES` configuration contains:

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

```python
"DIRS": [BASE_DIR / "templates"]
```

allows Django to search the project-level `templates` directory.

And:

```python
"APP_DIRS": True
```

allows Django to search templates inside installed applications.

---

## 7. Create a Dynamic Title Block

Open:

```text
templates/base.html
```

Instead of keeping the title completely static, we can create a dynamic block.

Example:

```html
<!DOCTYPE html>
<html>
<head>

    <title>
        {% block title %}
        My Django Project
        {% endblock %}
    </title>

</head>
<body>

    <h1>Welcome to My Project</h1>

</body>
</html>
```

The important part is:

```django
{% block title %}
My Django Project
{% endblock %}
```

---

## 8. Understanding `{% block title %}`

A Django block creates a section that a child template can override.

For example:

```django
{% block title %}
My Django Project
{% endblock %}
```

means:

> The child template can provide its own content for this section.

The child template can write:

```django
{% block title %}
Blog Post
{% endblock %}
```

Then the browser will receive:

```html
<title>Blog Post</title>
```

Instead of:

```html
<title>My Django Project</title>
```

---

## 9. Create a Dynamic Content Block

We can also make the main page content dynamic.

Inside `base.html`:

```html
<body>

    <h1>Welcome to My Project</h1>

    <hr>

    {% block content %}
    {% endblock %}

</body>
```

The important part is:

```django
{% block content %}
{% endblock %}
```

This creates a dynamic content area.

Different app templates can put their own content inside this block.

---

## 10. Complete `base.html`

A simple `base.html` can look like:

```html
<!DOCTYPE html>
<html>
<head>

    <title>
        {% block title %}
        My Django Project
        {% endblock %}
    </title>

</head>
<body>

    <h1>Welcome to My Project</h1>

    <hr>

    {% block content %}
    {% endblock %}

</body>
</html>
```

Here:

- `title` → Dynamic page title
- `content` → Dynamic page content
- Everything outside these blocks → Common HTML

---

## 11. Update the Blog Template

Open:

```text
blog/templates/blog/post_list.html
```

We no longer need to repeat:

```html
<!DOCTYPE html>
<html>
<head>
...
</head>
<body>
...
</body>
</html>
```

Instead, use:

```django
{% extends "base.html" %}

{% block title %}
Blog Post
{% endblock %}

{% block content %}

    <h1>Blog Post</h1>
    <p>Here is the latest blog post.</p>

{% endblock %}
```

---

## 12. Understanding `{% extends "base.html" %}`

This line:

```django
{% extends "base.html" %}
```

tells Django:

> This template should inherit the structure of `base.html`.

The child template can then override the blocks defined in the parent.

For example:

```django
{% extends "base.html" %}
```

followed by:

```django
{% block title %}
Blog Post
{% endblock %}
```

means that the `title` block from `base.html` will be replaced with:

```text
Blog Post
```

---

## 13. Understanding the Blog Content Block

The blog template contains:

```django
{% block content %}

    <h1>Blog Post</h1>
    <p>Here is the latest blog post.</p>

{% endblock %}
```

Everything between:

```django
{% block content %}
```

and:

```django
{% endblock %}
```

will be inserted into the `content` block of `base.html`.

Therefore, the final page contains:

```text
Welcome to My Project
---------------------

Blog Post
Here is the latest blog post.
```

---

## 14. Update the Shop Template

Open:

```text
shop/templates/shop/product_list.html
```

Replace the repeated HTML structure with:

```django
{% extends "base.html" %}

{% block title %}
Shop Products
{% endblock %}

{% block content %}

    <h1>Shop Products</h1>
    <p>Shop product listing page.</p>

{% endblock %}
```

Now the shop page also uses the same `base.html`.

---

## 15. How the Shop Template Works

The shop template contains:

```django
{% extends "base.html" %}
```

So Django first uses the structure from:

```text
base.html
```

Then it replaces the:

```django
{% block title %}
```

with:

```text
Shop Products
```

And it replaces:

```django
{% block content %}
```

with:

```html
<h1>Shop Products</h1>
<p>Shop product listing page.</p>
```

---

## 16. Dynamic Title Example

The base template contains:

```django
<title>
    {% block title %}
    My Django Project
    {% endblock %}
</title>
```

The blog template contains:

```django
{% block title %}
Blog Post
{% endblock %}
```

Therefore:

```text
/blog/
```

can have the title:

```text
Blog Post
```

The shop template contains:

```django
{% block title %}
Shop Products
{% endblock %}
```

Therefore:

```text
/shop/
```

can have the title:

```text
Shop Products
```

The common HTML structure remains the same.

---

## 17. Dynamic Content Example

The base template contains:

```django
{% block content %}
{% endblock %}
```

The blog template provides:

```django
{% block content %}

    <h1>Blog Post</h1>
    <p>Here is the latest blog post.</p>

{% endblock %}
```

The shop template provides:

```django
{% block content %}

    <h1>Shop Products</h1>
    <p>Shop product listing page.</p>

{% endblock %}
```

Therefore, the same base template can display different content depending on the app.

---

## 18. What Does `{% endblock %}` Mean?

Every block should be closed using:

```django
{% endblock %}
```

For example:

```django
{% block title %}
Blog Post
{% endblock %}
```

Here:

```django
{% block title %}
```

starts the block.

And:

```django
{% endblock %}
```

ends the block.

Similarly:

```django
{% block content %}
...
{% endblock %}
```

defines the beginning and end of the content block.

---

## 19. Parent and Child Template Relationship

The relationship can be visualized as:

```text
                 base.html
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
blog/post_list.html    shop/product_list.html
          │                     │
          ▼                     ▼
      Blog Content          Shop Content
```

The parent template provides the common layout.

The child templates provide app-specific content.

---

## 20. Error: `TemplateDoesNotExist`

While testing the shop page, you may see an error such as:

```text
TemplateDoesNotExist
```

For example:

```text
base.html
```

may not be found.

This usually means Django cannot locate the parent template.

---

## 21. Why `base.html` May Not Be Found

Suppose your structure is:

```text
myproject4/
├── myproject4/
│   ├── settings.py
│   └── urls.py
│
├── blog/
├── shop/
├── templates/
└── manage.py
```

The `templates` folder is at the project root.

If your settings contain:

```python
"DIRS": [BASE_DIR / "templates"],
```

Django searches:

```text
BASE_DIR/templates/
```

for:

```text
base.html
```

---

## 22. Incorrect Template Location

An incorrect structure could be:

```text
myproject4/
├── myproject4/
│   ├── settings.py
│   ├── urls.py
│   └── templates/
│       └── base.html
```

If the configuration expects:

```text
BASE_DIR/templates/
```

but `base.html` is somewhere else, Django may not find it.

---

## 23. Correct Template Location

The recommended project-level structure for this setup is:

```text
myproject4/
├── blog/
├── shop/
├── myproject4/
├── templates/
│   └── base.html
└── manage.py
```

The `templates` folder is alongside:

```text
manage.py
```

This matches:

```python
"DIRS": [BASE_DIR / "templates"],
```

---

## 24. Important Error-Handling Lesson

When Django shows an error such as:

```text
TemplateDoesNotExist
```

do not simply ignore the error.

Read the error message carefully.

It can tell you:

- Which template Django was trying to find
- Where Django searched
- Which template path is incorrect
- Which configuration may need to be changed

Understanding Django errors is an important development skill.

---

## 25. How Django Combines the Templates

Suppose `base.html` contains:

```html
<!DOCTYPE html>
<html>
<head>
    <title>
        {% block title %}
        My Django Project
        {% endblock %}
    </title>
</head>

<body>

    <h1>Welcome to My Project</h1>

    <hr>

    {% block content %}
    {% endblock %}

</body>
</html>
```

And the blog template contains:

```django
{% extends "base.html" %}

{% block title %}
Blog Post
{% endblock %}

{% block content %}
<h1>Blog Post</h1>
<p>Here is the latest blog post.</p>
{% endblock %}
```

Django combines them logically into a final HTML page.

Conceptually:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog Post</title>
</head>

<body>

    <h1>Welcome to My Project</h1>

    <hr>

    <h1>Blog Post</h1>
    <p>Here is the latest blog post.</p>

</body>
</html>
```

You do not need to manually write this combined HTML.

Django's template engine handles the inheritance.

---

## 26. Same Base Template for Multiple Apps

One `base.html` can be reused by multiple applications.

For example:

```text
base.html
   │
   ├── blog/post_list.html
   │
   ├── shop/product_list.html
   │
   └── accounts/profile.html
```

All of these templates can contain:

```django
{% extends "base.html" %}
```

Each application can then provide its own:

```django
{% block title %}
```

and:

```django
{% block content %}
```

---

## 27. Benefits of Template Inheritance

### 1. Code Reusability

Write common HTML once.

### 2. Less Repetition

You don't need to repeat:

```html
<html>
<head>
<body>
```

in every template.

### 3. Easy Maintenance

If you change the common layout in:

```text
base.html
```

the change can apply to all templates that extend it.

### 4. Consistent UI

All pages can follow the same basic layout.

### 5. Cleaner Templates

Child templates contain mostly page-specific content.

---

## 28. Complete Project Structure

After completing this chapter:

```text
myproject4/
│
├── blog/
│   ├── migrations/
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

## 29. Complete `base.html`

```html
<!DOCTYPE html>
<html>
<head>

    <title>
        {% block title %}
        My Django Project
        {% endblock %}
    </title>

</head>
<body>

    <h1>Welcome to My Project</h1>

    <hr>

    {% block content %}
    {% endblock %}

</body>
</html>
```

---

## 30. Complete Blog Template

File:

```text
blog/templates/blog/post_list.html
```

Code:

```django
{% extends "base.html" %}

{% block title %}
Blog Post
{% endblock %}

{% block content %}

    <h1>Blog Post</h1>
    <p>Here is the latest blog post.</p>

{% endblock %}
```

---

## 31. Complete Shop Template

File:

```text
shop/templates/shop/product_list.html
```

Code:

```django
{% extends "base.html" %}

{% block title %}
Shop Products
{% endblock %}

{% block content %}

    <h1>Shop Products</h1>
    <p>Shop product listing page.</p>

{% endblock %}
```

---

## 32. Important Django Template Tags

| Template Tag | Purpose |
| --- | --- |
| `{% extends "base.html" %}` | Inherits from another template |
| `{% block title %}` | Defines/overrides the title block |
| `{% block content %}` | Defines/overrides the content block |
| `{% endblock %}` | Ends a block |

---

## 33. Important Syntax to Remember

### Extending a Template

```django
{% extends "base.html" %}
```

### Creating a Block

```django
{% block content %}
{% endblock %}
```

### Creating a Title Block

```django
{% block title %}
Blog Post
{% endblock %}
```

### Creating a Content Block

```django
{% block content %}
<h1>Blog Post</h1>
<p>Latest blog post.</p>
{% endblock %}
```

---

## 34. Complete Flow

The complete template inheritance flow is:

```text
Browser
   ↓
Django URL
   ↓
App URL
   ↓
View
   ↓
Child Template
   ↓
{% extends "base.html" %}
   ↓
Django finds base.html
   ↓
Base template provides common structure
   ↓
Child template fills/overrides blocks
   ↓
Final HTML
   ↓
Browser
```

---

## 35. Quick Revision Table

| Concept | Meaning |
| --- | --- |
| `base.html` | Common parent template |
| Child template | Template that extends `base.html` |
| `{% extends %}` | Inherits another template |
| `{% block %}` | Defines replaceable content |
| `{% endblock %}` | Ends a block |
| `title` block | Allows dynamic page titles |
| `content` block | Allows dynamic page content |
| `DIRS` | Project-level template directory configuration |
| `APP_DIRS` | Searches installed apps for templates |
| Template inheritance | Reuses common template structure |

---

## 36. Key Takeaways

- Template inheritance prevents repeated HTML code.
- `base.html` acts as the common parent template.
- Child templates use:

```django
{% extends "base.html" %}
```

- Dynamic sections are created using:

```django
{% block ... %}
```

- Blocks are closed using:

```django
{% endblock %}
```

- A single `base.html` can be shared by multiple apps.
- Common HTML stays in `base.html`.
- App-specific HTML goes inside the child template.
- `DIRS` must correctly point to the project-level templates directory.
- The project-level `templates` folder should be placed according to the configured `BASE_DIR`.
- `TemplateDoesNotExist` errors should be investigated by checking the template path and template configuration.

---

## 37. What's Next

Now that we know how to connect a common `base.html` with multiple app templates, we can go deeper into Django Template Language.

The next concepts can include:

- More template tags
- Template variables
- Dynamic data
- Conditional statements
- Loops
- Filters
- Static files
- Reusable template components
