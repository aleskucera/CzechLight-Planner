from collections import deque


class Device(object):
    def __init__(self, name: str):
        self.name = name

    def neighbors(self, in_connection: str = None):
        raise NotImplementedError

    def get_path(self, target):
        visited, frontier = set(), deque()

        initial_state = State(device=self, in_connection=None, parent=None)
        frontier.extend(initial_state.children())

        while frontier:
            current_state = frontier.popleft()
            if current_state.is_target(target):
                return current_state.construct_path()

            if current_state not in visited:
                visited.add(current_state)
                frontier.extend(current_state.children())

        return False

    def __eq__(self, other):
        return self.name == other.name and type(self) == type(other)

    def __repr__(self):
        return f'{self.name} - {type(self).__name__}'

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return hash((self.name, type(self)))


class State(object):
    def __init__(self, device: Device, in_connection: str = None, parent=None):
        self.device = device
        self.parent = parent
        self.in_connection = in_connection

    def children(self):
        devices, connection_types = self.device.neighbors(self.in_connection)
        return [State(d, c, self) for d, c in zip(devices, connection_types)]

    def is_target(self, target: Device):
        return self.device == target

    def construct_path(self):
        path, state = [], self
        while state.parent is not None:
            path.append(state)
            state = state.parent
        path.append(state)
        return path[::-1]

    def __eq__(self, other):
        return self.device == other.device and self.in_connection == other.in_connection

    def __repr__(self):
        return f'{self.in_connection} - {self.device.name}'

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return hash((self.device, self.in_connection))


class LineDegreeROADM(Device):
    def __init__(self, name: str):
        super().__init__(name)
        self.line_conn = None
        self.intra_conn = {f'port_{i + 1}': None for i in range(10)}

    @property
    def num_intra_conn(self):
        return len([d for d in self.intra_conn.values() if d is not None])

    def neighbors(self, in_connection: str = None):
        devices, connection_types = [], []

        if in_connection == 'LineConnection' or in_connection is None:
            devices.extend([d for d in self.intra_conn.values() if d is not None])
            connection_types.extend(['IntraConnection'] * self.num_intra_conn)

        if in_connection == 'IntraConnection' or in_connection is None:
            devices.append(self.line_conn)
            connection_types.append('LineConnection')

        return devices, connection_types


class AddDropROADM(Device):
    def __init__(self, name: str):
        super().__init__(name)
        self.intra_conn = {f'port_{i + 1}': None for i in range(8)}
        self.client_conn = {f'port_{i + 1}': None for i in range(20)}

    @property
    def num_intra_conn(self):
        return len([d for d in self.intra_conn.values() if d is not None])

    @property
    def num_client_conn(self):
        return len([d for d in self.client_conn.values() if d is not None])

    def neighbors(self, in_connection: str = None):
        devices, connection_types = [], []

        if in_connection == 'IntraConnection' or in_connection is None:
            devices.extend([d for d in self.client_conn.values() if d is not None])
            connection_types.extend(['ClientConnection'] * self.num_client_conn)

        if in_connection == 'ClientConnection' or in_connection is None:
            devices.extend([d for d in self.intra_conn.values() if d is not None])
            connection_types.extend(['IntraConnection'] * self.num_intra_conn)

        return devices, connection_types


class Client(Device):
    def __init__(self, name: str):
        super().__init__(name)
        self.client_conn = None

    def neighbors(self, in_connection: str = None):
        devices, connection_types = [], []

        if in_connection is None:
            devices.append(self.client_conn)
            connection_types.append('ClientConnection')

        return devices, connection_types


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
