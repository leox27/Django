# Chapter 14 - Django Template Filters

## 1. Introduction

Django Template Filters are used to **modify, format, or process values** before displaying them in a template.

A filter is applied using the pipe symbol `|`.

Example:

```django
{{ post.title|upper }}
```

If `post.title` is:

```text
My Second Templates Post
```

The output becomes:

```text
MY SECOND TEMPLATES POST
```

---

## 2. What We Will Learn

In this chapter, we will learn:

- Text filters
- Number filters
- List filters
- Boolean-related filters
- `yesno`
- `pluralize`
- Date and time filters
- URL encoding
- Float formatting
- Filter chaining
- Common mistakes

---

## 3. Basic Project Setup

Assume the project is named:

```text
myproject6
```

and contains a `blog` app.

The important structure is:

```text
myproject6/
├── manage.py
├── myproject6/
│   ├── settings.py
│   └── urls.py
├── blog/
│   ├── views.py
│   └── urls.py
└── templates/
    └── blog/
        └── blog_details.html
```

---

## 4. Template Directory Configuration

If using a project-level `templates` directory, configure it in `settings.py`:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        # ...
    },
]
```

The template can then be stored at:

```text
templates/blog/blog_details.html
```

---

## 5. Creating the View

The view prepares the data and sends it to the template.

```python
from datetime import datetime
from django.shortcuts import render


def blog_details(request):
    post = {
        "title": "My Second Templates Post",
        "description": "Django is a high-level Python web framework.",
        "author": None,
        "created_at": datetime(2025, 8, 19, 10, 30),
        "comment_count": 5,
        "tags": ["Django", "Python", "Web Development"],
        "price": 100,
        "number": 7,
        "rating": 12.34567,
    }

    return render(
        request,
        "blog/blog_details.html",
        {"post": post}
    )
```

### Important

The context contains a key named `post`.

Therefore, inside the template we can access:

```django
{{ post.title }}
```

```django
{{ post.description }}
```

```django
{{ post.price }}
```

---

## 6. Connecting the View with URLs

In `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_details, name="blog_details"),
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

## 7. Template Filter Syntax

A basic filter has this syntax:

```django
{{ value|filter }}
```

A filter with an argument:

```django
{{ value|filter:argument }}
```

Example:

```django
{{ post.title|upper }}
```

Example with an argument:

```django
{{ post.price|add:5 }}
```

Filters can also be chained:

```django
{{ post.title|lower|truncatechars:20 }}
```

---

## 8. Text Filters

Text filters are useful when working with strings.

Important text filters include:

| Filter | Purpose |
| --- | --- |
| `upper` | Converts text to uppercase |
| `lower` | Converts text to lowercase |
| `capfirst` | Capitalizes the first character |
| `title` | Converts text to title case |
| `truncatechars` | Limits text by characters |
| `truncatewords` | Limits text by words |
| `linebreaks` | Converts line breaks into HTML |

---

## 9. `upper` Filter

The `upper` filter converts text into uppercase.

```django
{{ post.title|upper }}
```

Example:

```text
My Second Templates Post
```

Output:

```text
MY SECOND TEMPLATES POST
```

---

## 10. `lower` Filter

The `lower` filter converts text into lowercase.

```django
{{ post.title|lower }}
```

Output:

```text
my second templates post
```

---

## 11. `capfirst` Filter

The `capfirst` filter capitalizes the **first character** of a string.

```django
{{ post.title|capfirst }}
```

It is different from `title`.

- `capfirst` → first character
- `title` → title-case words

---

## 12. `title` Filter

The `title` filter converts text into title case.

```django
{{ post.title|title }}
```

For example:

```text
django template filters
```

can become:

```text
Django Template Filters
```

---

## 13. `truncatechars` Filter

The `truncatechars` filter limits text based on the number of characters.

```django
{{ post.description|truncatechars:20 }}
```

When the text is longer than the specified limit, Django truncates it and adds an ellipsis.

This is useful for:

- Blog previews
- Product descriptions
- Card components
- Short summaries

---

## 14. `truncatewords` Filter

The `truncatewords` filter limits text based on the number of words.

```django
{{ post.description|truncatewords:2 }}
```

For example:

```text
Django is a high-level Python web framework.
```

may be displayed as a shortened version containing only the requested number of words.

---

## 15. `linebreaks` Filter

The `linebreaks` filter converts line breaks in text into suitable HTML paragraph and line-break markup.

```django
{{ post.description|linebreaks }}
```

It is useful when text stored in a database contains multiple lines.

---

## 16. Number Filters

Django provides filters that can be useful when working with numbers.

Important examples:

- `add`
- `divisibleby`
- `floatformat`

---

## 17. `add` Filter

The `add` filter adds a value to another value.

```django
{{ post.price|add:5 }}
```

If:

```text
price = 100
```

the result is:

```text
105
```

### Important Notings

The filter performs:

```text
100 + 5 = 105
```

It does **not** produce `115`.

---

## 18. `divisibleby` Filter

The `divisibleby` filter checks whether a number is divisible by another number.

Example:

```django
{% if post.number|divisibleby:2 %}
    <p>Number is even.</p>
{% else %}
    <p>Number is odd.</p>
{% endif %}
```

If:

```text
number = 7
```

the output is:

```text
Number is odd.
```

For:

```text
number = 8
```

the output would be:

```text
Number is even.
```

### Important Note

`divisibleby` does **not** perform division.

It performs a divisibility check and returns a boolean result.

---

## 19. List Filters

Django filters can also work with lists.

Important list filters include:

- `first`
- `last`
- `length`
- `slice`
- `join`

Our example list is:

```python
"tags": ["Django", "Python", "Web Development"]
```

---

## 20. `first` and `last` Filters

The `first` filter returns the first item.

```django
{{ post.tags|first }}
```

Output:

```text
Django
```

The `last` filter returns the last item.

```django
{{ post.tags|last }}
```

Output:

```text
Web Development
```

---

## 21. `length` Filter

The `length` filter returns the number of items in a list.

```django
{{ post.tags|length }}
```

For:

```python
["Django", "Python", "Web Development"]
```

the output is:

```text
3
```

It can also be used with strings to get their length.

---

## 22. `slice` Filter

The `slice` filter works similarly to Python slicing.

```django
{{ post.tags|slice:"0:2" }}
```

For:

```python
["Django", "Python", "Web Development"]
```

the first two items are selected.

Conceptually:

```python
post["tags"][0:2]
```

---

## 23. `join` Filter

The `join` filter joins list elements using a separator.

```django
{{ post.tags|join:", " }}
```

Output:

```text
Django, Python, Web Development
```

Another example:

```django
{{ post.tags|join:" " }}
```

Output:

```text
Django Python Web Development
```

---

## 24. `yesno` Filter

The `yesno` filter converts boolean-like values into readable text.

Syntax:

```django
{{ value|yesno:"Yes,No,Maybe" }}
```

Example:

```django
{{ post.author|yesno:"Yes,No,Maybe" }}
```

The mapping is:

| Value | Output |
| --- | --- |
| `True` | `Yes` |
| `False` | `No` |
| `None` | `Maybe` |

This is useful when displaying values such as:

```text
Available: Yes
Published: No
Author provided: Maybe
```

---

## 25. `pluralize` Filter

The `pluralize` filter is useful when displaying counts.

Example:

```django
{{ post.comment_count }} comment{{ post.comment_count|pluralize }}
```

If:

```text
comment_count = 1
```

the output is:

```text
1 comment
```

If:

```text
comment_count = 5
```

the output is:

```text
5 comments
```

This prevents manually writing separate singular and plural messages.

---

## 26. Date and Time Filters

Django provides:

- `date`
- `time`

for formatting date and time values.

Our example contains:

```python
"created_at": datetime(2025, 8, 19, 10, 30)
```

---

## 27. Displaying the Original Date and Time

Without a filter:

```django
{{ post.created_at }}
```

Django displays the datetime according to its normal representation/settings.

Filters allow us to control the displayed format.

---

## 28. `date` Filter

The `date` filter formats a date.

Example:

```django
{{ post.created_at|date:"d M Y" }}
```

Possible output:

```text
19 Aug 2025
```

Another format:

```django
{{ post.created_at|date:"d/m/Y" }}
```

Output:

```text
19/08/2025
```

Common Django date format characters:

| Format | Meaning |
| --- | --- |
| `d` | Day |
| `m` | Month number |
| `M` | Short month name |
| `Y` | Four-digit year |

### Important Notes

Django template date-format characters are Django's own format syntax. They are not exactly the same as Python's `strftime()` syntax.

---

## 29. `time` Filter

The `time` filter formats the time portion.

Example:

```django
{{ post.created_at|time:"H:i" }}
```

Possible output:

```text
10:30
```

Common time format characters:

| Format | Meaning |
| --- | --- |
| `H` | Hour in 24-hour format |
| `i` | Minutes |
| `s` | Seconds |
| `a` | `a.m.` or `p.m.` |

---

## 30. `urlencode` Filter

The `urlencode` filter encodes a value so it can safely be used as part of a URL.

Example:

```django
{{ post.title|urlencode }}
```

For example, spaces and special characters can be percent-encoded.

### Security Notes

`urlencode` is for **URL encoding**.

It is not the same thing as HTML encoding.

---

## 31. `floatformat` Filter

The `floatformat` filter controls the number of decimal places displayed for a floating-point value.

Example data:

```python
"rating": 12.34567
```

Using:

```django
{{ post.rating|floatformat:2 }}
```

produces approximately:

```text
12.35
```

Using:

```django
{{ post.rating|floatformat:3 }}
```

produces:

```text
12.346
```

It is useful for displaying:

- Ratings
- Prices
- Percentages
- Measurements
- Calculated values

---

## 32. Filter Chaining

Multiple filters can be applied to the same value.

Example:

```django
{{ post.title|lower|truncatechars:20 }}
```

The processing happens from left to right:

```text
Original title
      ↓
lower
      ↓
truncatechars
      ↓
Final output
```

Another example:

```django
{{ post.tags|first|upper }}
```

First:

```text
Django
```

Then:

```text
DJANGO
```

### Security Note

The output of one filter becomes the input of the next filter.

---

## 33. Complete Template Example

Create:

```text
templates/blog/blog_details.html
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Template Filters</title>
</head>

<body>

    <h1>Django Template Filters</h1>

    <h2>Text Filters</h2>

    <p>Normal: {{ post.title }}</p>
    <p>Upper: {{ post.title|upper }}</p>
    <p>Lower: {{ post.title|lower }}</p>
    <p>Capfirst: {{ post.title|capfirst }}</p>
    <p>Title: {{ post.title|title }}</p>
    <p>Truncated: {{ post.description|truncatechars:20 }}</p>
    <p>Words: {{ post.description|truncatewords:4 }}</p>
    <p>Line breaks: {{ post.description|linebreaks }}</p>

    <h2>Number Filters</h2>

    <p>Original price: {{ post.price }}</p>
    <p>Price + 5: {{ post.price|add:5 }}</p>

    {% if post.number|divisibleby:2 %}
        <p>Number is even.</p>
    {% else %}
        <p>Number is odd.</p>
    {% endif %}

    <h2>List Filters</h2>

    <p>First tag: {{ post.tags|first }}</p>
    <p>Last tag: {{ post.tags|last }}</p>
    <p>Total tags: {{ post.tags|length }}</p>
    <p>First two: {{ post.tags|slice:"0:2" }}</p>
    <p>Joined: {{ post.tags|join:", " }}</p>

    <h2>Yes/No and Pluralize</h2>

    <p>
        Author available:
        {{ post.author|yesno:"Yes,No,Maybe" }}
    </p>

    <p>
        {{ post.comment_count }}
        comment{{ post.comment_count|pluralize }}
    </p>

    <h2>Date and Time</h2>

    <p>Original: {{ post.created_at }}</p>
    <p>Date: {{ post.created_at|date:"d M Y" }}</p>
    <p>Date: {{ post.created_at|date:"d/m/Y" }}</p>
    <p>Time: {{ post.created_at|time:"H:i" }}</p>

    <h2>URL Encoding</h2>

    <p>{{ post.title|urlencode }}</p>

    <h2>Float Formatting</h2>

    <p>2 decimals: {{ post.rating|floatformat:2 }}</p>
    <p>3 decimals: {{ post.rating|floatformat:3 }}</p>

</body>
</html>
```

---

## 34. Complete Request-Response Flow

The overall flow is:

```text
Browser
   ↓
/blog/
   ↓
Project urls.py
   ↓
include("blog.urls")
   ↓
blog/urls.py
   ↓
views.blog_details
   ↓
Create post dictionary
   ↓
render()
   ↓
blog_details.html
   ↓
Template filters process values
   ↓
HTML response
   ↓
Browser
```

For example:

```text
post.title
   ↓
upper filter
   ↓
MY SECOND TEMPLATES POST
```

---

## 35. Common Errors

### Error 1: Wrong View Name

If the view is:

```python
def blog_details(request):
```

the URL must use:

```python
path("", views.blog_details, name="blog_details")
```

Do not use:

```python
path("", views.home)
```

unless a `home()` function actually exists.

---

### Error 2: Template Does Not Exist

If Django cannot find:

```text
blog/blog_details.html
```

check:

```text
templates/
└── blog/
    └── blog_details.html
```

Also verify:

```python
"DIRS": [BASE_DIR / "templates"]
```

---

### Error 3: Wrong Context Key

If the view sends:

```python
{"post": post}
```

the template should use:

```django
{{ post.title }}
```

Not:

```django
{{ blog.title }}
```

unless the context contains `blog`.

---

### Error 4: Incorrect Filter Argument

Correct:

```django
{{ post.tags|slice:"0:2" }}
```

Correct:

```django
{{ post.price|add:5 }}
```

The syntax is:

```django
{{ value|filter:argument }}
```

---

### Error 5: Using `divisibleby` as Division

This:

```django
{{ post.number|divisibleby:2 }}
```

checks divisibility.

It does not calculate:

```text
number / 2
```

Use it as a condition:

```django
{% if post.number|divisibleby:2 %}
```

---

## 36. Template Filters Quick Revision

| Category | Filter | Purpose |
| --- | --- | --- |
| Text | `upper` | Uppercase |
| Text | `lower` | Lowercase |
| Text | `capfirst` | Capitalize first character |
| Text | `title` | Title case |
| Text | `truncatechars` | Limit characters |
| Text | `truncatewords` | Limit words |
| Text | `linebreaks` | Handle line breaks |
| Number | `add` | Add a value |
| Number | `divisibleby` | Check divisibility |
| Number | `floatformat` | Format decimals |
| List | `first` | First item |
| List | `last` | Last item |
| List | `length` | Number of items/characters |
| List | `slice` | Select a portion |
| List | `join` | Join items |
| Boolean | `yesno` | Convert values to readable text |
| Count | `pluralize` | Singular/plural suffix |
| Date | `date` | Format date |
| Time | `time` | Format time |
| URL | `urlencode` | URL-encode a value |

---

## 37. Important Syntax Patterns

### Filter without argument

```django
{{ value|upper }}
```

### Filter with argument

```django
{{ value|truncatechars:20 }}
```

### Filter with a string argument

```django
{{ value|slice:"0:2" }}
```

### Multiple filters

```django
{{ value|lower|truncatechars:20 }}
```

### Filter inside condition

```django
{% if number|divisibleby:2 %}
    Even
{% endif %}
```

---

## 38. Interview Questions

### Q1. What is a Django template filter?

A template filter modifies or formats a value before displaying it in a Django template.

---

### Q2. Which symbol is used to apply a filter?

The pipe symbol:

```text
|
```

Example:

```django
{{ name|upper }}
```

---

### Q3. What does the `upper` filter do?

It converts text to uppercase.

---

### Q4. What is the difference between `capfirst` and `title`?

`capfirst` capitalizes the first character, while `title` converts text into title case.

---

### Q5. What does `truncatewords` do?

It limits text based on the number of words.

---

### Q6. What does `divisibleby` do?

It checks whether a value is divisible by another value and returns a boolean result.

---

### Q7. What does `join` do?

It combines list elements using a specified separator.

---

### Q8. What does `yesno` do?

It converts `True`, `False`, and `None` into custom display text.

---

### Q9. What is the purpose of `pluralize`?

It helps display singular or plural words based on a count.

---

### Q10. What is filter chaining?

Applying multiple filters to the same value.

Example:

```django
{{ post.title|lower|truncatechars:20 }}
```

---

## 39. Key Takeaways

- Django template filters modify values before displaying them.
- Filters use the `|` symbol.
- Filters can be used with or without arguments.
- Multiple filters can be chained.
- `upper`, `lower`, `capfirst`, and `title` are useful for text.
- `truncatechars` works with characters.
- `truncatewords` works with words.
- `add` performs addition.
- `divisibleby` checks divisibility.
- `first`, `last`, `length`, `slice`, and `join` are useful with lists.
- `yesno` provides readable output for `True`, `False`, and `None`.
- `pluralize` helps display singular/plural words.
- `date` and `time` format date/time values.
- `urlencode` performs URL encoding.
- `floatformat` controls decimal formatting.
- Filters help keep simple presentation logic inside templates.

---

## 40. What's Next?

After learning template filters, the next step is to practice Django Template Language more deeply.

The next topics can include:

- Advanced template tags
- Template conditions
- Loops
- Built-in template tags
- Static files
- Template inheritance
- Custom template filters and tags

The goal is to become comfortable with displaying and formatting dynamic data using Django templates.
