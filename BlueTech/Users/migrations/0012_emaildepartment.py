# Generated by Django 2.0 on 2019-11-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_employee_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('dept', models.CharField(choices=[('CEO', 'CEO'), ('HR', 'HR'), ('SALES', 'SALES'), ('ACCOUNTS', 'ACCOUNTS')], max_length=10)),
            ],
        ),
    ]
