# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# from apps.devices.models import Device
#
#
# class DeviceStatusConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#         async_to_sync(self.channel_layer.group_add)(
#             'device_status',
#             self.channel_name
#         )
#
#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             'device_status',
#             self.channel_name
#         )
#
#     def device_status_message(self, event):
#         self.send(text_data=json.dumps({
#             'type': 'device_status',
#             'id': event['id'],
#             'online': event['online'],
#         }))
