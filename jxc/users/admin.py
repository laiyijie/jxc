from django.contrib import admin

from utils.admin_util import add_all_model_to_admin

add_all_model_to_admin("users")
