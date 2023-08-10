from apps.nodes.models import Device
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a test network of devices.'

    def handle(self, *args, **kwargs):
        ld1 = Device(
            type='line_degree',
            subtype='default',
            name='LD1',
            description='Line Degree 1 (Ceske Budejovice -> Praha)',
            latitude=48.98218183790268,
            longitude=14.47612526485368,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD6'
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
            description='Line Degree 2 (Ceske Budejovice -> Brno)',
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
            description='Line Degree 3 (Brno -> Ceske Budejovice)',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.3',
            links=dict(
                line=dict(
                    port_1='LD2'
                ),
                intra=dict(
                    port_1='LD4',
                    port_2='LD5',
                    port_3='AD2'
                )
            )
        )

        ld4 = Device(
            type='line_degree',
            subtype='default',
            name='LD4',
            description='Line Degree 4 (Brno -> Praha)',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.4',
            links=dict(
                line=dict(
                    port_1='LD7'
                ),
                intra=dict(
                    port_1='LD3',
                    port_2='LD5',
                    port_3='AD2'
                )
            )
        )

        ld5 = Device(
            type='line_degree',
            subtype='default',
            name='LD5',
            description='Line Degree 5 (Brno -> Olomouc)',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.5',
            links=dict(
                line=dict(
                    port_1='LD11'
                ),
                intra=dict(
                    port_1='LD3',
                    port_2='LD4',
                    port_3='AD2'
                )
            )
        )

        ld6 = Device(
            type='line_degree',
            subtype='default',
            name='LD6',
            description='Line Degree 6 (Praha -> Ceske Budejovice)',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD1'
                ),
                intra=dict(
                    port_1='LD7',
                    port_2='LD8',
                    port_3='LD9',
                    port_4='AD3'
                )
            )
        )

        ld7 = Device(
            type='line_degree',
            subtype='default',
            name='LD7',
            description='Line Degree 6 (Praha -> Brno)',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD4'
                ),
                intra=dict(
                    port_1='LD6',
                    port_2='LD8',
                    port_3='LD9',
                    port_4='AD3'
                )
            )
        )

        ld8 = Device(
            type='line_degree',
            subtype='default',
            name='LD8',
            description='Line Degree 8 (Praha -> Olomouc)',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD10'
                ),
                intra=dict(
                    port_1='LD6',
                    port_2='LD7',
                    port_3='LD9',
                    port_4='AD3'
                )
            )
        )

        ld9 = Device(
            type='line_degree',
            subtype='default',
            name='LD9',
            description='Line Degree 9 (Praha -> Usti nad Labem)',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD12'
                ),
                intra=dict(
                    port_1='LD6',
                    port_2='LD7',
                    port_3='LD8',
                    port_4='AD3'
                )
            )
        )

        ld10 = Device(
            type='line_degree',
            subtype='default',
            name='LD10',
            description='Line Degree 10 (Olomouc -> Praha)',
            latitude=49.59598688997882,
            longitude=17.248885224033778,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD8'
                ),
                intra=dict(
                    port_1='LD11',
                    port_2='AD4'
                )
            )
        )

        ld11 = Device(
            type='line_degree',
            subtype='default',
            name='LD11',
            description='Line Degree 11 (Olomouc -> Brno)',
            latitude=49.59598688997882,
            longitude=17.248885224033778,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD5'
                ),
                intra=dict(
                    port_1='LD10',
                    port_2='AD4'
                )
            )
        )

        ld12 = Device(
            type='line_degree',
            subtype='default',
            name='LD12',
            description='Line Degree 12 (Usti nad Labem -> Praha)',
            latitude=50.66670406117403,
            longitude=14.059224186273752,
            ip_address='192.168.0.1',
            links=dict(
                line=dict(
                    port_1='LD9'
                ),
                intra=dict(
                    port_1='AD5'
                )
            )
        )

        ad1 = Device(
            type='add_drop',
            subtype='wss',
            name='AD1',
            description='Add Drop 1 (Ceske Budejovice)',
            latitude=48.98218183790268,
            longitude=14.47612526485368,
            ip_address='192.168.0.1',
            links=dict(
                intra=dict(
                    port_1='LD1',
                    port_2='LD2'
                ),
                client=dict(
                    port_1='TP1',
                    port_2='TP2'
                )
            )
        )

        ad2 = Device(
            type='add_drop',
            subtype='wss',
            name='AD2',
            description='Add Drop 2 (Brno)',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.1',
            links=dict(
                intra=dict(
                    port_1='LD3',
                    port_2='LD4',
                    port_3='LD5'
                ),
                client=dict(
                    port_1='TP3'
                )
            )
        )

        ad3 = Device(
            type='add_drop',
            subtype='wss',
            name='AD3',
            description='Add Drop 3 (Praha)',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.1',
            links=dict(
                intra=dict(
                    port_1='LD6',
                    port_2='LD7',
                    port_3='LD8',
                    port_4='LD9'
                ),
                client=dict(
                    port_1='TP4',
                    port_2='TP5'
                )
            )
        )

        ad4 = Device(
            type='add_drop',
            subtype='wss',
            name='AD4',
            description='Add Drop 4 (Olomouc)',
            latitude=49.59598688997882,
            longitude=17.248885224033778,
            ip_address='192.168.0.1',
            links=dict(
                intra=dict(
                    port_1='LD10',
                    port_2='LD11'
                ),
                client=dict(
                    port_1='TP6',
                    port_2='TP7'
                )
            )
        )

        ad5 = Device(
            type='add_drop',
            subtype='wss',
            name='AD5',
            description='Add Drop 5 (Usti nad Labem)',
            latitude=50.66670406117403,
            longitude=14.059224186273752,
            ip_address='192.168.0.1',
            links=dict(
                intra=dict(
                    port_1='LD12'
                ),
                client=dict(
                    port_1='TP8'
                )
            )
        )

        ld1.save()
        ld2.save()
        ld3.save()
        ld4.save()
        ld5.save()
        ld6.save()
        ld7.save()
        ld8.save()
        ld9.save()
        ld10.save()
        ld11.save()
        ld12.save()

        ad1.save()
        ad2.save()
        ad3.save()
        ad4.save()
        ad5.save()
