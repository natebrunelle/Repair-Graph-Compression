"""
These graphs will consist exclusively of nodes which
are connected to every other node in the graph
"""

from graphs.graph import Graph

class CompleteGraph(Graph):
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
            for n in self.list_nodes:
                if n != node:
                    node.add_edge(n)

    def add_edge(self, n1, n2):
        """
        :param n1: MUST be a node in the CompleteGraph
        :paam n2: MUST be a node outside the graph (in another graph)

        for connecting a CompleteGraph to other graphs,
        NOT for connecting a Complete graph internally.
        """
        if n1.graph_id == self.graph_id and n2.graph_id != self.graph_id:
            n1.add_edge(n2)
        else:
            raise ValueError('Don\'t use this method to connect a complete graph internally')

    def delete_edge(self, n1, n2):
        # internal edge and not out into cluster
        if n1.graph_id == self.graph_id and n2.graph_id == self.graph_id:
            raise ValueError('Edge removal violates complete graph structure')
        else:
            n1.delete_edge(n2)

    def delete_node(self, n):
        """removes the node from the graph,
        clears the adj list therein,
        resets the node.graph_id to None,
        and removes all references other nodes hold to the deleted node"""

        super().delete_node(n)

    def add_node(self, n):
        """
        Adds a node and connects it to all other nodes in the complete graph
        Duplicate nodes fail silently.
        """

        if n not in self.list_nodes:
            n.graph_id = self.graph_id
            self.list_nodes.append(n)
            for node in self.list_nodes:
                if node != n:
                    n.add_edge(node)
                    node.add_edge(n)
                '''
            for i in range(len(self.list_nodes)):
                self.list_nodes[i].add_edge(n)
                '''
        else:
             raise ValueError('Node already in graph')
