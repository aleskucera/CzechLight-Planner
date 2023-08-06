from apps.nodes.models import Device
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Deletes all devices from the database.'

    def handle(self, *args, **kwargs):
        Device.objects.all().delete()
        print('All devices deleted.')
