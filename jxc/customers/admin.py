from django.contrib import admin

from utils import admin_util

admin_util.add_all_model_to_admin("customers")
