from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class Auction(models.Model):
    uname=models.CharField(max_length=50)
    bid=models.IntegerField(default=0)

class Items(models.Model):
    title=models.CharField(max_length=25)
    sold=models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/')
    slug = models.SlugField(default="", blank=True,null=False, db_index=True)
    bid=models.IntegerField(default=0)
    highest=models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title}"

class Bids(models.Model):
    item = models.SlugField(default="", blank=True,null=False, db_index=True)
    name=models.CharField(max_length=25)
    bid=models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.bid}"
    
class Search(models.Model):
    title=models.CharField(max_length=25)
