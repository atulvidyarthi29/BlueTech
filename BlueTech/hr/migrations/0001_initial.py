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
            name='EmailFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/email_departments/')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=5000)),
                ('trainee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainee', to='users.Employee')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to='users.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=5000)),
                ('date', models.DateField()),
                ('organiser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organiser', to='users.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain', models.CharField(max_length=5000)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=200)),
                ('against', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='against', to='users.Employee')),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='by', to='users.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payroll', models.IntegerField()),
                ('Incentives', models.IntegerField()),
                ('tax', models.FloatField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Employee')),
            ],
            options={
                'unique_together': {('employee_id',)},
            },
        ),
    ]