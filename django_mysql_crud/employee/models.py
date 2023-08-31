from django.db import models

# Create your models here.
class Employees(models.Model):
    emp_id = models.IntegerField(primary_key=True, max_length=10)
    emp_name = models.CharField(max_length=255)
    emp_des = models.CharField(max_length=255)
    emp_contact = models.CharField(max_length=255)
    class Meta:
        db_table = 'contacts'