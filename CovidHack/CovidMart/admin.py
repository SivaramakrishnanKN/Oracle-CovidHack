from django.contrib import admin
from .models import Customer, Item, Service
# Register your models here.
admin.register(Customer,Item,Service)(admin.ModelAdmin)
