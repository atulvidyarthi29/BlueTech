import uuid

from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True


class License(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=70)
    phone_no = models.CharField(max_length=10)
    licence = models.UUIDField(default=uuid.uuid4, editable=False)
    validated = models.BooleanField()


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15, null=True)
    date = models.DateField(null=True)
    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'),)
    gender = models.CharField(max_length=50, null=True, choices=GENDER_CHOICES)
    DEPT_CHOICES = (('CEO', 'CEO'),
                    ('HR', 'HR'),
                    ('SALES', 'SALES'),
                    ('ACCOUNTS', 'ACCOUNTS'))
    dept = models.CharField(max_length=100, choices=DEPT_CHOICES)
    position = models.CharField(max_length=50, null=True)
    date_of_joining = models.DateField(null=True)
    reporting_to = models.ForeignKey(
        "Employee", null=True, on_delete=models.CASCADE)
    is_verified = models.BooleanField()
    is_complete = models.BooleanField()
    cv = models.FileField(upload_to='media/cv')
    profile_pic = models.ImageField(upload_to='media/profile_pics')

    def __str__(self):
        return self.user.username


class EmailDepartment(models.Model):
    email = models.EmailField(max_length=70)
    DEPT_CHOICES = (('CEO', 'CEO'),
                    ('HR', 'HR'),
                    ('SALES', 'SALES'),
                    ('ACCOUNTS', 'ACCOUNTS'))
    dept = models.CharField(max_length=10, choices=DEPT_CHOICES)
