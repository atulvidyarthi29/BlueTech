# Generated by Django 2.2.6 on 2020-10-24 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='licence',
            field=models.CharField(default='', max_length=100),
        ),
    ]
