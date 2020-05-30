from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    zone = models.TextField()
    zoneID = models.IntegerField()
    
class Item(models.Model):
    itemName = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

class Service(models.Model):
    type_name = models.TextField()
    name = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    zone = models.TextField()
    zoneID = models.IntegerField()
