from django.urls import path
from .views import device_list, device_create, device_page, DeviceDetailView

app_name = 'devices'

urlpatterns = [
    path('list/', device_list, name='device-list'),
    path('add/', device_create, name='device-create'),
    path('device/<int:device_id>/', device_page, name='device-page'),
    path('api/device/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
]
