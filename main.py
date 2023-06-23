import yaml
from pyvis.network import Network

from devices import LineDegreeROADM, AddDropROADM, Client

device_colors = {'LineDegreeROADM': '#124559',
                 'AddDropROADM': '#598392',
                 'Client': '#d90368'}

connection_colors = {'line_connections': '#c1121f',
                     'intra_connections': '#72b01d',
                     'client_connections': '#fb5607'}


def main():
    with open('network.yaml') as f:
        data = yaml.safe_load(f)

    net = Network()
    devices = []
    device_names = []

    for i, device in enumerate(data):
        dev_type = device['type']
        if dev_type == 'LineDegreeROADM':
            device_names.append(device['name'])
            devices.append(LineDegreeROADM(device['name']))
            net.add_node(i, label=device['name'], title=dev_type, color=device_colors[dev_type], shape='square')
        elif dev_type == 'AddDropROADM':
            device_names.append(device['name'])
            devices.append(AddDropROADM(device['name']))
            net.add_node(i, label=device['name'], title=dev_type, color=device_colors[dev_type], shape='square')
        elif dev_type == 'Client':
            device_names.append(device['name'])
            devices.append(Client(device['name']))
            net.add_node(i, label=device['name'], title=dev_type, color=device_colors[dev_type], shape='dot')

    for i, (dev_data, device) in enumerate(zip(data, devices)):
        dev_type = dev_data['type']
        if dev_type == 'LineDegreeROADM':
            for port, dev_name in dev_data['intra_connections'].items():
                device.intra_conn[port] = devices[device_names.index(dev_name)]
                net.add_edge(i, device_names.index(dev_name), color=connection_colors['intra_connections'], width=4)

            device.line_conn = devices[device_names.index(dev_data['line_connection'])]
            net.add_edge(i, device_names.index(dev_data['line_connection']),
                         color=connection_colors['line_connections'], width=4)

        elif dev_type == 'AddDropROADM':
            for port, dev_name in dev_data['intra_connections'].items():
                device.intra_conn[port] = devices[device_names.index(dev_name)]
                net.add_edge(i, device_names.index(dev_name), color=connection_colors['intra_connections'], width=4)
            for port, dev_name in dev_data['client_connections'].items():
                device.client_conn[port] = devices[device_names.index(dev_name)]
                net.add_edge(i, device_names.index(dev_name), color=connection_colors['client_connections'], width=4)

        elif dev_type == 'Client':
            device.client_conn = devices[device_names.index(dev_data['client_connection'])]
            net.add_edge(i, device_names.index(dev_data['client_connection']),
                         color=connection_colors['client_connections'], width=4)

    net.show('graph.html')

    print(devices)
    path = devices[-1].get_path(devices[-3])
    print(path)


if __name__ == '__main__':
    main()
