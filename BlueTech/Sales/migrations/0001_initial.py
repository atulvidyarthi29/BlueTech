# Generated by Django 2.2.6 on 2020-10-24 19:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.IntegerField(unique=True)),
                ('account_number', models.IntegerField(blank=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=20)),
                ('bank_name', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10)),
                ('doj', models.DateField(blank=True, default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.AutoField(primary_key=True, serialize=False, verbose_name=int)),
                ('date', models.DateField(default=datetime.date.today)),
                ('total_amount', models.FloatField(blank=True, default=0)),
                ('amount_crdited', models.FloatField(blank=True, default=0)),
                ('amount_left', models.FloatField(blank=True, default=0)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1000)),
                ('remarks', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('itemcode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField(default=0)),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('selling_date', models.DateField(verbose_name='')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Customer')),
                ('prod_id', models.ForeignKey(db_column='itemcode', on_delete=django.db.models.deletion.CASCADE, to='sales.Product')),
            ],
        ),
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalesDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Employee')),
                ('sales_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Sale')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('purchased_from', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('product_id', models.ForeignKey(db_column='itemcode', on_delete=django.db.models.deletion.CASCADE, to='sales.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.FloatField(blank=True, default=0)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Product')),
            ],
        ),
    ]
