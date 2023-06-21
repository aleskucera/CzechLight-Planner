class LineDegreeROADM(object):
    def __init__(self, name: str):
        self.name = name
        self.line_conn = None
        self.express_conn = {i: None for i in range(10)}

    @property
    def children(self):
        return list(self.express_conn.values())

    def __eq__(self, other):
        return self.name == other.name and type(self) == type(other)


class AddDropROADM(object):
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.express_conn = {i: None for i in range(8)}
        self.client_conn = {i: None for i in range(20)}

    @property
    def children(self):
        return list(self.express_conn.values()) + list(self.client_conn.values())

    def __eq__(self, other):
        return self.name == other.name and type(self) == type(other)


class Client(object):
    def __init__(self, name: str):
        self.name = name
        self.client_conn = None

    def __eq__(self, other):
        return self.name == other.name and type(self) == type(other)

    def find_path(self, target):
        frontier = {self.client_conn: self}
        visited = []

        while frontier:
            current = frontier.pop()
            if current == target:
                return True
            visited.append(current)
            for child in current.children:
                if child not in visited:
                    frontier.append(child)


if __name__ == '__main__':
    client1 = Client('client1')
    client2 = Client('client2')

    ad1 = AddDropROADM('ad1')
    ad2 = AddDropROADM('ad2')

    ld1 = LineDegreeROADM('ld1')
    ld2 = LineDegreeROADM('ld2')

    print(client1 == ad1)
