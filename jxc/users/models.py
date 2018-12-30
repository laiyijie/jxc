from django.db import models
from django.db.models import *


class User(models.Model):
    username = CharField(max_length=127)
    password = CharField(max_length=255)
    name = CharField(max_length=127)
