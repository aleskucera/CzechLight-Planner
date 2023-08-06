# tasks.py

import subprocess
from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


@shared_task
def print_message():
    print('Hello, world!')


@shared_task
def check_ping(ip_address):
    try:
        output = subprocess.check_output(["ping", "-c", "1", "-W", "1", ip_address])
        print(output)
        return True
    except subprocess.CalledProcessError:
        print(f"Device with IP address {ip_address} is offline.")
        return False

# @shared_task
# def update_device_online_status():
#     device_list = Device.objects.all()
#     for device in device_list:
#         online = check_ping(device.ip_address)
#         # online = check_ping('10.0.154.94')
#         device.online = online
#         device.save()
#
#         if device.online != online:
#             device.online = online
#             device.save()
#             async_to_sync(channel_layer.group_send)(
#                 'device_status',
#                 {
#                     'type': 'device_status_message',
#                     'id': device.id,
#                     'online': online,
#                 }
#             )
