# Generated by Django 3.1.14 on 2022-05-31 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_user_regis_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_regis',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
