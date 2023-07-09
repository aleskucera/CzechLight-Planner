from .devices import Device
from collections import deque


def find_path(source: Device, destination: Device):
    visited, frontier = set(), deque()

    initial_state = State(device=source, in_connection=None, parent=None)
    frontier.extend(initial_state.children())

    while frontier:
        current_state = frontier.popleft()
        if current_state.is_target(destination):
            return current_state.construct_path()

        if current_state not in visited:
            visited.add(current_state)
            frontier.extend(current_state.children())

    return False


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
