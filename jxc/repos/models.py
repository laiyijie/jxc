from django.db import models


# Create your models here.

class Repo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(null=True, blank=True)
    default = models.BooleanField(default=False)

