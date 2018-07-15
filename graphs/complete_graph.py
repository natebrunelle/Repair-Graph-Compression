"""
These graphs will consist exclusively of nodes which
are connected to every other node in the graph

"""

from graphs.graph import Graph


class CompleteGraph(Graph):
    '''
    A representation of a complete graph based on the more
    general `Graph` class. It ensures all nodes are connected
    all the time.

    .. note:: It will reject changes to the graph that might
              cause it to lose this property.

    '''

    def __init__(self, n_list=None):

        super().__init__()

        # process the new nodes
        if n_list:
            self.connect_all_nodes(n_list)

    def connect_all_nodes(self, n_list):
        '''
        :param n_list: A list of new nodes.

        Adds a group of new nodes to the internal list,
        and connects them to each other. This should be used
        from __init__ only for the most part.
        '''
        for node in n_list:
            node.graph_id = self.graph_id
            self.list_nodes.append(node)

        for node in n_list:
            for ref_node in self.list_nodes:
                if ref_node != node:
                    node.add_edge(ref_node)

    def add_edge(self, node1, node2):
        """
        :param node1: MUST be a node in the CompleteGraph
        :paam node2: MUST be a node outside the graph (in another graph)

        for connecting a CompleteGraph to other graphs,
        NOT for connecting a Complete graph internally.
        """
        if node1.graph_id == self.graph_id and node2.graph_id != self.graph_id:
            node1.add_edge(node2)
        else:
            raise ValueError(
                'Don\'t use this method to connect a complete graph internally'
            )

    def delete_edge(self, node1, node2):
        # internal edge and not out into cluster
        if node1.graph_id == self.graph_id and node2.graph_id == self.graph_id:
            raise ValueError('Edge removal violates complete graph structure')
        else:
            node1.delete_edge(node2)

    def add_node(self, node):
        """
        Adds a node and connects it to all other nodes in the complete graph
        Duplicate nodes fail silently.
        """

        if node not in self.list_nodes:
            node.graph_id = self.graph_id
            self.list_nodes.append(node)
            for ref_node in self.list_nodes:
                if ref_node != node:
                    node.add_edge(ref_node)
                    ref_node.add_edge(node)
        else:
            raise ValueError('Node already in graph')
