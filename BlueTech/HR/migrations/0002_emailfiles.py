# Generated by Django 2.0 on 2019-11-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='Media/email_departments')),
            ],
        ),
    ]