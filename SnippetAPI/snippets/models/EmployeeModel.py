from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_branch = models.CharField(max_length=100)
    emp_salary = models.IntegerField()
    emp_phoneno = models.IntegerField()
    emp_location = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name