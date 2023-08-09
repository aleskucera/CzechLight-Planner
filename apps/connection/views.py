import json
from copy import deepcopy

from django.http import JsonResponse
from apps.nodes.models import Device, TerminationPoint
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

from .planner import find_path


def get_graph_data(nodes: list) -> dict:
    """Generates a dictionary of nodes and links for the network graph.

    Parameters:
        nodes (list): A list of all devices and termination points in the network.

    Returns:
        dict: A dictionary containing the nodes and links for the network graph.
    """
    graph_data = {
        'nodes': [],
        'links': [],
    }

    for node in nodes:

        graph_data['nodes'].append({
            'id': node.name,
            'type': node.type if isinstance(node, Device) else 'termination_point',
        })

        for link in node.list_links(nodes):
            graph_data['links'].append({
                'source': node.name,
                'target': link[0].name,
                'type': link[1],
                'selected': False,
            })

    return graph_data


def remove_zero_length_links(links):
    return [link for link in links if link['source_coords'] != link['target_coords']]


def remove_duplicate_links(links):
    unique_links = {}
    for link in links:
        src, dst = sorted([link['source'], link['target']])
        key = (src, dst)
        if key not in unique_links:
            unique_links[key] = {
                'source': src,
                'target': dst,
                'source_coords': link['source_coords'],
                'target_coords': link['target_coords'],
                'type': link['type'],
                'selected': False,
            }

    return list(unique_links.values())


def get_map_data(devices: list) -> dict:
    """Generates a dictionary of nodes and links for the network graph in map.

    Parameters:
        devices (list): A list of all devices in the network.

    Returns:
        dict: A dictionary containing the nodes and links for the network graph in map.
    """

    graph_data = {
        'nodes': [],
        'links': [],
    }

    for device in devices:
        graph_data['nodes'].append({
            'id': device.name,
            'type': device.type,
            'latitude': device.latitude,
            'longitude': device.longitude,
        })

        for link in device.list_links(devices):
            graph_data['links'].append({
                'source': device.name,
                'target': link[0].name,
                'source_coords': [device.longitude, device.latitude],
                'target_coords': [link[0].longitude, link[0].latitude],
                'type': link[1],
                'selected': False
            })

    graph_data['links'] = remove_zero_length_links(graph_data['links'])
    graph_data['links'] = remove_duplicate_links(graph_data['links'])

    return graph_data


def select_path(path: dict, graph_data: dict, map_data: dict) -> tuple:
    """Selects the links in the path in the graph and map data.

    Parameters:
        path (dict): A dictionary containing the path information.
        graph_data (dict): A dictionary containing the nodes and links for the network graph.
        map_data (dict): A dictionary containing the nodes and links for the network graph in map.

    Returns:
        tuple: A tuple containing the graph and map data with the links in the path selected.
    """

    for i in range(len(path['nodes']) - 1):
        dev_a = path['nodes'][i]
        dev_b = path['nodes'][i + 1]

        for link in graph_data['links']:
            if link['source'] == dev_a and link['target'] == dev_b:
                link['selected'] = True
            elif link['source'] == dev_b and link['target'] == dev_a:
                link['selected'] = True

        for link in map_data['links']:
            if link['source'] == dev_a and link['target'] == dev_b:
                link['selected'] = True
            elif link['source'] == dev_b and link['target'] == dev_a:
                link['selected'] = True

    return graph_data, map_data


@csrf_exempt
def get_path(request):
    devices = Device.objects.all()
    termination_points = TerminationPoint.objects.all()
    nodes = list(devices) + list(termination_points)
    graph_data = get_graph_data(nodes)
    map_data = get_map_data(devices)

    if request.method == 'POST':
        source_id = request.POST.get('tp_a')
        destination_id = request.POST.get('tp_b')

        source = get_object_or_404(TerminationPoint, pk=source_id)
        destination = get_object_or_404(TerminationPoint, pk=destination_id)

        paths = find_path(source, destination, nodes)

        response = dict()
        for name, path in paths.items():
            path_graph_data, path_map_data = select_path(path, deepcopy(graph_data), deepcopy(map_data))
            response[name] = dict(graph_data=path_graph_data,
                                  map_data=path_map_data,
                                  path_text=str(path),
                                  tp_a_id=source_id,
                                  tp_b_id=destination_id)

        return JsonResponse(response)

    return render(request, 'connection/find_path.html',
                  {'termination_points': termination_points,
                   'graph_data': json.dumps(graph_data),
                   'map_data': json.dumps(map_data)})


def test(request):
    return render(request, 'connection/test.html')
