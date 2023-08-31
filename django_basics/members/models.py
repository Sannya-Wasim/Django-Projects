from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name=models.CharField(max_length=255)
    employee_des = models.CharField(max_length=255)
    employee_contact = models.IntegerField(default=99999999999)

    def __str__(self):
        return self.employee_name

    objects = models.Manager()