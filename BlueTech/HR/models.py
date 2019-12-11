from django.db import models
from Users.models import Employee


# Create your models here.


class Complaint(models.Model):
    description = models.CharField(max_length=5000)
    filed_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    filed_against = models.CharField(max_length=100)
    date = models.DateField()


class Meeting(models.Model):
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    organiser = models.ForeignKey(
        Employee, null=True, related_name='organiser', on_delete=models.CASCADE)
    date = models.DateField()


class Training(models.Model):
    trainee = models.ForeignKey(
        Employee, null=True, related_name='trainee', on_delete=models.CASCADE)
    trainer = models.ForeignKey(
        Employee, null=True, related_name='trainer', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=5000)


class Salary(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payroll = models.IntegerField()
    Incentives = models.IntegerField()
    tax = models.FloatField()

    class Meta:
        unique_together = ['employee_id']


class EmailFiles(models.Model):
    file = models.FileField(upload_to='Media/email_departments/')
