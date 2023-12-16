from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
# Create your models here.

class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    user_name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

class Signup(models.Model):
    user_name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)