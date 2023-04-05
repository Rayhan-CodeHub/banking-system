from django.contrib import admin

# Register your models here.
from .templates.models import money_entry_data

admin.site.register((money_entry_data))