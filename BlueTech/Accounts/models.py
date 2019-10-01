from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_name = models.CharField(max_length=100)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    date = models.DateField()
    gender = models.CharField(max_length=50)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    reporting_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Is_verified = models.BooleanField()
    cv = models.FileField(upload_to=None)


class Complaints(models.Model):
    description = models.CharField(max_length=5000)
    filed_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    filed_against = models.CharField(max_length=100)
    date = models.DateField()


class Salary_desc(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payroll = models.IntegerField()
    Incentives = models.IntegerField()
    tax = models.FloatField()


class Meetings(models.Model):
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    organiser = models.CharField(max_length=100)
    date = models.DateField()


class Trainings(models.Model):
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    traineer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=5000)


class product(models.Model):
    prod_name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    price = models.FloatField()


class sales_desc(models.Model):
    sales_id = models.ForeignKey(sales, on_delete=models.CASCADE)
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class sales(models.Model):
    prod_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    seeling_date = models.DateField(_(""), auto_now=False, auto_now_add=False)


class Leads(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.PhoneNumberField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=500)


class Customers(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.PhoneNumberField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1000)


class Purcahge(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Purcahged_from = models.CharField(max_length=100)
    date = models.DateField()


class account_payable(models.Model):
    purchage_id = models.ForeignKey(Purcahge, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    deal_amount = models.IntegerField()
    liberage = models.IntegerField()
    net_amount = models.IntegerField()


class sales_table(models.Model):
    sales_id = models.ForeignKey(sales, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    deal_amount = models.IntegerField()
    liberage = models.IntegerField()
    net_amount = models.IntegerField()


class assets(models.Model):
    cash = models.FloatField()
    investment_value = models.FloatField()
    capital_asset = models.FloatField()


class liability(models.Model):
    current_liability = models.FloatField()
    non_current_liability = models.FloatField()
