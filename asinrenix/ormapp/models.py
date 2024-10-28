from django.db import models
from django.contrib import admin
class Customer (models.Model):
  cid=models.CharField(max_length=20,primary_key="cid")
  account=models.IntegerField()
  name=models.CharField(max_length=20)
  age=models.IntegerField()
  address=models.CharField(max_length=50)
  phone=models.IntegerField()
  
class CustomerAdmin(admin.ModelAdmin):
 list_display=('cid','account','name','age','address','phone')
