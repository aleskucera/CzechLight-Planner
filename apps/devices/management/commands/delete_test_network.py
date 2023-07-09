from apps.devices.models import DeviceModel
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Deletes all devices from the database.'

    def handle(self, *args, **kwargs):
        DeviceModel.objects.all().delete()
        print('All devices deleted.')
