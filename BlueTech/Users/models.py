from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):
    dept_name = models.CharField(max_length=100)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    date = models.DateField()
    gender = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    reporting_to = models.ForeignKey(
        "Employee",  on_delete=models.CASCADE)
    Is_verified = models.BooleanField()
    cv = models.FileField(upload_to=None)
