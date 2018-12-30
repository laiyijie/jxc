from django.contrib import admin

# Register your models here.
from utils import admin_util

admin_util.add_all_model_to_admin("products")
