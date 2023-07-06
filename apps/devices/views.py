# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import LineDegreeModel, AddDropModel, ClientModel
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from .devices import LineDegreeROADM, AddDropROADM, Client
import json
from .forms import LineDegreeForm

from django.core.serializers import serialize


def serialize_device(device):
    # Define the fields you want to include in the serialized output
    fields = ['name', 'latitude', 'longitude', 'ip_address', 'description']

    # Create a dictionary with the selected fields and their values
    device_data = {field: getattr(device, field) for field in fields}

    return device_data


def device_list(request):
    line_degree_devices = LineDegreeModel.objects.all()
    add_drop_devices = AddDropModel.objects.all()
    client_devices = ClientModel.objects.all()

    devices = list(line_degree_devices) + list(add_drop_devices) + list(client_devices)

    # Serialize the devices using Django's serializer
    devices_json = json.dumps([serialize_device(device) for device in devices])

    return render(request, 'devices/device_list.html', {'devices': devices, 'devices_json': devices_json})


# def device_list(request):
#     line_degree_devices = {d.name: LineDegreeROADM(d) for d in LineDegreeModel.objects.all()}
#     add_drop_devices = {d.name: AddDropROADM(d) for d in AddDropModel.objects.all()}
#     client_devices = {d.name: Client(d) for d in ClientModel.objects.all()}
#     devices = {**line_degree_devices, **add_drop_devices, **client_devices}
#
#     return render(request, 'devices/device_list.html', {'devices': list(devices.values())})

def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device_type = request.POST.get('device-type')

            # Set the device type specific fields
            if device_type == 'lineDegree':
                device.line_conn = request.POST.get('line_connection')
                device.ports = request.POST.get('ports')
            elif device_type == 'addDrop':
                device.ports = request.POST.get('ports')
                device.client_conn = request.POST.get('client_connection')
            elif device_type == 'client':
                device.client_conn = request.POST.get('client_connection')

            device.save()
            return redirect('devices:device-list')
    else:
        form = DeviceForm()
    return render(request, 'devices/add_device.html', {'form': form})


def line_degree_create(request):
    if request.method == 'POST':
        form = LineDegreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devices:device-list')
    else:
        form = LineDegreeForm()
    return render(request, 'devices/add_device.html', {'form': form})

# class DeviceDetailView(DetailView):
#     model = Device
#
#     # template_name = "devices/device_detail.html"
#
#     def render_to_response(self, context, **response_kwargs):
#         device = self.get_object()
#         data = {
#             "id": device.id,
#             "name": device.name,
#             "latitude": device.latitude,
#             "longitude": device.longitude,
#             "online": device.online
#         }
#         return JsonResponse(data)
