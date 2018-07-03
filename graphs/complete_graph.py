from graphs.graph import Graph


"""
These graphs will consist exclusively of nodes which
are connected to every other node in the graph
"""


class CompleteGraph(Graph):
    def __init__(self):
        # n_list = None allows us to optionally pass all the nodes we want at start

        super().__init__()  # this is a placeholder
        # connect all nodes in n_list here
        # may need to redesign functions or add new functions here.
        # Maybe a hub and spoke function called recursively?
        # building the complete graph not all at once, dynamically
        # we may not want to support this

    def add_edge(self, n1, n2):
        """
        n1 MUST be a node in the CompleteGraph
        n2 MUST be a node outside the graph (in another graph)
        for connecting a CompleteGraph to other graphs,
        NOT for connecting a Complete graph internally.
        """
        if n1.graph_id == self.graph_id and n2.graph_id != self.graph_id:
            n1.add_edge(n2)  # n2 is appended to n1's list, n1->n2

    def delete_edge(self, n1, n2):
        if n1.graph_id == self.graph_id and n2.graph_id == self.graph_id:  # internal edge and not out into cluster
            raise ValueError('Edge removal violates complete graph structure')
            # maybe this should be a warning, not an error, so it doesn't stop the program?
        else:
            n1.delete_edge(n2)  # n1->n2, directed graph

    def delete_node(self, n):
        """removes the node from the graph,
        clears the adj list therein,
        resets the node.graph_id to None,
        and removes all references other nodes hold to the deleted node"""
        # original implementation here moved to graph class b/c general graphs should use it too
        super().delete_node(n)

    def add_node(self, n):
        """
        Adds a node and connects it to all other nodes in the complete graph
        Duplicate nodes fail silently.
        """

        if n not in self.list_nodes:
            n.graph_id = self.graph_id
            self.list_nodes.append(n)
            for i in range(len(self.list_nodes)):
                self.list_nodes[i].add_edge(n)  # should call Node.add_edge
        # else:
        #     raise ValueError('Node already in graph')
