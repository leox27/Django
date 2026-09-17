# Chapter 21 - Django ORM (Object-Relational Mapper)

## 1. Introduction to Django ORM

- ORM stands for **Object-Relational Mapper**.
- Django ORM allows us to work with databases using **Python code and Django models** instead of writing SQL queries for every operation.
- A Django model is written as a Python class.
- Django ORM translates operations performed on the model into database-specific SQL.

> ORM does not mean that SQL disappears completely. Django generates SQL behind the scenes, while developers can work mainly with Python and Django's ORM API.

---

## 2. Full Form of ORM

### ORM = Object-Relational Mapper

It provides a bridge between:

- Python objects/classes
- Relational database tables
- SQL queries

The basic idea is:

```text
Python Model / ORM Operation
          ↓
      Django ORM
          ↓
   SQL Statement
          ↓
       Database
```

---

## 3. Why Django Provides ORM

Without an ORM, developers often need to write database-specific SQL manually.

For example:

```sql
SELECT * FROM student;
```

With Django ORM:

```python
Student.objects.all()
```

Django converts the ORM operation into an appropriate SQL query for the configured database.

---

## 4. Object-Relational Mapping Concept

ORM maps programming concepts to database concepts.

| Python / Django | Database |
| --- | --- |
| Model class | Table |
| Model field | Column |
| Model object | Row |
| QuerySet | Query result |
| ORM operation | SQL query |

For example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Conceptually, this represents a database table containing columns such as:

```text
name
age
```

---

## 5. Basic ORM Working Architecture

The basic ORM workflow can be understood in two directions.

### Writing data

```text
Python/Django Code
       ↓
     ORM
       ↓
Generated SQL
       ↓
    Database
       ↓
 Data Stored
```

### Reading data

```text
Database
    ↓
SQL Result
    ↓
   ORM
    ↓
Python Objects / QuerySet
    ↓
Application
```

---

## 6. Python Code to SQL Conversion

Suppose we write an ORM operation:

```python
Student.objects.all()
```

Django ORM translates this operation into SQL conceptually similar to:

```sql
SELECT * FROM student;
```

The exact generated SQL can vary depending on:

- Database backend
- Model configuration
- Django version
- Query being performed

---

## 7. Creating a Django Model

A Django model is normally created inside an app's `models.py`.

Example:

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Here:

- `Student` is the model class.
- `name` is a model field.
- `age` is a model field.
- `CharField` represents text data.
- `IntegerField` represents integer data.

---

## 8. Model Class and Database Table

The model is written using Python syntax:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Django uses this model definition to create the corresponding database structure through migrations.

Conceptually:

```text
Student class
      ↓
Django ORM
      ↓
Student database table
```

---

## 9. CharacterField for Names

For text such as a student's name, we can use:

```python
name = models.CharField(max_length=100)
```

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
```

`max_length` defines the maximum length of the field.

---

## 10. IntegerField for Age

For integer values such as age:

```python
age = models.IntegerField()
```

Complete example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

---

## 11. Model Fields and Database Columns

A model field generally corresponds to a database column.

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Conceptually:

```text
Student
----------------
name
age
```

Django handles the database-specific SQL required to create and work with these fields.

---

## 12. Creating Database Tables with Migrations

Defining a model alone is not enough to update the database.

The normal Django workflow is:

```bash
python manage.py makemigrations
python manage.py migrate
```

First:

```bash
python manage.py makemigrations
```

Django creates migration instructions based on model changes.

Then:

```bash
python manage.py migrate
```

Django applies those changes to the database.

---

## 13. ORM for Retrieving Data

Suppose we have a `Student` model.

To retrieve all students:

```python
students = Student.objects.all()
```

This is conceptually similar to:

```sql
SELECT * FROM student;
```

The returned `students` value is a **QuerySet**.

---

## 14. Understanding the Objects Manager

In:

```python
Student.objects.all()
```

`objects` is Django's default model manager.

It provides methods for interacting with the database.

Common methods include:

```python
Student.objects.all()
Student.objects.filter(...)
Student.objects.get(...)
Student.objects.create(...)
```

The manager acts as an entry point for many ORM operations.

---

## 15. The `all()` Query

The `all()` method retrieves all objects matching the query.

Example:

```python
students = Student.objects.all()
```

Conceptually:

```sql
SELECT * FROM student;
```

You can then iterate over the result:

```python
for student in students:
    print(student.name)
```

---

## 16. QuerySet Concept

A QuerySet represents a collection of database records returned by Django ORM.

Example:

```python
students = Student.objects.all()
```

Here:

```text
students
   ↓
QuerySet
   ↓
Student records
```

A QuerySet can be filtered, ordered, sliced, and further queried.

---

## 17. ORM Compared with Raw SQL

### Raw SQL

```sql
SELECT * FROM student;
```

### Django ORM

```python
Student.objects.all()
```

The ORM version is written using Python/Django syntax and allows Django to generate the appropriate SQL.

---

## 18. Database Independence

One major benefit of ORM is that the same ORM code can often work with different supported relational databases.

Examples include:

- SQLite
- PostgreSQL
- MySQL
- Oracle

For example:

```python
Student.objects.all()
```

does not contain PostgreSQL-specific or Oracle-specific SQL.

Django's database backend handles the database-specific SQL generation.

---

## 19. Changing the Database Backend

A project can be configured to use different supported database systems.

The application code can continue using Django ORM:

```python
Student.objects.all()
```

while the configured database backend changes.

However, database migration is not always completely automatic or problem-free.

Considerations can include:

- Database-specific features
- Existing data
- Field compatibility
- Constraints
- SQL differences
- Migration requirements

So ORM reduces database dependency, but it does not guarantee that every database can be swapped without additional work.

---

## 20. Less Manual SQL

With Django ORM, common operations can be written without manually creating SQL statements.

Examples:

```python
Student.objects.all()
```

```python
Student.objects.filter(age=20)
```

```python
Student.objects.get(id=1)
```

```python
Student.objects.create(name="Mohit", age=20)
```

Django generates the corresponding SQL behind the scenes.

---

## 21. ORM and Readability

Compare:

```sql
SELECT * FROM student;
```

with:

```python
Student.objects.all()
```

The ORM syntax integrates database operations directly into Python/Django code.

This can make application code easier to understand for developers who primarily work with Python.

---

## 22. ORM and Maintainability

ORM can make database-related application code easier to maintain because:

- Models describe the data structure.
- Queries use a consistent Python API.
- Database-specific SQL is generally handled by Django.
- Model changes can be managed through migrations.
- Common database operations do not require repeated raw SQL.

---

## 23. ORM and Security

Using Django ORM can help reduce SQL injection risks because Django handles query construction and parameterization for normal ORM operations.

For example:

```python
Student.objects.filter(name=user_name)
```

is preferable to manually constructing SQL by concatenating user input.

However, ORM does **not** automatically make every database operation secure.

Developers still need to:

- Validate input.
- Use ORM APIs correctly.
- Be careful with raw SQL.
- Follow Django security practices.

---

## 24. ORM Does Not Mean SQL Is Unnecessary

Django ORM covers many common database operations.

However, Django also provides ways to execute raw SQL when necessary.

For example:

```python
from django.db import connection
```

Raw SQL may sometimes be used for:

- Database-specific features
- Highly specialized queries
- Legacy SQL
- Cases where ORM is not suitable

For normal application operations, Django ORM is usually the primary database API.

---

## 25. Basic Create Operation

A model object can be created through the ORM.

Example:

```python
student = Student.objects.create(
    name="Mohit",
    age=20
)
```

Conceptually, this performs an SQL `INSERT`.

The important idea is:

```text
Python object/data
       ↓
Django ORM
       ↓
INSERT SQL
       ↓
Database
```

---

## 26. Basic Read Operation

Retrieve all students:

```python
students = Student.objects.all()
```

Retrieve students matching a condition:

```python
students = Student.objects.filter(age=20)
```

Retrieve one specific object:

```python
student = Student.objects.get(id=1)
```

These are ORM operations rather than manually written SQL statements.

---

## 27. Basic Update Operation

An existing object can be modified:

```python
student = Student.objects.get(id=1)

student.age = 21
student.save()
```

Conceptually, Django performs an SQL `UPDATE`.

The flow is:

```text
Get object
   ↓
Change attribute
   ↓
save()
   ↓
Database updated
```

---

## 28. Basic Delete Operation

An object can be deleted using:

```python
student = Student.objects.get(id=1)
student.delete()
```

Conceptually, this performs an SQL `DELETE`.

---

## 29. CRUD and Django ORM

CRUD means:

| Operation | ORM Example |
| --- | --- |
| Create | `Student.objects.create(...)` |
| Read | `Student.objects.all()` |
| Update | `student.save()` |
| Delete | `student.delete()` |

These operations are fundamental to Django database development.

---

## 30. ORM Query Flow

A typical Django request involving a database can be visualized as:

```text
Browser
   ↓
Django URL
   ↓
View
   ↓
ORM Query
   ↓
Database Backend
   ↓
Database
   ↓
Query Result
   ↓
Django View
   ↓
Template / Response
   ↓
Browser
```

---

## 31. Example Model and Query

### Model

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

### Query

```python
students = Student.objects.all()
```

### Loop

```python
for student in students:
    print(student.name)
    print(student.age)
```

This allows Python code to work with database records as Django model objects.

---

## 32. Important ORM Terms

| Term | Meaning |
| --- | --- |
| ORM | Object-Relational Mapper |
| Model | Python representation of database data |
| Field | Model attribute representing a database column |
| Manager | Interface for database queries |
| `objects` | Default model manager |
| QuerySet | Collection/result of ORM queries |
| Migration | Django's mechanism for applying model/database schema changes |
| SQL | Language used by relational databases |

---

## 33. ORM Advantages

Important benefits include:

- Less manual SQL.
- Python-based database interaction.
- Model-based database design.
- Support for multiple relational databases.
- Reusable query APIs.
- Good readability.
- Easier maintenance for common operations.
- Integration with Django migrations.
- Protection against many SQL injection issues when using ORM correctly.

---

## 34. ORM Limitations

ORM is powerful, but it is not a replacement for understanding databases.

You should still understand:

- SQL basics.
- Tables and columns.
- Primary keys.
- Foreign keys.
- Relationships.
- Joins.
- Indexes.
- Transactions.
- Query performance.

A Django developer should understand both **Django ORM and SQL fundamentals**.

---

## 35. ORM and Database Knowledge

Learning ORM should not mean ignoring SQL.

For example, understanding:

```sql
SELECT *
FROM student
WHERE age = 20;
```

helps you understand:

```python
Student.objects.filter(age=20)
```

Knowing SQL makes it easier to:

- Understand ORM behavior.
- Debug database problems.
- Optimize queries.
- Understand joins and relationships.
- Work with database-specific issues.

---

## 36. Common Beginner Mistakes

### Mistake 1: Forgetting migrations

Incorrect assumption:

```python
class Student(models.Model):
    ...
```

automatically changes the database immediately.

Correct workflow:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Mistake 2: Confusing a model with an object

Model:

```python
class Student(models.Model):
    ...
```

Object:

```python
student = Student.objects.get(id=1)
```

### Mistake 3: Thinking `all()` immediately returns a list

```python
students = Student.objects.all()
```

returns a QuerySet, not a normal Python list.

---

## 37. Important ORM Examples

### Get all records

```python
Student.objects.all()
```

### Filter records

```python
Student.objects.filter(age=20)
```

### Get one record

```python
Student.objects.get(id=1)
```

### Create a record

```python
Student.objects.create(
    name="Rohit",
    age=21
)
```

### Delete a record

```python
student.delete()
```

---

## 38. Interview Questions

### Q1. What is ORM?

ORM stands for **Object-Relational Mapper**. It allows developers to interact with relational databases using programming-language objects and APIs instead of writing SQL for every operation.

### Q2. What is Django ORM?

Django ORM is Django's database abstraction layer that allows developers to define models as Python classes and perform database operations using Python code.

### Q3. What is a Django model?

A model is a Python class that describes the structure of application data and is used by Django ORM to interact with the database.

### Q4. What does `objects` mean?

`objects` is Django's default model manager used to perform database queries.

### Q5. What does `Student.objects.all()` do?

It returns a QuerySet containing all `Student` objects.

### Q6. Does Django ORM eliminate SQL completely?

No. Django ORM generates SQL behind the scenes, and developers can still use raw SQL when required.

### Q7. What is a QuerySet?

A QuerySet represents a collection of database records obtained through Django ORM.

---

## 39. Quick Revision Table

| Concept | Example |
| --- | --- |
| ORM full form | Object-Relational Mapper |
| Model | `class Student(models.Model)` |
| Text field | `models.CharField()` |
| Integer field | `models.IntegerField()` |
| Manager | `Student.objects` |
| All records | `Student.objects.all()` |
| Filter | `Student.objects.filter(age=20)` |
| Get one | `Student.objects.get(id=1)` |
| Create | `Student.objects.create(...)` |
| Update | `student.save()` |
| Delete | `student.delete()` |
| Create migration | `python manage.py makemigrations` |
| Apply migration | `python manage.py migrate` |

---

## 40. Key Takeaways

- **ORM = Object-Relational Mapper.**
- Django models are written as Python classes.
- Django ORM translates ORM operations into SQL.
- `models.py` is commonly used to define models.
- `Student.objects.all()` retrieves all student records.
- `objects` is the default model manager.
- QuerySets represent database query results.
- Django ORM supports common CRUD operations.
- ORM reduces the need for manually written SQL.
- Django supports multiple relational database backends.
- ORM does not remove the need to understand SQL.
- Migrations are used to apply model/schema changes to the database.
- Raw SQL is still available when ORM is not suitable.

---

## 41. What's Next

The next step is to move from the **theory of Django ORM** to practical database development.

Important topics to learn next include:

- Creating models properly.
- Model fields and options.
- Migrations.
- Creating records.
- Reading records.
- Filtering data.
- Updating records.
- Deleting records.
- QuerySets.
- Relationships between models.
- Foreign keys.
- One-to-one relationships.
- Many-to-many relationships.
- Advanced ORM queries.
