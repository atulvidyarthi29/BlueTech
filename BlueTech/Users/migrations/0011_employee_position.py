# Generated by Django 2.1.7 on 2019-11-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_auto_20191110_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=50, null=True),
        ),
    ]