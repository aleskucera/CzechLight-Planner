# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import json
from .forms import DeviceForm
from .models import DeviceModel
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from apps.device_config import device_ports
from django.http import JsonResponse


def serialize_device(device):
    fields = ['name', 'latitude', 'longitude', 'ip_address', 'description']
    device_data = {field: getattr(device, field) for field in fields}
    return device_data


def device_list(request):
    devices = DeviceModel.objects.all()
    devices_json = json.dumps([serialize_device(device) for device in devices])
    return render(request, 'devices/device_list.html', {'devices': devices, 'devices_json': devices_json})


def debug_device_data(device_data):
    print('Device Data:')
    for key, value in device_data.items():
        print(f'{key}: {value}')


def get_single_conn(request, conn_type):
    device = request.POST.get(f'{conn_type}-connection')
    return device if device else None


def get_multi_conn(request, conn_type):
    ports = request.POST.getlist(f'{conn_type}-port')
    device_names = request.POST.getlist(f'{conn_type}-device-name')
    return {port: device_name for port, device_name in zip(ports, device_names)} if ports else None


def validate_device_form(request):
    """ Validates the device form data and returns True if valid, False otherwise. """
    return True


def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid() and validate_device_form(request):
            device = form.save(commit=False)

            device.connections = dict(
                single_line=get_single_conn(request, 'line'),
                single_intra=get_single_conn(request, 'intra'),
                single_client=get_single_conn(request, 'client'),
                multi_line=get_multi_conn(request, 'line'),
                multi_intra=get_multi_conn(request, 'intra'),
                multi_client=get_multi_conn(request, 'client'),
            )

            # Save the device instance with the updated connections
            device.save()
            return redirect('devices:device-list')
    else:
        form = DeviceForm()
    device_ports_json = json.dumps(device_ports)
    return render(request, 'devices/add_device.html', {'form': form, 'device_ports': device_ports_json})


def device_page(request, device_id):
    device = DeviceModel.objects.get(id=device_id)
    form = DeviceForm(instance=device)
    device_ports_json = json.dumps(device_ports)
    return render(request, 'devices/device_page.html', {'form': form, 'device': device,
                                                        'device_ports': device_ports_json})


class DeviceDetailView(DetailView):
    model = DeviceModel

    # template_name = "devices/device_detail.html"
    def render_to_response(self, context, **response_kwargs):
        device = self.get_object()
        data = {
            "id": device.id,
            "name": device.name,
            "latitude": device.latitude,
            "longitude": device.longitude,
        }
        return JsonResponse(data)
