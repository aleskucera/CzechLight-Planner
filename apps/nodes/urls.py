from django.urls import path
from .views import device_list, device_page, device_detail_view, termination_points_list, termination_point_page, \
    termination_point_detail_view

app_name = 'nodes'

urlpatterns = [
    path('device-list/', device_list, name='device-list'),
    # path('add-device/', device_create, name='device-create'),
    path('device/<int:pk>/', device_page, name='device-page'),
    path('api/device/<int:pk>/', device_detail_view, name='device-detail'),
    path('list-termination-points/', termination_points_list, name='termination-points-list'),
    # # path('add/', device_create, name='device-create'),
    path('termination-point/<int:pk>/', termination_point_page, name='termination-point-page'),
    path('api/termination-point/<int:pk>/', termination_point_detail_view, name='termination-point-detail'),
]
