# Chapter 23 - Django ORM QuerySet and Data Retrieval

## 1. Introduction to Data Retrieval

In this lecture, we learn how to retrieve data from a database using Django ORM.

The lecture introduces three important QuerySet methods:

```python
all()
get()
filter()
```

Django ORM allows us to work with database data using Python code instead of directly writing SQL queries.

The basic flow is:

```text
Database
    ↓
Django Model
    ↓
Django ORM
    ↓
QuerySet
    ↓
Python / HTML Template
```

---

## 2. What is a QuerySet?

A QuerySet is a collection of database rows represented as Django model objects.

For example, if the `Student` table contains multiple students:

```text
Student Table
--------------------------------
id    name     age    city
1     Mohit    25     Delhi
2     Rohit    30     Ghaziabad
3     Anil     28     Delhi
4     Anuj     35     Ghaziabad
```

Django can retrieve these records as model objects through a QuerySet.

One benefit of Django ORM is that we can use Python code instead of writing database-specific SQL queries.

---

## 3. Django Shell

The lecture uses Django Shell to test ORM queries.

Start the shell using:

```bash
python manage.py shell
```

Import the model:

```python
from blog.models import Student
```

Here:

```text
blog
→ App name

Student
→ Model name
```

After importing the model, we can use Django ORM commands directly in the shell.

---

## 4. Using `__str__()` for Readable Output

Inside the model, we can define:

```python
def __str__(self):
    return self.name
```

Without `__str__()`, objects may appear like:

```text
<Student: Student object (1)>
<Student: Student object (2)>
```

With `__str__()`:

```text
<Student: Mohit>
<Student: Rohit>
<Student: Anil>
```

The purpose is to make model objects easier to read when displayed.

Important:

```text
__str__()
→ Improves object representation
→ Does not modify database data
```

---

## 5. `all()` – Retrieve All Records

The `all()` method is used to retrieve all records from a model.

Example:

```python
students = Student.objects.all()
```

Print the QuerySet:

```python
print(students)
```

To access individual fields:

```python
for student in students:
    print(student.name)
    print(student.age)
    print(student.city)
```

Conceptually, it is similar to:

```sql
SELECT * FROM student;
```

So:

```python
Student.objects.all()
```

means:

```text
Retrieve all records from Student.
```

---

## 6. `get()` – Retrieve a Single Record

The `get()` method is used when we want to retrieve a single record.

Example:

```python
student = Student.objects.get(id=1)
```

We can access its fields:

```python
print(student.name)
print(student.age)
print(student.city)
```

A unique field can also be used:

```python
student = Student.objects.get(email="test@gmail.com")
```

Important:

`get()` should be used when we are expecting one specific record.

If no record exists, Django raises:

```text
DoesNotExist
```

If multiple records match the condition, Django raises:

```text
MultipleObjectsReturned
```

---

## 7. `filter()` – Retrieve Records with Conditions

The `filter()` method is used to retrieve records based on conditions.

Example:

```python
students = Student.objects.filter(age=30)
```

Print the result:

```python
print(students)
```

It returns a QuerySet.

Conceptually:

```sql
SELECT * FROM student
WHERE age = 30;
```

Unlike `get()`, `filter()` can return multiple records.

For example:

```python
students = Student.objects.filter(age=18)
```

can return all students whose age is 18.

---

## 8. Common Filter Lookups

Django provides lookup expressions for filtering records.

### Greater Than

```python
Student.objects.filter(age__gt=18)
```

`gt` means greater than.

### Less Than

```python
Student.objects.filter(age__lt=30)
```

`lt` means less than.

### Greater Than or Equal To

```python
Student.objects.filter(age__gte=18)
```

`gte` means greater than or equal to.

### Less Than or Equal To

```python
Student.objects.filter(age__lte=30)
```

`lte` means less than or equal to.

### Starts With

```python
Student.objects.filter(name__startswith="A")
```

This retrieves records whose name starts with `A`.

### iContains

```python
Student.objects.filter(name__icontains="A")
```

It retrieves all Student records where the name field contains the letter "A" anywhere in the string, ignoring case.

---

## 9. `all()` vs `get()` vs `filter()`

| Method | Purpose | Result |
| --- | --- | --- |
| `all()` | Retrieve all records | QuerySet |
| `get()` | Retrieve one specific record | Model object |
| `filter()` | Retrieve records matching conditions | QuerySet |

Easy way to remember:

```text
all()
→ All records

get()
→ One specific record

filter()
→ Records matching a condition
```

Example:

```python
Student.objects.all()
```

```python
Student.objects.get(id=1)
```

```python
Student.objects.filter(age=30)
```

---

## 10. Using Retrieved Data

After retrieving records using a QuerySet, we can access their fields using a loop.

Example:

```python
students = Student.objects.all()

for student in students:
    print(student.name)
    print(student.age)
    print(student.city)
```

The same retrieved data can later be passed from a Django view to an HTML template.

The basic flow is:

```text
Database
    ↓
Model
    ↓
ORM Query
    ↓
QuerySet
    ↓
View
    ↓
HTML Template
    ↓
User Interface
```

---

## Interview Questionss

### Q1. What is Django ORM?

Django ORM allows us to interact with the database using Python code instead of directly writing SQL queries.

### Q2. What is a QuerySet?

A QuerySet is a collection of database records represented as Django model objects.

### Q3. What does `objects.all()` do?

It retrieves all records from the model's database table.

### Q4. What is the difference between `get()` and `filter()`?

`get()` is used to retrieve one specific object, while `filter()` returns a QuerySet that can contain multiple objects.

### Q5. What happens if `get()` does not find a record?

Django raises a `DoesNotExist` exception.

### Q6. What happens if `get()` finds multiple records?

Django raises a `MultipleObjectsReturned` exception.

### Q7. Why is `__str__()` used in a Django model?

It provides a readable representation of model objects.

### Q8. Does `__str__()` change the database?

No. It only changes how the object is represented when displayed.

### Q9. What does `__gt` mean?

`__gt` means greater than.

Example:

```python
Student.objects.filter(age__gt=18)
```

### Q10. What does `__gte` mean?

`__gte` means greater than or equal to.

Example:

```python
Student.objects.filter(age__gte=18)
```

### Q11. What does `__lt` mean?

`__lt` means less than.

Example:

```python
Student.objects.filter(age__lt=30)
```

### Q12. What does `__lte` mean?

`__lte` means less than or equal to.

Example:

```python
Student.objects.filter(age__lte=30)
```

### Q13. What does `__startswith` do?

It retrieves records where the specified field starts with the given value.

Example:

```python
Student.objects.filter(name__startswith="A")
```

### Q14. Where can Django ORM queries be tested directly?

They can be tested using the Django Shell:

```bash
python manage.py shell
```

### Q15. What is the basic syntax for retrieving all records?

```python
Model.objects.all()
```

### Q16. What is the basic syntax for retrieving one record?

```python
Model.objects.get(field=value)
```

### Q17. What is the basic syntax for filtering records?

```python
Model.objects.filter(field=value)
```

---

## Quick Revision

```python
# Start Django Shell
python manage.py shell

# Import model
from blog.models import Student

# Retrieve all records
students = Student.objects.all()

# Retrieve one record
student = Student.objects.get(id=1)

# Filter records
students = Student.objects.filter(age=30)

# Greater than
Student.objects.filter(age__gt=18)

# Less than
Student.objects.filter(age__lt=30)

# Greater than or equal
Student.objects.filter(age__gte=18)

# Less than or equal
Student.objects.filter(age__lte=30)

# Name starts with A
Student.objects.filter(name__startswith="A")

# Table contains "A"
Student.objects.filter(name__icontains="A")

# Read fields
for student in students:
    print(student.name)
    print(student.age)
    print(student.city)
```
