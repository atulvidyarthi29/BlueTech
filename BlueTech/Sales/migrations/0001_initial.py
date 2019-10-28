# Generated by Django 2.1.7 on 2019-10-16 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1000)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=5000)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('purchased_from', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('selling_date', models.DateField(verbose_name='')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.Customer')),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SalesDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Employee')),
                ('sales_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.Sale')),
            ],
        ),
    ]
