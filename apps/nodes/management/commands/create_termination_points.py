from apps.nodes.models import TerminationPoint
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a test network of devices.'

    def handle(self, *args, **kwargs):
        tp1 = TerminationPoint(
            name='TP1',
            description='Termination Point 1',
            link='AD1'
        )

        tp2 = TerminationPoint(
            name='TP2',
            description='Termination Point 2',
            link='AD2'
        )

        tp3 = TerminationPoint(
            name='TP3',
            description='Termination Point 3',
            link='AD3'
        )

        tp4 = TerminationPoint(
            name='TP4',
            description='Termination Point 4',
            link='AD3'
        )

        tp1.save()
        tp2.save()
        tp3.save()
        tp4.save()
