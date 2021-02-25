from django.db import models

# Create your models here.


class Student(models.Model):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    dob = models.DateField()
    age = models.IntegerField()
    phone = models.IntegerField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    picture = models.ImageField(null=True)
    mark = models.IntegerField(blank=True,null=True)

class Admin(models.Model):

    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
