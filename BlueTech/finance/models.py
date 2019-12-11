from django.db import models
from Sales.models import Purchase, Product, Sale
import datetime


# Create your models here.


class SalesAccount(models.Model):
    sales_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField("Date", default=datetime.date.today)
    price = models.IntegerField()

    @property
    def net_amount(self):
        return (self.quantity * self.price) * 0.82


class PayableAccount(models.Model):
    purchase_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField("Date", default=datetime.date.today)
    quantity = models.IntegerField()
    price = models.IntegerField()

    @property
    def net_expenditure(self):
        return (self.quantity * self.price) * 1.18


class Asset(models.Model):
    asset_type = models.CharField(max_length=200)
    annual_return_rate = models.DecimalField(max_digits=12, decimal_places=2)
    tax_levied = models.DecimalField(max_digits=12, decimal_places=2)
    asset_value = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def net_income(self):
        return (float(self.asset_value) * float(self.annual_return_rate) * 0.01) * (1 - float(self.tax_levied) * 0.01)


class Liability(models.Model):
    tax_levied = models.DecimalField(max_digits=12, decimal_places=2)
    liability_type = models.CharField(max_length=200)
    annual_return_rate = models.DecimalField(max_digits=12, decimal_places=2)
    liability_value = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def net_expense(self):
        return (float(self.liability_value) * float(self.annual_return_rate) * 0.01) * (1 + float(self.tax_levied) * 0.01)
