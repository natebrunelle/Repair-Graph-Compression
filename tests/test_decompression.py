from unittest import TestCase

from graphs.graph import Graph
from nodeAndRepairNode.nodes import Node, RepairNode
from repair.compression import Repair


class RepairDecompress(TestCase):
    ''' Tests the decompress method '''

    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
        self.node4 = Node(4)
        self.node5 = Node(5)

        # setup edges, almost decided to use the add_edge method
        self.node1.edges = [self.node2, self.node3, self.node4, self.node5]
        self.node2.edges = [self.node1, self.node3, self.node4, self.node5]
        self.node3.edges = [self.node1, self.node2, self.node4, self.node5]
        self.node4.edges = [self.node1, self.node2, self.node3, self.node5]
        self.node5.edges = [self.node1, self.node2, self.node3, self.node4]

        self.node_list = [
            self.node1, self.node2, self.node3, self.node4, self.node5
        ]

        self.graph = Graph(self.node_list)

        self.repair = Repair(self.graph)

    def test_empty_graph(self):
        ''' Tests the compress method when the graph is empty '''
        graph = Graph([])
        repair = Repair(graph)

        decompressed = repair.decompress()

        #TODO check back when the graph compare methods are implemented
        self.assertEqual(graph, decompressed,
                         "Empty graph is not empty when decompressed")

    def test_no_compression_nodes(self):
        ''' Tests the decompress when there are no compression nodes '''

        # change the graph to avoid multiple pairing
        self.node1.edges = [self.node2, self.node3, self.node4, self.node5]
        self.node2.edges = [self.node1, self.node5]
        self.node3.edges = [self.node1, self.node2]
        self.node4.edges = [self.node3, self.node5]
        self.node5.edges = []

        self.graph = Graph(self.node_list)
        expected_graph = self.graph

        self.repair = Repair(self.graph)
        self.repair.compress()

        decompressed_graph = self.repair.decompress()
        # self.assertEqual(decompressed_graph,expected_graph, "no compression nodes but graph changed"
        self.fail("Update when the graph equal method is ready")

    def test_multiple_compression_nodes(self):
        ''' Test decompression when multiple compression nodes exist '''

        self.node1.edges = [self.node2, self.node3, self.node4, self.node5]
        self.node2.edges = [self.node1, self.node4, self.node5]
        self.node3.edges = [self.node1, self.node2, self.node4, self.node5]
        self.node4.edges = [self.node3, self.node5]
        self.node5.edges = []

        self.graph = Graph(self.node_list)
        self.repair = Repair(self.graph)
        self.repair.compress()

        compressed_graph = self.repair.decompress()

        expected_graph = None

        self.fail("No useful test yet")

    def test_multiple_run(self):
        ''' Tests a graph that has three compression nodes '''

        compressed_graph = self.repair.compress()
        decompressed_graph = self.repair.decompress()

        self.fail("No useful test yet")
