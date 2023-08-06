from apps.nodes.models import TerminationPoint
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Deletes all termination points from the database.'

    def handle(self, *args, **kwargs):
        TerminationPoint.objects.all().delete()
        print('All termination points deleted.')
