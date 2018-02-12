import unittest
from graphs.graph import Graph
from nodes import Node  # need to merge branches and fix directory structure to resolve this. 


class GraphTestCase(unittest.TestCase):

    def setUp(self):
        # some stuff here
        # need nodes
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        # self.g.list_nodes = [Node(1), Node(2), Node(3)]
        self.g = Graph([self.n1, self.n2, self.n3], 3)

    def test_graph_add_node_edge(self):
        self.g.add_node(self.n4)
        self.g.add_edge(self.n1, self.n4)  # could potentially fail if n1 randomly selected in add_node

    def test_graph_add_edge_node(self):
        self.g.add_edge(self.n1, self.n4)
        self.g.add_node(self.n4)  # adds an edge between random node and n4.
        # Note that n4 can still be added even though it's already attached.

