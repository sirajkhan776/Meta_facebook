# Generated by Django 3.1.14 on 2022-05-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_regis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField(default=1)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
