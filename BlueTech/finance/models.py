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
    date = models.DateField("Date", default=datetime.date.today)
    annual_return_rate = models.DecimalField(max_digits=12, decimal_places=2)
    tax_levied = models.DecimalField(max_digits=12, decimal_places=2)
    asset_value = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def net_income(self):
        return (float(self.asset_value) * float(self.annual_return_rate) * 0.01) * (1 - float(self.tax_levied) * 0.01)


class Liability(models.Model):
    tax_levied = models.DecimalField(max_digits=12, decimal_places=2)
    liability_type = models.CharField(max_length=200)
    date = models.DateField("Date", default=datetime.date.today)
    annual_return_rate = models.DecimalField(max_digits=12, decimal_places=2)
    liability_value = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def net_expense(self):
        return (float(self.liability_value) * float(self.annual_return_rate) * 0.01) * (
                    1 + float(self.tax_levied) * 0.01)


class FinancialYear(models.Model):
    year = models.IntegerField()


class ShareholderFunds(models.Model):
    year = models.ForeignKey(FinancialYear, on_delete=models.CASCADE)
    equity_share = models.DecimalField(max_digits=12, decimal_places=2)
    reserves_surplus = models.DecimalField(max_digits=12, decimal_places=2)
    revaluation_reserves = models.DecimalField(max_digits=12, decimal_places=2)
    share_application_money = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def net_share_holding(self):
        return float(self.equity_share) + float(self.reserves_surplus) + float(self.revaluation_reserves) + float(
            self.share_application_money)


class LiabilitySources(models.Model):
    year = models.ForeignKey(FinancialYear, on_delete=models.CASCADE)
    secured_loans = models.DecimalField(max_digits=12, decimal_places=2)
    unsecured_loans = models.DecimalField(max_digits=12, decimal_places=2)
    reserves_surplus = models.DecimalField(max_digits=12, decimal_places=2)
    revaluation_reserves = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def net_liabilities(self):
        return float(self.secured_loans) + float(self.unsecured_loans) + float(self.reserves_surplus) + float(
            self.revaluation_reserves)


class FundApplication(models.Model):
    year = models.ForeignKey(FinancialYear, on_delete=models.CASCADE)
    gross_block = models.DecimalField(max_digits=12, decimal_places=2)
    capital_work_in_progress = models.DecimalField(max_digits=12, decimal_places=2)
    inventories = models.DecimalField(max_digits=12, decimal_places=2)
    debtors = models.DecimalField(max_digits=12, decimal_places=2)
    cash_and_bank_balance = models.DecimalField(max_digits=12, decimal_places=2)
    loans_forwarded = models.DecimalField(max_digits=12, decimal_places=2)
    operational_activities = models.DecimalField(max_digits=12, decimal_places=2)
    cost_of_materials = models.DecimalField(max_digits=12, decimal_places=2)
    change_in_inventories = models.DecimalField(max_digits=12, decimal_places=2)
    employee_benefit_cost = models.DecimalField(max_digits=12, decimal_places=2)
    finance_cost = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def net_fund_application(self):
        return float(self.gross_block) + float(self.capital_work_in_progress) + float(self.inventories) + float(
            self.debtors) + float(self.cash_and_bank_balance) + float(self.loans_forwarded) + float(
            self.operational_activities) + float(self.cost_of_materials) + float(self.change_in_inventories) + float(
            self.employee_benefit_cost) + float(self.finance_cost)


class Profit(models.Model):
    year = models.ForeignKey(FinancialYear, on_delete=models.CASCADE)
    estimated_profit = models.DecimalField(max_digits=12, decimal_places=2)
    estimated_profit_before_tax = models.DecimalField(max_digits=12, decimal_places=2)
    real_profit = models.DecimalField(max_digits=12, decimal_places=2)
