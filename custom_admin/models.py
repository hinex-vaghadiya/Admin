from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Admins(AbstractUser):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=40,unique=True)
    mobile_number=models.IntegerField()
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=100)
    profile_pic=models.CharField(default=" ",null=False)

