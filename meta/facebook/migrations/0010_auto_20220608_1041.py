# Generated by Django 3.1.14 on 2022-06-08 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0009_auto_20220608_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_name',
            new_name='product',
        ),
    ]