from apps.devices.models import DeviceModel
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a test network of devices.'

    def handle(self, *args, **kwargs):
        ld1 = DeviceModel(
            type='line_degree',
            name='LD1',
            description='Line Degree 1',
            latitude=48.98218183790268,
            longitude=14.47612526485368,
            ip_address='192.168.0.1',
            connections=dict(
                single_line='LD5',
                multi_intra=dict(
                    port_1='LD2',
                    port_2='AD1'
                )
            )
        )

        ld2 = DeviceModel(
            type='line_degree',
            name='LD2',
            description='Line Degree 2',
            latitude=48.98218183790268,
            longitude=14.47612526485368,
            ip_address='192.168.0.2',
            connections=dict(
                single_line='LD3',
                multi_intra=dict(
                    port_1='LD1',
                    port_2='AD1'
                )
            )
        )

        ld3 = DeviceModel(
            type='line_degree',
            name='LD3',
            description='Line Degree 3',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.3',
            connections=dict(
                single_line='LD2',
                multi_intra=dict(
                    port_1='LD4',
                    port_2='AD2'
                )
            )
        )

        ld4 = DeviceModel(
            type='line_degree',
            name='LD4',
            description='Line Degree 4',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.4',
            connections=dict(
                single_line='LD6',
                multi_intra=dict(
                    port_1='LD3',
                    port_2='AD2'
                )
            )
        )

        ld5 = DeviceModel(
            type='line_degree',
            name='LD5',
            description='Line Degree 5',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.5',
            connections=dict(
                single_line='LD1',
                multi_intra=dict(
                    port_1='LD6',
                    port_2='AD3'
                )
            )
        )

        ld6 = DeviceModel(
            type='line_degree',
            name='LD6',
            description='Line Degree 6',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.6',
            connections=dict(
                single_line='LD4',
                multi_intra=dict(
                    port_1='LD5',
                    port_2='AD3'
                )
            )
        )

        ad1 = DeviceModel(
            type='wss_add_drop',
            name='AD1',
            description='Add Drop 1',
            latitude=48.98218183790268,
            longitude=14.47612526485368,
            ip_address='192.168.0.7',
            connections=dict(
                multi_intra=dict(
                    port_1='LD1',
                    port_2='LD2'
                ),
                multi_client=dict(
                    port_1='C1'
                )
            )
        )

        ad2 = DeviceModel(
            type='wss_add_drop',
            name='AD2',
            description='Add Drop 2',
            latitude=49.199348820265804,
            longitude=16.607827206488952,
            ip_address='192.168.0.8',
            connections=dict(
                multi_intra=dict(
                    port_1='LD3',
                    port_2='LD4'
                ),
                multi_client=dict(
                    port_1='C2'
                )
            )
        )

        ad3 = DeviceModel(
            type='wss_add_drop',
            name='AD3',
            description='Add Drop 3',
            latitude=50.086228105241084,
            longitude=14.439678023707962,
            ip_address='192.168.0.9',
            connections=dict(
                multi_intra=dict(
                    port_1='LD5',
                    port_2='LD6'
                ),
                multi_client=dict(
                    port_1='C3',
                    port_2='C4'
                )
            )
        )

        c1 = DeviceModel(
            type='client',
            name='C1',
            description='Client 1',
            latitude=48.95084884802407,
            longitude=14.443268377550638,
            ip_address='192.168.0.10',
            connections=dict(
                single_client='AD1'
            )
        )

        c2 = DeviceModel(
            type='client',
            name='C2',
            description='Client 2',
            latitude=49.20821705408701,
            longitude=16.68109554741428,
            ip_address='192.168.0.11',
            connections=dict(
                single_client='AD2'
            )

        )

        c3 = DeviceModel(
            type='client',
            name='C3',
            description='Client 3',
            latitude=50.1594862922319,
            longitude=14.52605511755838,
            ip_address='192.168.0.12',
            connections=dict(
                single_client='AD3'
            )
        )

        c4 = DeviceModel(
            type='client',
            name='C4',
            description='Client 4',
            latitude=50.1594862922319,
            longitude=14.52605511755838,
            ip_address='192.168.0.13',
            connections=dict(
                single_client='AD3'
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

        c1.save()
        c2.save()
        c3.save()
        c4.save()
