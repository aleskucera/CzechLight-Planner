# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from .views import device_list, line_degree_create

app_name = 'devices'

urlpatterns = [
    path('list/', device_list, name='device-list'),
    path('add/', line_degree_create, name='device-create'),
    # path('device/<int:device_id>/', device_page, name='device-page'),
    # path('api/devices/<int:pk>/', DeviceDetailView.as_view(), name='device-detail')
]
