# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, DeviceForm
from .models import Device
from django.http import JsonResponse
from django.views.generic.detail import DetailView


def device_page(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('devices:device-page', device_id=device_id)
    else:
        form = DeviceForm(instance=device)
    context = {'device': device, 'form': form}
    return render(request, 'devices/device_page.html', context)


def device_list(request):
    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})


def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devices:device-list')
    else:
        form = DeviceForm()
    return render(request, 'devices/add_device.html', {'form': form})


class DeviceDetailView(DetailView):
    model = Device

    # template_name = "devices/device_detail.html"

    def render_to_response(self, context, **response_kwargs):
        device = self.get_object()
        data = {
            "id": device.id,
            "name": device.name,
            "latitude": device.latitude,
            "longitude": device.longitude,
            "online": device.online
        }
        return JsonResponse(data)
