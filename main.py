import yaml
from pyvis.network import Network

from devices import LineDegreeROADM, AddDropROADM, Client

device_colors = {'LineDegreeROADM': '#22577a',
                 'AddDropROADM': '#57cc99',
                 'Client': '#c7f9cc'}

connection_colors = {'LongConnection': '#4f000b',
                     'ExpressConnection': '#720026',
                     'ClientConnection': '#ce4257'}


def main():
    with open('network.yaml') as f:
        data = yaml.safe_load(f)

    net = Network()

    for i, device in enumerate(data):
        assert device['type'] in device_colors.keys()
        net.add_node(i, label=device['name'], title=device['type'], color=device_colors[device['type']])

    net.show('graph.html')  # save visualization in 'graph.html'


if __name__ == '__main__':
    main()

# net = Network()  # create graph object
#
# # add nodes
# net.add_nodes(
#     [1, 2, 3, 4, 5],  # node ids
#     label=['Node #1', 'Node #2', 'Node #3', 'Node #4', 'Node #5'],  # node labels
#     # node titles (display on mouse hover)
#     title=['Main node', 'Just node', 'Just node', 'Just node', 'Node with self-loop'],
#     color=['#d47415', '#22b512', '#42adf5', '#4a21b0', '#e627a3']  # node colors (HEX)
# )
# # add list of edges, same as in the previous example
# net.add_edges([(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)])
#
# net.show('graph.html')  # save visualization in 'graph.html'
