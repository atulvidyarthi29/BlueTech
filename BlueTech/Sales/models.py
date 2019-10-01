from django.db import models
from Users.models import Employee

# Create your models here.


class Product(models.Model):
    prod_name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    price = models.FloatField()


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1000)


class Sale(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seeling_date = models.DateField((""), auto_now=False, auto_now_add=False)


class SalesDesc(models.Model):
    sales_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=500)


class Purchase(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Purcahged_from = models.CharField(max_length=100)
    date = models.DateField()
