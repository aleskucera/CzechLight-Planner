from collections import deque

from apps.nodes.models import Device, TerminationPoint
from .models import Connection


def find_path(source: TerminationPoint, destination: TerminationPoint, nodes: list) -> Connection:
    """Finds a path between two termination points in the network of connected devices.

    This function performs a Breadth-First Search (BFS) on the state space to explore possible paths
    from the source to the destination termination point.

    Parameters:
        source (TerminationPoint): The starting termination point.
        destination (TerminationPoint): The destination termination point.
        nodes (list): A list of all devices and termination points in the network.

    Returns:
        Connection: An instance of the Connection model representing the paths found.
        The Connection object contains the main path and alternative paths from the source to the destination.
    """

    visited, frontier, counter, connection = set(), deque(), 0, Connection(alternative_paths={})
    connection.save()
    connection.termination_points.add(source, destination)

    initial_state = State(node=source)
    frontier.extend(initial_state.children(nodes))

    while frontier:
        current_state = frontier.popleft()
        if current_state.is_target(destination):
            counter += 1
            if connection.main_path is None:
                connection.main_path = current_state.construct_path()
            connection.alternative_paths[f'path_{counter}'] = current_state.construct_path()
            if counter >= 3:
                break

        if current_state not in visited:
            visited.add(current_state)
            frontier.extend(current_state.children(nodes))

    return connection


class State(object):
    """Represents a state in the state space search.

    Attributes:
        node: The current device or termination point in the state.
        port: The port number connected to the previous state's node through the incoming link.
        link_type: The type of incoming link connected to the previous state's node.
        parent: The parent state from which this state is reached.

    Methods:
        children(nodes: list) -> List[State]: Generate child states from the current state based on neighboring nodes.
        is_target(target) -> bool: Check if the current state is the target state.
        construct_path() -> dict: Construct the path from the initial state to the current state.
    """

    def __init__(self, node, link_type: str = None, port: int = None, parent=None):
        self.node = node
        self.port = port
        self.link_type = link_type

        self.parent = parent

    def children(self, nodes: list):
        """Generate child states from the current state based on neighboring nodes.

        Parameters:
            nodes (list): A list of all devices and termination points in the network.

        Returns:
            List[State]: A list of child states.
        """

        links = self.node.neighbors(nodes, self.link_type)
        return [State(node, link_type, port, self) for node, link_type, port in links]

    def is_target(self, target):
        """Check if the current state is the target state.

        Parameters:
            target: The target termination point.

        Returns:
            bool: True if the current state is the target state, False otherwise.
        """

        return self.node == target

    def construct_path(self):
        """Construct the path from the initial state to the current state.

        Returns:
            dict: A dictionary representing the path with devices, connections, and ports.
        """

        state, path = self, dict(devices=[], link_types=[], ports=[])
        while state.parent is not None:
            if isinstance(state.node, Device):
                path['devices'].append(state.node.name)
                path['link_types'].append(state.link_type)
                path['ports'].append(state.port)

            state = state.parent

        # Reverse the path and take out the first connection
        path['devices'] = path['devices'][::-1]
        path['link_types'] = path['link_types'][:-1][::-1]
        path['ports'] = path['ports'][:-1][::-1]

        return path

    def __eq__(self, other):
        return self.node == other.node and self.link_type == other.link_type and self.port == other.port

    def __repr__(self):
        return f'({self.node}, {self.link_type}, {self.port})'

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return hash((self.node, self.link_type, self.port))
