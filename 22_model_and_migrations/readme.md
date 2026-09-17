# Chapter  - Django Models and Migrations

## 1. Introduction to Django Models

In Django, a **model** is a Python class that represents a database table.

Models are normally created inside the app's:

```text
models.py
```

Example:

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Here:

- `Student` represents the model/table.
- `name` and `age` represent fields.
- Django ORM uses this model to work with the database.

---

## 2. Creating a Model

To create a model, define a Python class that inherits from:

```python
models.Model
```

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

The model describes the structure of the data that Django will manage in the database.

---

## 3. Understanding Model Fields

Fields define the type of data that can be stored.

Common examples:

```python
name = models.CharField(max_length=100)
age = models.IntegerField()
email = models.EmailField(unique=True)
enrollment_date = models.DateField(auto_now_add=True)
```

Important options used in the lecture:

- `max_length=100` → maximum length for a `CharField`.
- `unique=True` → value should be unique.
- `auto_now_add=True` → automatically sets the date when the object is created.

---

## 4. Model and Database Table

A model represents the structure of a database table.

For example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
```

Conceptually, the table contains:

```text
Student
--------------------------------
id
name
age
email
enrollment_date
```

Django can automatically create an `id` primary key when one is not explicitly defined.

---

## 5. What Are Migrations?

A migration is Django's way of recording changes made to models so those changes can be applied to the database.

The overall process is:

```text
models.py
    ↓
makemigrations
    ↓
Migration File
    ↓
migrate
    ↓
Database Table
```

A model definition alone does not immediately create or update the database table.

---

## 6. `makemigrations` Command

After creating or modifying a model, run:

```bash
python manage.py makemigrations
```

This command:

- Detects changes in the models.
- Creates a migration file.
- Stores the migration inside the app's `migrations` folder.

Example:

```text
blog/
└── migrations/
    ├── __init__.py
    └── 0001_initial.py
```

The migration file contains instructions describing the required database schema changes.

---

## 7. `migrate` Command

After creating the migration, run:

```bash
python manage.py migrate
```

This applies the migration to the database.

Remember:

```text
makemigrations → Creates migration file
migrate        → Applies migration to database
```

During the first migration, Django may also apply migrations belonging to its built-in applications such as authentication and sessions.

---

## 8. Changing an Existing Model

Suppose the original model is:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Later, we add:

```python
email = models.EmailField(unique=True)
```

After changing `models.py`, run:

```bash
python manage.py makemigrations
```

Django creates another migration file.

Then run:

```bash
python manage.py migrate
```

The database structure is updated according to the new migration.

---

## 9. Complete Model-to-Database Workflow

The complete process can be remembered as:

```text
1. Create or modify model
          ↓
2. Save models.py
          ↓
3. Run makemigrations
          ↓
4. Migration file is created
          ↓
5. Run migrate
          ↓
6. Database table/schema is updated
```

Example commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

Migration files normally preserve the history of database schema changes, so existing migrations should not be casually deleted in an established project.

---

## 10. Key Takeaways

- A Django model is a Python class representing database data.
- Models are normally written inside `models.py`.
- Model fields define the type of data.
- `CharField`, `IntegerField`, `EmailField`, and `DateField` are common field types.
- `makemigrations` creates migration files.
- `migrate` applies migrations to the database.
- Model changes are generally followed by the migration workflow.
- Django can automatically create a primary key when one is not explicitly defined.
- Migrations keep track of database schema changes.
- The next step is learning how to insert, read, update, and delete data using Django ORM.

---

## 11. Interview Questions

### Q1. What is a Django model?

A Django model is a Python class that represents the structure of application data and is used by Django ORM to interact with the database.

### Q2. Where are Django models normally created?

They are normally created inside an app's `models.py` file.

### Q3. What is a migration in Django?

A migration records changes made to models and allows those changes to be applied to the database.

### Q4. What is the difference between `makemigrations` and `migrate`?

```text
makemigrations → Creates migration files
migrate        → Applies migrations to the database
```

### Q5. What does `models.Model` do?

`models.Model` is Django's base model class from which Django model classes inherit.

### Q6. What is `max_length`?

`max_length` specifies the maximum length of a `CharField`.

Example:

```python
name = models.CharField(max_length=100)
```

### Q7. What does `unique=True` mean?

It specifies that duplicate values should not be allowed for that field.

Example:

```python
email = models.EmailField(unique=True)
```

### Q8. What does `auto_now_add=True` do?

It automatically sets a date/time field when an object is created.

Example:

```python
enrollment_date = models.DateField(auto_now_add=True)
```
