# Ex02 Django ORM Web Application
## Date: 27/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot (3).png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
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

from django.contrib import admin
from .models import Customer,CustomerAdmin
admin.site.register(Customer,CustomerAdmin)


## OUTPUT

![alt text](<Screenshot (1)-1.png>)

 ## RESULT
Thus the program for creating a database using ORM has been executed successfully
