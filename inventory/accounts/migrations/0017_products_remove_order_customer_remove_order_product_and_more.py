# Generated by Django 4.1.7 on 2023-04-07 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_roles_delete_tag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('pmediatype', models.CharField(max_length=1)),
                ('pprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pquantity', models.IntegerField(default=0)),
                ('pamountsold', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeePassword',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeRole_id',
            field=models.ForeignKey(db_column='employeeRole_id', on_delete=django.db.models.deletion.RESTRICT, to='accounts.roles'),
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('bid', models.ForeignKey(db_column='bid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.products')),
                ('btitle', models.CharField(max_length=500)),
                ('bauthor', models.CharField(max_length=500)),
                ('bgenre', models.CharField(max_length=500)),
                ('bstarrating', models.FloatField(default=0.0)),
                ('binstock', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CDs',
            fields=[
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.products')),
                ('ctitle', models.CharField(max_length=500)),
                ('cartist', models.CharField(max_length=500)),
                ('cgenre', models.CharField(max_length=500)),
                ('cstarrating', models.FloatField(default=0.0)),
                ('cinstock', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='DVDs',
            fields=[
                ('did', models.ForeignKey(db_column='did', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.products')),
                ('dtitle', models.CharField(max_length=500)),
                ('dactor', models.CharField(max_length=500)),
                ('dgenre', models.CharField(max_length=500)),
                ('dstarrating', models.FloatField(default=0.0)),
                ('dinstock', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('rid', models.ForeignKey(db_column='rid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.products')),
                ('rtitle', models.CharField(max_length=500)),
                ('rartist', models.CharField(max_length=500)),
                ('rgenre', models.CharField(max_length=500)),
                ('rstarrating', models.FloatField(default=0.0)),
                ('rinstock', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
