# models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    # email = models.EmailField()
    title=models.CharField(max_length=2123)
    age = models.IntegerField()
    

    def __str__(self):
        return self.name