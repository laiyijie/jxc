from django.db import models


# Create your models here.

class Customer(models.Model):
    category = models.CharField(max_length=127, db_index=True)
    name = models.CharField(max_length=255, unique=True)
    pinyin_key = models.CharField(max_length=127, db_index=True)
    phone = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    ps = models.TextField()

    # should get pinyin head here
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.pinyin_key = ""
        super(Customer, self).save(force_insert, force_update, using, update_fields)
