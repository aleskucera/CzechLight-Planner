from apps.nodes.models import TerminationPoint
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a test network of devices.'

    def handle(self, *args, **kwargs):
        tp1 = TerminationPoint(
            name='TP1',
            description='Termination Point 1 (Ceske Budejovice)',
            link='AD1'
        )

        tp2 = TerminationPoint(
            name='TP2',
            description='Termination Point 2 (Ceske Budejovice)',
            link='AD1'
        )

        tp3 = TerminationPoint(
            name='TP3',
            description='Termination Point 3 (Brno)',
            link='AD2'
        )

        tp4 = TerminationPoint(
            name='TP4',
            description='Termination Point 4 (Praha)',
            link='AD3'
        )

        tp5 = TerminationPoint(
            name='TP5',
            description='Termination Point 5 (Praha)',
            link='AD3'
        )

        tp6 = TerminationPoint(
            name='TP6',
            description='Termination Point 6 (Olomouc)',
            link='AD4'
        )

        tp7 = TerminationPoint(
            name='TP7',
            description='Termination Point 7 (Olomouc)',
            link='AD4'
        )

        tp8 = TerminationPoint(
            name='TP8',
            description='Termination Point 8 (Usti nad Labem)',
            link='AD5'
        )

        tp1.save()
        tp2.save()
        tp3.save()
        tp4.save()
        tp5.save()
        tp6.save()
        tp7.save()
        tp8.save()
