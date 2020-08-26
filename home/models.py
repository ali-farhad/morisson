from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    time = models.DateField(default=timezone.now)
    username = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    message = models.CharField(max_length=1000)


class Pricing(models.Model):
    time = models.DateField(default=timezone.now)
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    cname = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    checks = models.CharField(max_length=30)
    message = models.CharField(max_length=1000)

class Jobs(models.Model):
    time = models.DateField(default=timezone.now)
    username = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    role = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    cv = models.CharField(max_length=1000)
