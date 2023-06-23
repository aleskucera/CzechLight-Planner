from django.db import models


# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    color = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    online = models.BooleanField(default=False)

# class Node(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     description = models.TextField(blank=True)
#
# class Device2(models.Model):
#     name = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     ip_address = models.GenericIPAddressField()
#     user = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     leaf_ports = models.TextField(blank=True)


