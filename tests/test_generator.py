import unittest
from graphs.graph_factory import GraphTypes
from graphs.graph_factory import GraphFactory
from graphs.graph_factory import GraphFactoryNoData
from graphs.graph_factory import GraphFactoryAlphaNumeric
from graphs.graph_generator import weakly_connected_graph
from nodeAndRepairNode.nodes import Node
from graphs.graph import Graph


class GraphGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        # self.g.list_nodes = [Node(1), Node(2), Node(3)]
        self.g = Graph([self.n1, self.n2, self.n3])
        self.gf = GraphFactory(1, 10)

    def test_graph_generator(self):
        g = weakly_connected_graph(10, 20, 10, self.gf);
        self.assertEqual(gf., )

        #connections
        #number of nodes
        #number of graphs
        #if connections are valid
        #

