# Generated by Django 3.1.14 on 2022-06-07 05:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0005_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.BigIntegerField()),
                ('date', models.DateField(verbose_name=datetime.datetime.today)),
                ('status', models.BooleanField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook.user_regis')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook.product')),
            ],
        ),
    ]
