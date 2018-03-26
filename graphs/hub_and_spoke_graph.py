from graphs.graph import Graph

"""
These graphs will consist of many nodes all connected
only to one central hub node.
This graph should implement from the top down a guaranteed connected graph 
rather than the Graph class' possible bottom-up of creation of a connected graph
"""


class HubAndSpoke(Graph):

    def __init__(self, hub, nodes=None):
        self.hub_node = hub
        if nodes:
            super().__init__(nodes)
        else:
            super().__init__([])

    def add_edge(self, n1, n2):
        if self.hub_node not in (n1, n2):
            raise ValueError('Hub node not targeted')  # wouldn't it be easier to change the parameters?
            # Or overriding, so can't? IDK.  Is it necessary to override/can we create a new function?
        else:
            if n2 not in n1.edges:  # TODO: fix other classes so they look like this
                n1.add_edge(n2)  # n2 is appended to n1's list

    def delete_edge(self, n1, n2):
        if n1 in n2.edges:
            n1.delete_edge(n2)
        else:
            raise ValueError('Edge does not exist')  # TODO: should exit quietly instead?

    def delete_node(self, n):
        if n in self.list_nodes:
            # TODO: call delete_edge remove n from nodes that list it in otherNode.edge
            # see general Graph class above
            self.list_nodes.remove(n)
            for i in range(len(self.list_nodes)):
                self.list_nodes[i].delete_edge(n)
        else:
            raise ValueError('Node does not exist, cannot be deleted')

    def add_node(self, n):
        if n not in self.list_nodes:
            self.list_nodes.append(n)
            n.add_edge(self.hub_node)
        else:
            raise ValueError('Node already exists in graph')
            # TODO: exit/fail quietly w/out error b/c called by other functions

    """
    Not necessary since an add is not allowed unless the hub is
    targeted; adding a random node is effectively no different
    than adding a particular node
    """
    # def add_node_rand(self, n):
    #