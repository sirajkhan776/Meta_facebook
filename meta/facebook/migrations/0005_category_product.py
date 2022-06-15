# Generated by Django 3.1.14 on 2022-06-01 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0004_auto_20220531_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=200)),
                ('img_path', models.ImageField(upload_to='upload/product/')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook.category')),
            ],
        ),
    ]