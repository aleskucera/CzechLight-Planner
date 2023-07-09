from apps.devices.models import DeviceModel


class Device(object):
    def __init__(self, device_model: DeviceModel):
        self.device_model = device_model

        self.id = device_model.id
        self.name = device_model.name

        self.latitude = device_model.latitude
        self.longitude = device_model.longitude
        self.ip_address = device_model.ip_address
        self.description = device_model.description

    def neighbors(self, in_connection: str = None):
        raise NotImplementedError

    def __eq__(self, other):
        return self.name == other.name and type(self) == type(other)

    def __repr__(self):
        return f'{self.name} - {type(self).__name__}'

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return hash((self.name, type(self)))


class LineDegreeROADM(Device):
    def __init__(self, device_model: DeviceModel):
        super().__init__(device_model)
        self.line_conn = None
        self.intra_conn = dict()

    def neighbors(self, in_connection: str = None):
        devices, connection_types = [], []

        if in_connection == 'LineConnection' or in_connection is None:
            devices.extend(self.intra_conn.values())
            connection_types.extend(['IntraConnection'] * len(self.intra_conn))

        if in_connection == 'IntraConnection' or in_connection is None:
            devices.append(self.line_conn)
            connection_types.append('LineConnection')

        return devices, connection_types

    def create_connections(self, devices: dict):
        intra_conns = self.device_model.connections['multi_intra']
        line_conn_name = self.device_model.connections['single_line']

        # Create the line connection
        self.line_conn = devices[line_conn_name] if line_conn_name in devices else None

        # Create the intra connections
        for port, device_name in intra_conns.items():
            if device_name in devices:
                self.intra_conn[port] = devices[device_name]


class AddDropROADM(Device):
    def __init__(self, device_model: DeviceModel):
        super().__init__(device_model)
        self.intra_conn = dict()
        self.client_conn = dict()

    def neighbors(self, in_connection: str = None):
        devices, connection_types = [], []

        if in_connection == 'IntraConnection' or in_connection is None:
            devices.extend(self.client_conn.values())
            connection_types.extend(['ClientConnection'] * len(self.client_conn))

        if in_connection == 'ClientConnection' or in_connection is None:
            devices.extend(self.intra_conn.values())
            connection_types.extend(['IntraConnection'] * len(self.intra_conn))

        return devices, connection_types

    def create_connections(self, devices: dict):
        intra_conns = self.device_model.connections['multi_intra']
        client_conns = self.device_model.connections['multi_client']

        # Create the intra connections
        for port, device_name in intra_conns.items():
            if device_name in devices:
                self.intra_conn[port] = devices[device_name]

        # Create the client connections
        for port, device_name in client_conns.items():
            if device_name in devices:
                self.client_conn[port] = devices[device_name]


class Client(Device):
    def __init__(self, device_model: DeviceModel):
        super().__init__(device_model)
        self.client_conn = None

    def neighbors(self, in_connection: str = None):
        devices, connection_types = [], []

        if in_connection is None:
            devices.append(self.client_conn)
            connection_types.append('ClientConnection')

        return devices, connection_types

    def create_connections(self, devices: dict):
        client_conn_name = self.device_model.connections['single_client']
        self.client_conn = devices[client_conn_name] if client_conn_name in devices else None


if __name__ == '__main__':
    ld1 = LineDegreeROADM('ld1')
    ld2 = LineDegreeROADM('ld2')
    ld3 = LineDegreeROADM('ld3')
    ld4 = LineDegreeROADM('ld4')
    ld5 = LineDegreeROADM('ld5')
    ld6 = LineDegreeROADM('ld6')

    ad1 = AddDropROADM('ad1')
    ad2 = AddDropROADM('ad2')
    ad3 = AddDropROADM('ad3')

    client1 = Client('client1')
    client2 = Client('client2')
    client3 = Client('client3')
    client4 = Client('client4')

    # Configure connections
    ld1.line_conn = ld5
    ld1.intra_conn[0] = ld2
    ld1.intra_conn[1] = ad1

    ld2.line_conn = ld3
    ld2.intra_conn[0] = ld1
    ld2.intra_conn[1] = ad1

    ld3.line_conn = ld2
    ld3.intra_conn[0] = ld4
    ld3.intra_conn[1] = ad2

    ld4.line_conn = ld6
    ld4.intra_conn[0] = ld3
    ld4.intra_conn[1] = ad2

    ld5.line_conn = ld1
    ld5.intra_conn[0] = ld6
    ld5.intra_conn[1] = ad3

    ld6.line_conn = ld4
    ld6.intra_conn[0] = ld5
    ld6.intra_conn[1] = ad3

    ad1.intra_conn[0] = ld1
    ad1.intra_conn[1] = ld2
    ad1.client_conn[0] = client1

    ad2.intra_conn[0] = ld3
    ad2.intra_conn[1] = ld4
    ad2.client_conn[0] = client2

    ad3.intra_conn[0] = ld5
    ad3.intra_conn[1] = ld6
    ad3.client_conn[0] = client3
    ad3.client_conn[1] = client4

    client1.client_conn = ad1
    client2.client_conn = ad2
    client3.client_conn = ad3
    client4.client_conn = ad3

    print(client1.get_path(client4))
