# Generated by Django 2.0.2 on 2018-12-31 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPurchaseAction',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=127)),
                ('customer_name', models.CharField(max_length=127)),
                ('price', models.IntegerField()),
                ('num', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.ProductInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSaleAction',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=127)),
                ('customer_name', models.CharField(max_length=127)),
                ('price', models.IntegerField()),
                ('num', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.ProductInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseTicket',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticket_name', models.CharField(max_length=127, unique=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('total_money', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('paid', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.Customer')),
                ('items', models.ManyToManyField(to='tickets.ProductPurchaseAction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesTicket',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticket_name', models.CharField(max_length=127, unique=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('total_money', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('paid', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.Customer')),
                ('items', models.ManyToManyField(to='tickets.ProductSaleAction')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
