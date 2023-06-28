from django.db import models
from jsonfield import JSONField


class DeviceModel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    ip_address = models.GenericIPAddressField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        abstract = True


class LineDegreeModel(DeviceModel):
    line_conn = models.CharField(max_length=255, null=True, blank=True)
    ports = JSONField(null=True, blank=True)


class AddDropModel(DeviceModel):
    ports = JSONField(null=True, blank=True)
    client_conn = models.CharField(max_length=255, null=True, blank=True)


class ClientModel(DeviceModel):
    client_conn = models.CharField(max_length=255, null=True, blank=True)
