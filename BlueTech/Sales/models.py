import datetime

from django.db import models
from Users.models import Employee

status = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
)


class Product(models.Model):
    itemcode = models.CharField(primary_key=True, max_length=20)
    itemname = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    discount = models.FloatField(default=0)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.itemname


class Customer(models.Model):
    company_name = models.CharField(max_length=200)
    email = models.EmailField(blank=False, unique=True)
    mobile = models.IntegerField(blank=False, unique=True)
    account_number = models.IntegerField(blank=True)
    ifsc_code = models.CharField(blank=True, max_length=20)
    bank_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=500, blank=True)
    status = models.CharField(choices=status, null=False, max_length=10)
    doj = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return self.company_name


class Invoice(models.Model):
    invoice_no = models.AutoField(int, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today, blank=False)
    total_amount = models.FloatField(default=0, blank=True)
    amount_crdited = models.FloatField(default=0, blank=True)
    amount_left = models.FloatField(default=0, blank=True)
    status = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return "INV"+str(self.invoice_no)


class ProductBought(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=False)
    amount = models.FloatField(default=0, blank=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.product)


class Sale(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="itemcode")
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    selling_date = models.DateField("", auto_now=False, auto_now_add=False)


class SalesDesc(models.Model):
    sales_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=500)


class Purchase(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='itemcode')
    Quantity = models.IntegerField()
    purchased_from = models.CharField(max_length=100)
    date = models.DateField()

class userlogin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)