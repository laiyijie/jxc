from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    ps = models.TextField()
