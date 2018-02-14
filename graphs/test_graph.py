import unittest
from graphs.graph import Graph
from nodeAndRepairNode.nodes import Node


class GraphTestCase(unittest.TestCase):

    def setUp(self):
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
        # Note that n4 can still be added even though it's already attached. Should check rand_node.adj_list()

    def test_graph_delete_node(self):
        self.g.delete_node(self.n1)
        # check that n1 no longer listed in other nodes adj_lists() self.g.list_nodes
        # aka check that Node.delete_edge() worked  AssertNotIn(a, b) a not in b
        self.assertEqual(self.g.node_count(), 2)

