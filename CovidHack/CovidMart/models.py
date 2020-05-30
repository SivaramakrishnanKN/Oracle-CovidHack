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
    itemType = models.CharField(max_length=200, default="")

class Service(models.Model):
    shopType = models.TextField()
    name = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    zone = models.TextField()
    zoneID = models.IntegerField()
    slotID = models.IntegerField()
    numCust = models.IntegerField(default=0)
