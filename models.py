from django.db import models
from .models import *


# Create your models here.
class tblcontact(models.Model):
    name=models.CharField(max_length=70,null=True)
    email=models.EmailField(max_length=100,null=True)
    mobile=models.CharField(max_length=20,null=True)
    message=models.TextField(null=True)


class tblgallery(models.Model):
    title=models.CharField(max_length=100,null=True)
    picture=models.ImageField(upload_to="static/gallery/",null=True)

class tblcategory(models.Model):
    title=models.CharField(max_length=100,null=True)
    picture=models.ImageField(upload_to="static/category/",null=True,blank=True)
    def __str__(self):
        return self.title


class tblproduct(models.Model):
    title= models.CharField(max_length=300)
    product_info=models.TextField(null=True)
    product_category=models.ForeignKey(tblcategory,on_delete=models.CASCADE,null=True)
    price=models.FloatField(null=True)
    discounted_price=models.FloatField(null=True)
    weight=models.CharField(max_length=80,null=True)
    picture=models.ImageField(upload_to="static/product/",null=True,blank=True)
    posted_date=models.DateField(null=True)


class tblregister(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(primary_key=True,max_length=100)
    password=models.CharField(max_length=40,null=True)
    mobile=models.CharField(max_length=20,null=True)
    picture=models.ImageField(upload_to="static/userpic/",null=True,blank=True)
    pincode=models.IntegerField(null=True)
    landmark=models.CharField(max_length=100,null=True)
    address=models.TextField(null=True)
    regdate=models.DateField(null=True)


class tblcart(models.Model):
    userid=models.CharField(max_length=50,null=True)
    pid=models.CharField(max_length=50,null=True)
    product_name=models.CharField(max_length=200,null=True)
    product_picture=models.CharField(max_length=200,null=True)
    product_info=models.TextField(null=True)
    product_price=models.CharField(max_length=50,null=True)
    discounted_price=models.CharField(max_length=50,null=True)
    total_price=models.CharField(max_length=50,null=True)
    product_weight=models.CharField(max_length=60,null=True)
    product_quantity=models.CharField(max_length=50,null=True)
    added_date=models.DateField(null=True)

class tblorder(models.Model):
    userid=models.CharField(max_length=50,null=True)
    pid=models.CharField(max_length=50,null=True)
    product_name=models.CharField(max_length=200,null=True)
    product_picture=models.CharField(max_length=200,null=True)
    product_info=models.TextField(null=True)
    product_price=models.CharField(max_length=50,null=True)
    discounted_price=models.CharField(max_length=50,null=True)
    total_price=models.CharField(max_length=50,null=True)
    product_weight=models.CharField(max_length=60,null=True)
    product_quantity=models.CharField(max_length=50,null=True)
    added_date=models.DateField(null=True)
    status=models.CharField(max_length=30,null=True)
