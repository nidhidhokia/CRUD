from django.db import models

# Create your models here.
class User(models.Model):
    roll_no = models.CharField(max_length=5,default='')
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    division = models.CharField(max_length=10)
    address = models.CharField(max_length=100,default='')