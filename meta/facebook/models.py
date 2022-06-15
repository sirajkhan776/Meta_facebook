import email
from pyexpat import model
from django.db import models

# Create your models here.
import datetime


class user_registeration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField(default=1)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)


class user_regis(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField(default=1)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, default='male')

    def __str__(self):
        return self.first_name


class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class product(models.Model):
    pro_name = models.CharField(max_length=200)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    img_path = models.ImageField(upload_to='upload/product/')
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.pro_name


class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(user_regis, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    mobile = models.BigIntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.pro_name
