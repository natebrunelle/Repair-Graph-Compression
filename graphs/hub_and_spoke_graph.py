"""
These graphs will consist of many nodes all connected
only to one central hub node. This graph should implement
from the top down a guaranteed connected graph rather than the
Graph class' possible bottom-up of creation of a connected graph
"""

from graphs.graph import Graph


class HubAndSpoke(Graph):
    '''
    A hub and spoke representation.
    :param hub: The hub node.
    :param nodes: All other nodes.

    .. note:: The hub points to the nodes. Not the other way around.
    .. warning:: The hub is not included in the list for now.
    '''

    def __init__(self, hub, nodes=None):
        self.hub_node = hub
        super().__init__(nodes)

    def add_edge(self, n1, n2):

        # if the nodes don't exist already, add them
        if n1 not in self.list_nodes:
            self.add_node(n1)
        if n2 not in self.list_nodes:
            self.add_node(n2)

        if n2 not in n1.edges:
            n1.add_edge(n2)

    def delete_edge(self, n1, n2):
        if n1 in n2.edges:
            n1.delete_edge(n2)
        else:
            raise ValueError('Edge does not exist')

    def delete_node(self, n):
        """
        removes the node from the graph,
        clear the adj list therein,
        resets the node.graph_id to None,
        and removes all references other nodes hold to the deleted node
        """
        if n == self.hub_node:
            raise ValueError(
                'Deleting hub node leaves unconnected and misleading graph')

        super().delete_node(n)

    def add_node(self, n):
        """
        Adds a node and connects it to the hub node
        Duplicate nodes will raise an exception
        """
        if n not in self.list_nodes:
            n.graph_id = self.graph_id
            self.list_nodes.append(n)
            n.add_edge(self.hub_node)
        else:
            raise ValueError('Node already exists in graph')
