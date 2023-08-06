from typing import List, Tuple, Optional, Any

from django.db import models
from jsonfield import JSONField


class Device(models.Model):
    """This model represents a device in the network.

    Attributes:
        type (str): The type of device. This is used to determine the device's behavior.
        name (str): The name of the device. This is used to identify the device.
        description (str): A description of the device. This is used to describe the device.
        latitude (float): The latitude of the device. This is used to locate the device.
        longitude (float): The longitude of the device. This is used to locate the device.
        ip_address (str): The IP address of the device. This is used to connect to the device.
        links (dict): The links of the device. This is used to connect the device to other devices.

    Methods:
        port(node: str) -> Optional[int]:
            Returns the port number associated with the given node's name in the device's links.

        neighbors(nodes: List['Device'], link_type: Optional[str] = None) -> List[Tuple['Device', str,
        Tuple[int, Optional[int]]]]:
            Returns a list of neighboring devices along with their link type and port numbers based
            on the provided link_type. If link_type is not provided (None), all neighbors of the device are returned.

        find_links(nodes: List['Device'], link_types: Tuple[str, ...] = ('line', 'intra', 'client')) ->
        List[Tuple['Device', str, Tuple[int, Optional[int]]]]:
            Returns a list of neighboring devices along with their link type and port numbers based on the
            specified link types.
    """

    type = models.CharField(max_length=255)
    subtype = models.CharField(max_length=255, null=True, blank=True)

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    ip_address = models.GenericIPAddressField(blank=True, null=True)

    links = JSONField(default=dict, null=True, blank=True)

    def port(self, node: str) -> Optional[int]:
        """Returns the port number associated with the given node's name in the device's links.

        Parameters:
            node (str): The name of the neighboring node.

        Returns:
            Optional[int]: The port number if the neighboring node is found in the links, otherwise None.
        """

        for link_type in self.links:
            for port, name in self.links[link_type].items():
                if name == node:
                    return port
        return None

    def neighbors(self, nodes: List['Device'], link_type: Optional[str] = None) \
            -> List[Tuple[Any, str, Tuple[Optional[int], Optional[int]]]]:
        """Returns a list of neighboring devices along with their link type and port numbers
        based on the provided link_type. If link_type is not provided (None),
        all neighbors of the device are returned.

        Parameters:
            nodes (List['Device']): The list of all devices in the network.
            link_type (Optional[str]): The type of link to filter the neighbors (e.g., 'line', 'intra', 'client').

        Returns:
            List[Tuple['Device', str, Tuple[int, Optional[int]]]]: A list of neighboring devices
            along with their link type and port numbers.
        """

        assert link_type in [None, 'line', 'intra', 'client']

        if link_type is None:
            return self.list_links(nodes)
        elif link_type == 'line':
            return self.list_links(nodes, ('intra', 'client'))
        elif link_type == 'intra':
            return self.list_links(nodes, ('line', 'client'))
        elif link_type == 'client':
            return self.list_links(nodes, ('line', 'intra'))

    def list_links(self, nodes: list, link_types: Tuple[str, ...] = ('line', 'intra', 'client')) \
            -> List[Tuple[Any, str, Tuple[Optional[int], Optional[int]]]]:
        """Returns a list of neighboring devices along with their link type and port numbers
        based on the specified link types.

        Parameters:
            nodes (List['Device']): The list of all devices in the network.
            link_types (Tuple[str, ...]): The connection types to check for links (e.g., ('line', 'intra', 'client')).

        Returns:
            List[Tuple['Device', str, Tuple[int, Optional[int]]]]: A list of neighboring devices
            along with their link type and port numbers.
        """

        links = []
        for link_type in link_types:

            # Check if the connection type is defined in the connections
            if link_type in self.links:

                # Iterate through the ports and look for the device
                for port, name in self.links[link_type].items():
                    for node in nodes:
                        if node.name == name:
                            links.append((node, link_type, (port, node.port(self.name))))
                            break

        return links

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

    def __hash__(self):
        return hash((self.name, self.type))


class TerminationPoint(models.Model):
    """This model represents a termination point in the network.

    Attributes:
        name (str): The name of the termination point.
        link (str): The name of the device to which this termination point is connected.
        description (str): A description of the termination point.

    Methods:
        port(node: str) -> None:
            Always returns None for termination points.

        neighbors(nodes: list, in_connection: str = None) -> List[Tuple['Device', str, Tuple[int, Optional[int]]]]:
            Returns a list of neighboring devices along with their link type and port numbers for this termination point.
            This method is used to get the neighboring devices of a termination point, which is connected to a device.
    """

    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    @staticmethod
    def port(node: str) -> None:
        """Always returns None for termination points.

        Parameters:
            node (str): The name of the neighboring node.

        Returns:
            None: This method always returns None for termination points.
        """
        return None

    def neighbors(self, nodes: list, link_type: str = None) \
            -> List[Tuple[Any, str, Tuple[Optional[int], Optional[int]]]]:
        """Returns a list of neighboring devices along with their link type and port numbers for this termination point.

        Parameters:
            nodes (list): The list of all devices in the network.
            link_type (str, optional): The connection type to filter the neighbors (e.g., 'client').

        Returns:
            List[Tuple['Device', str, Tuple[int, Optional[int]]]]: A list of neighboring devices along with their
            link type and port numbers.
        """
        assert link_type in [None, 'client']

        if link_type is None:
            return [self.__create_link(self.link, nodes)]
        else:
            return []

    def list_links(self, nodes: list, link_types: Tuple[str, ...] = ('line', 'intra', 'client')) \
            -> List[Tuple[Any, str, Tuple[Optional[int], Optional[int]]]]:
        if 'client' in link_types:
            return [self.__create_link(self.link, nodes)]
        else:
            return []

    def __create_link(self, node_name: str, nodes: list) -> Tuple[Any, str, Tuple[Optional[int], Optional[int]]]:
        for node in nodes:
            if node.name == node_name:
                return node, 'client', (None, node.port(self.name))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.link == other.link

    def __hash__(self):
        return hash((self.name, self.link))
