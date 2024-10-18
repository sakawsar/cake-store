from django.contrib import admin

# Register your models here.
from .models import Product, Menu

admin.site.register(Product)
admin.site.register(Menu)