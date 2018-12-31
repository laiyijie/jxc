from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=127)


class ProductInfo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=127, db_index=True)
    spec = models.CharField(max_length=127)
    unit = models.CharField(max_length=127)
    active = models.BooleanField(default=True)
    # statistic info
    price = models.IntegerField()
    total_count = models.IntegerField()
