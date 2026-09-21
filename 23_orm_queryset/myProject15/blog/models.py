from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self): # It reurns the string representation of the object. It is used to display the object in a human-readable format.
        return f"{self.name} ({self.roll}) - {self.city}"