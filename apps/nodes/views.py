# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import json
from django.http import JsonResponse
from apps.device_config import device_ports
from django.shortcuts import render, get_object_or_404

from .models import Device, TerminationPoint
from .forms import DeviceForm, TerminationPointForm


def serialize_device(device: Device) -> dict:
    fields = ['type', 'subtype', 'name', 'latitude', 'longitude', 'ip_address', 'description']
    return {field: getattr(device, field) for field in fields}


def device_list(request: object) -> object:
    devices = Device.objects.all()
    devices_json = json.dumps([serialize_device(device) for device in devices])
    return render(request, 'nodes/device_list.html', {'devices': devices, 'devices_json': devices_json})


def device_page(request: object, pk: int) -> object:
    device = get_object_or_404(Device, pk=pk)
    form = DeviceForm(instance=device)
    device_ports_json = json.dumps(device_ports)
    return render(request, 'nodes/device_page.html', {'form': form, 'device': device,
                                                      'device_ports': device_ports_json})


def device_detail_view(request: object, pk: int) -> object:
    device = get_object_or_404(Device, pk=pk)
    data = {
        "id": device.id,
        "name": device.name,
        "type": device.type,
        "subtype": device.subtype,
        "latitude": device.latitude,
        "longitude": device.longitude,
        "ip_address": device.ip_address,
        "description": device.description,
    }
    return JsonResponse(data)


def serialize_termination_point(termination_point: TerminationPoint) -> dict:
    fields = ['name', 'link', 'description']
    return {field: getattr(termination_point, field) for field in fields}


def termination_points_list(request: object) -> object:
    termination_points = TerminationPoint.objects.all()
    termination_points_json = json.dumps([serialize_termination_point(tp) for tp in termination_points])
    return render(request, 'nodes/termination_points_list.html',
                  {'termination_points': termination_points, 'termination_points_json': termination_points_json})


def termination_point_page(request: object, pk: int) -> object:
    tp = get_object_or_404(TerminationPoint, pk=pk)
    form = TerminationPointForm(instance=tp)
    return render(request, 'nodes/termination_point_page.html',
                  {'form': form, 'termination_point': tp})


def termination_point_detail_view(request: object, pk: int) -> object:
    tp = get_object_or_404(TerminationPoint, pk=pk)
    data = {
        "id": tp.id,
        "name": tp.name,
        "type": tp.link,
        "description": tp.description,
    }
    return JsonResponse(data)

#
# def get_single_conn(request, conn_type):
#     device = request.POST.get(f'{conn_type}-connection')
#     return device if device else None
#
#
# def get_multi_conn(request, conn_type):
#     ports = request.POST.getlist(f'{conn_type}-port')
#     device_names = request.POST.getlist(f'{conn_type}-device-name')
#     return {port: device_name for port, device_name in zip(ports, device_names)} if ports else None
#
#
# def validate_device_form(request):
#     """ Validates the device form data and returns True if valid, False otherwise. """
#     return True
#
#
# def device_create(request):
#     if request.method == 'POST':
#         form = DeviceForm(request.POST)
#         if form.is_valid() and validate_device_form(request):
#             device = form.save(commit=False)
#
#             device.connections = dict(
#                 single_line=get_single_conn(request, 'line'),
#                 single_intra=get_single_conn(request, 'intra'),
#                 single_client=get_single_conn(request, 'client'),
#                 multi_line=get_multi_conn(request, 'line'),
#                 multi_intra=get_multi_conn(request, 'intra'),
#                 multi_client=get_multi_conn(request, 'client'),
#             )
#
#             # Save the device instance with the updated connections
#             device.save()
#             return redirect('devices:device-list')
#     else:
#         form = DeviceForm()
#     device_ports_json = json.dumps(device_ports)
#     return render(request, 'devices/add_device.html', {'form': form, 'device_ports': device_ports_json})
#
#
#
