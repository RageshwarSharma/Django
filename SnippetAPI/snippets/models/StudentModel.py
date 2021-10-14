from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    teachername = models.CharField(max_length=100)
    classname = models.CharField(max_length=100)
    schoolname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname