from django.db import models
from Sales.models import *


# Create your models here.


class PayableAccount(models.Model):
    purchase_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    deal_amount = models.IntegerField()
    liberage = models.IntegerField()
    net_amount = models.IntegerField()


class SalesAccount(models.Model):
    sales_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    deal_amount = models.IntegerField()
    liberage = models.IntegerField()
    net_amount = models.IntegerField()


class Asset(models.Model):
    cash = models.FloatField()
    investment_value = models.FloatField()
    capital_asset = models.FloatField()


class Liability(models.Model):
    current_liability = models.FloatField()
    non_current_liability = models.FloatField()
