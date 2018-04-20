from graphs.graph import Graph


"""
These graphs will consist of many nodes all connected
only to one central hub node.
This graph should implement from the top down a guaranteed connected graph
rather than the Graph class' possible bottom-up of creation of a connected graph
"""


class HubAndSpoke(Graph):
    def __init__(self, hub):
        self.hub_node = hub  # Could set the hub's id to the graph's id, but no reason to
        super().__init__()

    def add_edge(self, n1, n2):
        if self.hub_node not in (n1, n2):
            raise ValueError(
                'Hub node not targeted'
            )  # wouldn't it be easier to change the parameters?
            # Or overriding, so can't? IDK.  Is it necessary to override/can we create a new function?
        else:
            if n2 not in n1.edges:
                n1.add_edge(n2)  # n2 is appended to n1's list

    def delete_edge(self, n1, n2):
        if n1 in n2.edges:
            n1.delete_edge(n2)
        # else:
        #     raise ValueError('Edge does not exist')  # should exit quietly instead?

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
        Duplicate nodes fail silently.
        """
        if n not in self.list_nodes:
            n.graph_id = self.graph_id
            self.list_nodes.append(n)
            n.add_edge(self.hub_node)
        # else:
        #     raise ValueError('Node already exists in graph')
        #     # exit/fail quietly w/out error b/c called by other functions

    """
    Not necessary since an add is not allowed unless the hub is
    targeted; adding a random node is effectively no different
    than adding a particular node
    """
    # def add_node_rand(self, n):
