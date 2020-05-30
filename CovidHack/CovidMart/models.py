from django.db import models

# Create your models here.
class Customer:
    name = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    zone = models.TextField()
    zoneID = models.IntegerField()
    
class Item:
    itemName = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

class Service:
    type = models.TextField()
    name = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    zone = models.TextField()
    zoneID = models.IntegerField()
