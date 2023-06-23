# from django.urls import re_path
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from core import consumers
#
# websocket_urlpatterns = [
#     re_path(r'ws/device_status/$', consumers.DeviceStatusConsumer.as_asgi()),
# ]
#
# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ),
# })
