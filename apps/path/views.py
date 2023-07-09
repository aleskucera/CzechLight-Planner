from django.shortcuts import render, redirect
from apps.devices.models import DeviceModel
from django.http import JsonResponse

from .planner import find_path
from .devices import LineDegreeROADM, AddDropROADM, Client

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_path(request):
    device_models = DeviceModel.objects.all()
    devices = dict()
    for device_model in device_models:
        if 'line' in device_model.type:
            devices[device_model.name] = LineDegreeROADM(device_model)
        elif 'add_drop' in device_model.type:
            devices[device_model.name] = AddDropROADM(device_model)
        elif 'client' in device_model.type:
            devices[device_model.name] = Client(device_model)

    for device in devices.values():
        device.create_connections(devices)

    if request.method == 'POST':
        source_id = request.POST.get('source')
        destination_id = request.POST.get('destination')

        source = None
        destination = None

        for device in devices.values():
            if device.id == int(source_id):
                source = device
            elif device.id == int(destination_id):
                destination = device

        path = find_path(source, destination)
        path = [str(state) for state in path]
        response = {
            'result': path
        }
        return JsonResponse(response)

    return render(request, 'path/find_path.html', {'devices': device_models})
