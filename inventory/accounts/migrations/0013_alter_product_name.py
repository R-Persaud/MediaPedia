# Generated by Django 4.1.7 on 2023-04-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_employee_phonenumber_alter_employee_employeeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]