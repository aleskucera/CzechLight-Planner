from apps.nodes.models import Device
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a test network of devices.'

    def handle(self, *args, **kwargs):
        ld1 = Device(
            type='line_degree',
            subtype='default',
            name='LD1',
            description='Line Degree 1',
            latitude=48.98218183790268,
            longitude=14.47612526485368,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD5'
                ),
                intra=dict(
                    port_1='LD2',
                    port_2='AD1'
                )
            )
        )

        ld2 = Device(
            type='line_degree',
            subtype='default',
            name='LD2',
            description='Line Degree 2',
            latitude=48.98218183790268,
            longitude=14.47612526485368,
            ip_address='192.168.0.2',
            links=dict(
                line=dict(
                    port_1='LD3'
                ),
                intra=dict(
                    port_1='LD1',
                    port_2='AD1'
                )
            )
        )

        ld3 = Device(
            type='line_degree',
            subtype='default',
            name='LD3',
            description='Line Degree 3',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.3',
            links=dict(
                line=dict(
                    port_1='LD2'
                ),
                intra=dict(
                    port_1='LD4',
                    port_2='AD2'
                )
            )
        )

        ld4 = Device(
            type='line_degree',
            subtype='default',
            name='LD4',
            description='Line Degree 4',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.4',
            links=dict(
                line=dict(
                    port_1='LD6'
                ),
                intra=dict(
                    port_1='LD3',
                    port_2='AD2'
                )
            )
        )

        ld5 = Device(
            type='line_degree',
            subtype='default',
            name='LD5',
            description='Line Degree 5',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.5',
            links=dict(
                line=dict(
                    port_1='LD1'
                ),
                intra=dict(
                    port_1='LD6',
                    port_2='AD3'
                )
            )
        )

        ld6 = Device(
            type='line_degree',
            subtype='default',
            name='LD6',
            description='Line Degree 6',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.6',
            links=dict(
                line=dict(
                    port_1='LD4'
                ),
                intra=dict(
                    port_1='LD5',
                    port_2='AD3'
                )
            )
        )

        ad1 = Device(
            type='add_drop',
            subtype='wss',
            name='AD1',
            description='Add Drop 1',
            latitude=48.98218183790268,
            longitude=14.47612526485368,
            ip_address='192.168.0.7',
            links=dict(
                intra=dict(
                    port_1='LD1',
                    port_2='LD2'
                ),
                client=dict(
                    port_1='TP1'
                )
            )
        )

        ad2 = Device(
            type='add_drop',
            subtype='wss',
            name='AD2',
            description='Add Drop 2',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.8',
            links=dict(
                intra=dict(
                    port_1='LD3',
                    port_2='LD4'
                ),
                client=dict(
                    port_1='TP2'
                )
            )
        )

        ad3 = Device(
            type='add_drop',
            subtype='wss',
            name='AD3',
            description='Add Drop 3',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.9',
            links=dict(
                intra=dict(
                    port_1='LD5',
                    port_2='LD6'
                ),
                client=dict(
                    port_1='TP3',
                    port_2='TP4'
                )
            )
        )

        ld1.save()
        ld2.save()
        ld3.save()
        ld4.save()
        ld5.save()
        ld6.save()

        ad1.save()
        ad2.save()
        ad3.save()
