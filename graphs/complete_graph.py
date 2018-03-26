from graphs.graph import Graph

"""
These graphs will consist exclusively of nodes which
are connected to every other node in the graph
"""


class CompleteGraph(Graph):

    def __init__(self, n_list=None):
        # n_list = None allows us to optionally pass all the nodes we want at start
        if n_list:
            super().__init__(n_list)  # this is a placeholder
            # connect all nodes in n_list here
            # may need to redesign functions or add new functions here.
            # Maybe a hub and spoke function called recursively?
        else:
            super().__init__([])  # this is a more complex option
            # building the complete graph not all at once, dynamically
            # we may not want to support this

    def add_edge(self, n1, n2):
        if n1 not in self.list_nodes or n2 not in self.list_nodes:
            self.add_node(n1)
            self.add_node(n2)
        if n1 not in n2.edges:
            n1.add_edge(n2)  # directed graph

    def delete_edge(self, n1, n2):
        if n1 in self.list_nodes and n2 in self.list_nodes:  # if edge inside graph and not out into cluster
            raise ValueError('Edge removal violates complete graph structure')
            # TODO: maybe this should be a warning, not an error, so it doesn't stop the program?
        else:
            n1.delete_edge(n2)  # directed graph

    def delete_node(self, n):
        """removes the node from the graph,
        clears the adj list therein,
        and removes all references other nodes hold to the deleted node"""
        if n in self.list_nodes:
            # the node and it's list of edges is deleted
            self.list_nodes.remove(n)
            for x in n.edges:
                self.delete_edge(x, n)
            # every outside reference to the node is deleted - costly
            for x in self.list_nodes:  # for all other nodes
                while self.list_nodes[x].edges.count(n) != 0:  # remove n as many times as it appears in edges
                    self.list_nodes[x].edges.remove(n)
        else:
            raise ValueError('Node not in graph')

    def add_node(self, n):  # TODO: Simonne check this
        if n not in self.list_nodes:
            self.list_nodes.append(n)
            for i in range(len(self.list_nodes)):
                self.list_nodes[i].add_edge(n)
        else:
            raise ValueError('Node already in graph')

    """
    Since every node ends up being connected to every other node
    anyway, this method is effectively the same as add_node
    """
    # def add_node_rand(self, n):
    #
    #     return 0

