from django.db import models
from jsonfield import JSONField
from apps.device_config import device_types


class DeviceModel(models.Model):
    type = models.CharField(max_length=255, choices=device_types)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    ip_address = models.GenericIPAddressField()

    connections = JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
