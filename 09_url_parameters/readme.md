# Chapter 09 - URL Parameters and Dynamic URL Routing in Django

## 1. Introduction

In Django, **URL Parameters** are used to create **dynamic URLs**.

A dynamic URL is a URL whose value can change depending on the data being requested.

For example:

```text
/blog/1/
/blog/2/
/blog/3/
```

Here, the `/blog/` part is fixed, while `1`, `2`, and `3` are dynamic values.

Another example:

```text
/product/mobile/iphone/
```

Here, `mobile` and `iphone` can represent dynamic information.

Django provides different ways to work with URL parameters:

1. **`path()`**
2. **`re_path()`** — Regex-based URL matching
3. **`**kwargs`** — Keyword arguments for handling multiple parameters

---

## 2. What Are URL Parameters?

URL parameters allow us to pass dynamic values through the URL to a Django view.

For example:

```text
/blog/5/
```

Here:

- `/blog/` → static part
- `5` → dynamic parameter
- `5` can represent a post ID

So instead of creating separate URLs like:

```text
/blog/1/
/blog/2/
/blog/3/
/blog/4/
```

we can create one dynamic URL:

```text
/blog/<int:post_id>/
```

This single pattern can handle many different IDs.

---

## 3. Why Do We Need Dynamic URLs?

Dynamic URLs are useful when the application contains many similar resources.

For example, a blog may contain:

```text
/blog/1/
/blog/2/
/blog/3/
/blog/4/
```

Each URL can represent a different blog post.

Similarly, an application may have user profiles:

```text
/user/mohit/
/user/rohit/
/user/amit/
```

The username changes dynamically.

This makes URL routing:

- Flexible
- Reusable
- Scalable
- Easier to maintain

---

## 4. Project Setup

For this chapter, create a new Django project.

Create the project:

```bash
django-admin startproject myproject2
```

Move inside the project directory:

```bash
cd myproject2
```

Create the `blog` application:

```bash
python manage.py startapp blog
```

On macOS/Linux:

```bash
python3 manage.py startapp blog
```

---

## 5. Register the App

Open:

```text
myproject2/settings.py
```

Find:

```python
INSTALLED_APPS = [
    ...
]
```

Add the `blog` application:

```python
INSTALLED_APPS = [
    ...
    "blog",
]
```

### Important

Registering the app is an important part of Django application integration.

It is needed for features such as:

- Models
- Migrations
- App configuration
- Template/static discovery in normal Django app usage

However, **URL routing itself does not depend on the app being registered in `INSTALLED_APPS`**.

---

## 6. Creating Views with URL Parameters

Open:

```text
blog/views.py
```

Import `HttpResponse`:

```python
from django.http import HttpResponse
```

Now create a view for displaying a post.

```python
from django.http import HttpResponse


def post_details(request, post_id):
    return HttpResponse(
        f"<h1>Show Blog Post: {post_id}</h1>"
    )
```

Here:

- `request` → Django request object
- `post_id` → value received from the URL
- `post_id` can contain an integer because we will define it as an integer in the URL pattern

For example:

```text
/blog/post/5/
```

The value `5` will be passed to:

```python
post_id
```

---

## 7. Creating a User Profile View

We can also pass a string parameter such as a username.

Add another view:

```python
def user_profile(request, username):
    return HttpResponse(
        f"<h1>Profile of User: {username}</h1>"
    )
```

Here:

```python
username
```

will receive the username from the URL.

For example:

```text
/user/mohit/
```

will pass:

```text
mohit
```

to the `username` parameter.

---

## 8. Creating the App-Level `urls.py`

Django does not automatically create a `urls.py` file inside every new app.

Create:

```text
blog/urls.py
```

Add:

```python
from django.urls import path
from . import views


urlpatterns = [
    path(
        "post/<int:post_id>/",
        views.post_details,
        name="post-details"
    ),

    path(
        "user/<str:username>/",
        views.user_profile,
        name="user-profile"
    ),
]
```

---

## 9. Understanding `<int:post_id>`

This is the important part:

```python
<int:post_id>
```

It consists of two parts:

```text
<int:post_id>
     │
     └── Parameter name
```

### `int`

`int` tells Django that the parameter must be an integer.

Examples:

```text
1
5
10
100
```

### `post_id`

This is the name of the parameter that will be passed to the view.

Therefore:

```python
<int:post_id>
```

means:

> Capture an integer from the URL and pass it to the view using the name `post_id`.

---

## 10. Understanding `<str:username>`

Similarly:

```python
<str:username>
```

means:

> Capture a string from the URL and pass it to the view using the name `username`.

For example:

```text
/user/mohit/
```

The view receives:

```python
username = "mohit"
```

Another example:

```text
/user/rohit/
```

The view receives:

```python
username = "rohit"
```

---

## 11. Common Django Path Converters

Django provides several path converters.

| Converter | Purpose | Example |
| --- | --- | --- |
| `int` | Matches integers | `<int:id>` |
| `str` | Matches non-empty strings excluding `/` | `<str:name>` |
| `slug` | Matches slug strings | `<slug:post>` |
| `uuid` | Matches UUID values | `<uuid:id>` |
| `path` | Matches a path including `/` | `<path:value>` |

Examples:

```python
<int:id>
```

```python
<str:username>
```

```python
<slug:slug>
```

```python
<uuid:id>
```

```python
<path:filepath>
```

The converter helps Django determine what type of value should be accepted from the URL.

---

## 12. Connecting App URLs to Project URLs

Now open the main project URL configuration:

```text
myproject2/urls.py
```

Import `include`:

```python
from django.urls import include, path
```

Then includ#e the blog URL configuration:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
```

---

## 13. Understanding `include()`

This line:

```python
path("blog/", include("blog.urls")),
```

means:

> Whenever the URL starts with `/blog/`, Django should continue checking the URL patterns inside `blog/urls.py`.

For example:

```text
/blog/post/5/
```

Django first matches:

```text
/blog/
```

Then it passes the remaining part:

```text
post/5/
```

to:

```text
blog/urls.py
```

There Django matches:

```python
path("post/<int:post_id>/", ...)
```

So the final view receives:

```python
post_id = 5
```

---

## 14. Complete URL Flow

The complete flow looks like this:

```text
Browser
   │
   ▼
/blog/post/5/
   │
   ▼
Project urls.py
   │
   │ path("blog/", include("blog.urls"))
   ▼
blog/urls.py
   │
   │ post/<int:post_id>/
   ▼
views.post_details
   │
   ▼
post_id = 5
   │
   ▼
HttpResponse
   │
   ▼
Browser
```

---

## 15. Testing the Integer Parameter

Start the Django development server:

```bash
python manage.py runserver
```

Or:

```bash
python3 manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/blog/post/5/
```

The output will be:

```text
Show Blog Post: 5
```

You can change the ID:

```text
/blog/post/10/
```

Output:

```text
Show Blog Post: 10
```

Or:

```text
/blog/post/67/
```

Output:

```text
Show Blog Post: 67
```

The same URL pattern handles all these values.

---

## 16. Testing the String Parameter

For the user profile URL:

```text
http://127.0.0.1:8000/blog/user/mohit/
```

Output:

```text
Profile of User: mohit
```

Another example:

```text
/blog/user/rohit/
```

Output:

```text
Profile of User: rohit
```

The username is dynamically received from the URL.

---

## 17. What Happens with an Invalid Parameter?

Because we used:

```python
<int:post_id>
```

Django expects an integer.

This will work:

```text
/blog/post/5/
```

This will work:

```text
/blog/post/100/
```

But this will not match the pattern:

```text
/blog/post/abc/
```

because:

```text
abc
```

is not an integer.

Similarly, the string converter:

```python
<str:username>
```

is designed to capture a non-empty string segment.

---

## 18. Multiple URL Parameters with `path()`

Django can handle multiple parameters in the same URL.

For example, suppose we want:

```text
/articles/2024/2/
```

where:

- `2024` → year
- `2` → month

Create a view:

```python
def article_details(request, year, month):
    return HttpResponse(
        f"<h1>Article: {year}, Month: {month}</h1>"
    )
```

Then create the URL pattern:

```python
path(
    "articles/<int:year>/<int:month>/",
    views.article_details,
    name="article-details"
),
```

Now:

```text
/articles/2024/2/
```

will send:

```python
year = 2024
month = 2
```

to the view.

---

## 19. Multiple Parameters Do Not Require `kwargs`

An important point:

You can handle multiple URL parameters directly using normal function parameters.

Example:

```python
def article_details(request, year, month):
    ...
```

with:

```python
path(
    "articles/<int:year>/<int:month>/",
    views.article_details,
    name="article-details"
)
```

So `path()` is already capable of handling multiple parameters.

---

## 20. What Is `re_path()`?

Django also provides:

```python
re_path()
```

`re_path()` allows URL matching using **regular expressions (Regex)**.

Regex stands for:

> Regular Expression

Regular expressions are patterns used to match strings.

They are useful when the URL pattern is more complex than what Django's normal path converters can conveniently express.

Import it using:

```python
from django.urls import re_path
```

---

## 21. Why Use `re_path()`?

Suppose we want a URL containing a four-digit year.

For example:

```text
/articles/2024
/articles/2025
/articles/2026
```

We can create a regular expression that accepts exactly four digits.

Example:

```python
re_path(
    r"^articles/(?P<year>[0-9]{4})/$",
    views.articles_by_year,
    name="articles-by-year"
)
```

The important part is:

```text
[0-9]{4}
```

It means:

> Match exactly four digits from `0` to `9`.

Therefore:

```text
2024
2025
1999
```

can match.

But:

```text
24
202
20245
```

will not match this four-digit pattern.

---

## 22. Understanding Regex Symbols

Consider:

```python
r"^articles/(?P<year>[0-9]{4})/$"
```

### `r`

```python
r"..."
```

creates a Python raw string, which is useful for writing regular expressions.

### `^`

```text
^
```

means the beginning of the string.

### `articles/`

This is the static part of the URL.

### `(?P<year>...)`

This creates a **named capture group**.

The captured value is passed to the view using the name:

```text
year
```

### `[0-9]`

Matches a digit from:

```text
0 to 9
```

### `{4}`

Means exactly four occurrences.

Therefore:

```text
[0-9]{4}
```

means:

```text
Exactly four digits
```

### `$`

```text
$
```

means the end of the string.

---

## 23. `re_path()` Example

In `views.py`:

```python
def articles_by_year(request, year):
    return HttpResponse(
        f"<h1>Articles of Year: {year}</h1>"
    )
```

In `blog/urls.py`:

```python
from django.urls import path, re_path
from . import views


urlpatterns = [
    path(
        "post/<int:post_id>/",
        views.post_details,
        name="post-details"
    ),

    path(
        "user/<str:username>/",
        views.user_profile,
        name="user-profile"
    ),

    re_path(
        r"^articles/(?P<year>[0-9]{4})/$",
        views.articles_by_year,
        name="articles-by-year"
    ),
]
```

Now:

```text
/blog/articles/2024/
```

can match the regex pattern.

The view receives:

```python
year = 2024
```

---

## 24. `path()` vs `re_path()`

### Defining URL Structure with `path()`

Use `path()` for normal URL patterns.

Example:

```python
path(
    "post/<int:post_id>/",
    views.post_details
)
```

It is:

- Simple
- Readable
- Easy to maintain
- Usually preferred for normal Django URLs

### `re_path()`

Use `re_path()` when you need more complex pattern matching.

Example:

```python
re_path(
    r"^articles/(?P<year>[0-9]{4})/$",
    views.articles_by_year
)
```

It provides more control through regular expressions.

---

## 25. What Are `*args` and `**kwargs`?

`*args` and `**kwargs` are Python features.

They are **not Django-specific features**.

`**kwargs` means:

> Keyword arguments

It allows a function to receive multiple keyword arguments.

Example:

```python
def show(**kwargs):
    print(kwargs)
```

Calling:

```python
show(name="Mohit", age=28, city="Delhi")
```

produces a dictionary-like result:

```python
{
    "name": "Mohit",
    "age": 28,
    "city": "Delhi"
}
```

---

## 26. Why Is `**kwargs` Useful in Django?

`**kwargs` can be useful when a view needs to handle a flexible number of keyword parameters.

For example:

```python
def article_details(request, **kwargs):
    return HttpResponse(
        f"<h1>Data: {kwargs}</h1>"
    )
```

If the URL routing provides named parameters, Django can pass them as keyword arguments.

For example:

```python
path(
    "article/<int:year>/<int:month>/",
    views.article_details
)
```

The view can receive the values through:

```python
kwargs
```

Conceptually:

```python
{
    "year": 2024,
    "month": 2
}
```

---

## 27. Example of `**kwargs` in a Django View

```python
def article_details(request, **kwargs):
    return HttpResponse(
        f"<h1>Data: {kwargs}</h1>"
    )
```

With a URL such as:

```text
/article/2024/2/
```

the keyword arguments can represent:

```python
{
    "year": 2024,
    "month": 2
}
```

You can then access individual values:

```python
year = kwargs.get("year")
month = kwargs.get("month")
```

---

## 28. `path()` vs `**kwargs`

These are not really competing features.

They solve different parts of the problem.

### `path()`

Defines the URL structure:

```python
path(
    "article/<int:year>/<int:month>/",
    views.article_details
)
```

### `**kwargs`

Provides a flexible way for the view to receive named parameters:

```python
def article_details(request, **kwargs):
    ...
```

So:

```text
URL
 ↓
path()
 ↓
named parameters
 ↓
view
 ↓
**kwargs
```

---

## 29. Flexible Multiple Parameters

Suppose a URL contains:

```text
/article/2024/2/30/
```

You could define:

```python
path(
    "article/<int:year>/<int:month>/<int:day>/",
    views.article_details
)
```

with:

```python
def article_details(request, year, month, day):
    ...
```

This works, but every parameter has to be explicitly added.

With `**kwargs`, the view can be more flexible:

```python
def article_details(request, **kwargs):
    return HttpResponse(
        f"<h1>Data: {kwargs}</h1>"
    )
```

The route can provide named parameters and Django passes them as keyword arguments.

---

## 30. Complete Example

## `blog/views.py`

```python
from django.http import HttpResponse


def post_details(request, post_id):
    return HttpResponse(
        f"<h1>Show Blog Post: {post_id}</h1>"
    )


def user_profile(request, username):
    return HttpResponse(
        f"<h1>Profile of User: {username}</h1>"
    )


def articles_by_year(request, year):
    return HttpResponse(
        f"<h1>Articles of Year: {year}</h1>"
    )


def article_details(request, **kwargs):
    return HttpResponse(
        f"<h1>Data: {kwargs}</h1>"
    )
```

---

## `blog/urls.py`

```python
from django.urls import path, re_path
from . import views


urlpatterns = [
    path(
        "post/<int:post_id>/",
        views.post_details,
        name="post-details"
    ),

    path(
        "user/<str:username>/",
        views.user_profile,
        name="user-profile"
    ),

    path(
        "article/<int:year>/<int:month>/",
        views.article_details,
        name="article-details"
    ),

    re_path(
        r"^articles/(?P<year>[0-9]{4})/$",
        views.articles_by_year,
        name="articles-by-year"
    ),
]
```

---

## `myproject2/urls.py`

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
```

---

## 31. Example URLs

With the above configuration:

### Post details

```text
/blog/post/5/
```

Output:

```text
Show Blog Post: 5
```

### User profile

```text
/blog/user/mohit/
```

Output:

```text
Profile of User: mohit
```

### Article by year

```text
/blog/articles/2024/
```

Output:

```text
Articles of Year: 2024
```

### Article by year and month

```text
/blog/article/2024/2/
```

Output:

```text
Data: {'year': 2024, 'month': 2}
```

---

## 32. Complete Request Flow

The complete dynamic URL process is:

```text
User enters URL
       │
       ▼
Project urls.py
       │
       │ include("blog.urls")
       ▼
blog/urls.py
       │
       │ Match URL pattern
       ▼
Path converter / Regex
       │
       │ Extract parameter
       ▼
Django View
       │
       │ Receive parameter
       ▼
Business Logic
       │
       ▼
HttpResponse / Template
       │
       ▼
Browser
```

---

## 33. Important Concept: Static vs Dynamic URL

### Static URL

```python
path("about/", views.about)
```

The URL is fixed:

```text
/about/
```

### Dynamic URL

```python
path("post/<int:post_id>/", views.post_details)
```

The URL can change:

```text
/post/1/
/post/2/
/post/3/
/post/100/
```

One URL pattern can handle many values.

---

## 34. Common Mistakes

### 1. Forgetting the parameter in the view

Wrong:

```python
def post_details(request):
    ...
```

while the URL contains:

```python
<int:post_id>
```

Correct:

```python
def post_details(request, post_id):
    ...
```

---

### 2. Parameter names do not match

URL:

```python
path(
    "post/<int:post_id>/",
    views.post_details
)
```

View:

```python
def post_details(request, id):
    ...
```

This is incorrect because the URL parameter is named:

```text
post_id
```

The view should receive:

```python
def post_details(request, post_id):
    ...
```

---

### 3. Forgetting `include()`

If app URLs are defined in:

```text
blog/urls.py
```

they need to be connected to the project's URLconf:

```python
path("blog/", include("blog.urls"))
```

---

### 4. Forgetting to create `urls.py`

Django's `startapp` command does not automatically create:

```text
blog/urls.py
```

You need to create it manually when using app-level URL routing.

---

### 5. Using the wrong parameter type

For:

```python
<int:post_id>
```

this works:

```text
/post/5/
```

but:

```text
/post/abc/
```

does not match.

---

### 6. Forgetting to import `include`

Use:

```python
from django.urls import include, path
```

---

## 35. Important Commands

Create a project:

```bash
django-admin startproject myproject2
```

Move into project:

```bash
cd myproject2
```

Create an app:

```bash
python manage.py startapp blog
```

Run server:

```bash
python manage.py runserver
```

macOS/Linux:

```bash
python3 manage.py runserver
```

---

## 36. Quick Revision Table

| Concept | Purpose | Example |
| --- | --- | --- |
| URL parameter | Creates dynamic URLs | `/post/5/` |
| `path()` | Normal URL routing | `path("post/<int:id>/", ...)` |
| `int` | Integer parameter | `<int:id>` |
| `str` | String parameter | `<str:name>` |
| `slug` | Slug parameter | `<slug:slug>` |
| `uuid` | UUID parameter | `<uuid:id>` |
| `path` converter | Captures path including `/` | `<path:value>` |
| `re_path()` | Regex-based routing | `re_path(...)` |
| Regex | Complex pattern matching | `[0-9]{4}` |
| `include()` | Connects app URLs to project URLs | `include("blog.urls")` |
| `**kwargs` | Flexible keyword arguments | `def view(request, **kwargs)` |

---

## 37. `path()` vs `re_path()` vs `**kwargs`

| Feature | `path()` | `re_path()` | `**kwargs` |
| --- | --- | --- | --- |
| Main purpose | URL routing | Regex URL routing | Receive keyword arguments |
| Django-specific | Yes | Yes | No, Python feature |
| Dynamic URLs | Yes | Yes | Helps views receive values |
| Multiple parameters | Yes | Yes | Yes |
| Regex support | No | Yes | No |
| Simplicity | High | Lower | High |
| Best for | Normal URLs | Complex patterns | Flexible view parameters |

---

## 38. Recommended Approach

For normal Django projects, prefer:

```python
path()
```

with Django's built-in converters:

```python
<int:id>
<str:name>
<slug:slug>
<uuid:id>
<path:value>
```

Use:

```python
re_path()
```

when you genuinely need complex regular-expression matching.

Use:

```python
**kwargs
```

when a view benefits from receiving a flexible collection of named keyword arguments.

---

## 39. Complete Process

```text
1. Create Django project
        ↓
2. Create blog app
        ↓
3. Register blog in INSTALLED_APPS
        ↓
4. Create views
        ↓
5. Add parameters to views
        ↓
6. Create blog/urls.py
        ↓
7. Define dynamic URL patterns
        ↓
8. Use path converters
        ↓
9. Connect blog URLs using include()
        ↓
10. Run development server
        ↓
11. Test dynamic URLs
        ↓
12. Use re_path() for complex patterns
        ↓
13. Use **kwargs for flexible keyword parameters
```

---

## 40. Key Takeaways

- URL parameters are used to create **dynamic URLs**.
- Django's `path()` function supports dynamic URL parameters.
- Path converters specify what type of value a parameter should accept.
- Common converters include `int`, `str`, `slug`, `uuid`, and `path`.
- The parameter name in the URL should match the parameter expected by the view.
- Multiple URL parameters can be handled using `path()`.
- `re_path()` provides regex-based URL matching for more complex patterns.
- `^` represents the beginning of a regex pattern.
- `$` represents the end of a regex pattern.
- `[0-9]{4}` represents exactly four digits.
- `include()` connects an app's URL configuration with the project's URL configuration.
- `**kwargs` is a core Python feature that can be used to receive multiple keyword arguments.
- `path()` is generally preferred for normal Django URL patterns because it is simpler and more readable.

---
