from django.db import models

# Create your models here.
class Student(models.Model):            # where the 'Model' is method of 'models' module which is imported from 'django.db' package.
    id = models.AutoField(primary_key=True) # An auto-incrementing primary key field for the student ID.
    name = models.CharField(max_length=100) # A character field for the student's name with a maximum length of 100 characters.
    age = models.IntegerField()             # An integer field for the student's age.
    email = models.EmailField(unique=True)  # An email field for the student's email address, which must be unique.
    ph_no = models.CharField(max_length=10) # A character field for the student's phone number with a maximum length of 10 characters.
    roll_no = models.CharField(max_length=10, unique=True) # A character field for the student's roll number with a maximum length of 10 characters, which must be unique.