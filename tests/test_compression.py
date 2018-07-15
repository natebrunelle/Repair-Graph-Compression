import math
from unittest import TestCase

from graphs.graph import Graph
from nodes.nodes import Node, RepairNode
from repair.repair import Repair, RepairPriorityQueue


def compare_by_value(graph1, graph2):
    ''' compares two graphs by their values

    The UUID based comparison is hard to test since the id's are generated
    randomly on each run. Therefore, the test cases can not properly create
    the expected compressed graph. This method solves that problem for now.

    A better approach might be to find a way to seed the UUID. Will update this
    if I get that to work/if it is possible to do so. '''

    # check length
    if len(graph1.list_nodes) != len(graph2.list_nodes):
        return False

    # check values
    for index in range(len(graph1.list_nodes)):
        if graph1.list_nodes[index].value != graph2.list_nodes[index].value:
            return False

    # they must be equal
    return True


class TestRepairPriorityQueue(TestCase):
    ''' Tests the priority queue implementation '''

    def setUp(self):
        self.queue = RepairPriorityQueue()
        self.graph = Graph([])

    def test_passed_list_queued(self):
        ''' Tests that a list of points passed in are correctly queued '''
        pair_list = list()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)

        graph = Graph([node1, node2, node3, node4, node5, node6, node7, node8])

        pair_list.append((9, (node1, node2)))
        pair_list.append((20, (node3, node4)))
        pair_list.append((87, (node5, node6)))
        pair_list.append((4, (node7, node8)))

        queue = RepairPriorityQueue(pair_list)

        expected = [5, 6, 3, 4, 1, 2, 7, 8]
        actual = list()

        while not queue.empty():
            node = queue.get()
            actual.append(node[1][0].value)
            actual.append(node[1][1].value)

        self.assertEqual(actual, expected,
                         "List injection doesn't get in the right order")

    def test_put_unique_nodes(self):
        ''' Tests the ability to insert unique nodes w/ unique freq '''
        self.queue.put((9, (Node(1), Node(2))))
        self.queue.put((3, (Node(88), Node(80))))
        self.queue.put((7, (Node(3), Node(4))))

        expected = [1, 2, 3, 4, 88, 80]
        actual = list()

        while not self.queue.empty():
            node = self.queue.get()
            actual.append(node[1][0].value)
            actual.append(node[1][1].value)

        self.assertEqual(actual, expected,
                         "Manual insertion doesn't get the priority right")

    # todo: handle this soon
    def test_put_duplicate_freq(self):
        ''' Tests ability to handle duplicate frequency '''

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(88)
        node4 = Node(80)
        node5 = Node(3)
        node6 = Node(4)

        graph = Graph([node1, node2, node3, node4, node5, node6])

        self.queue.put((9, (node1, node2)))
        self.queue.put((9, (node3, node4)))
        self.queue.put((7, (node5, node6)))

        expected = [88, 80, 1, 2, 3, 4]
        expected_alternative = [1, 2, 88, 80, 3, 4]

        actual = list()

        while not self.queue.empty():
            node = self.queue.get()
            actual.append(node[1][0].value)
            actual.append(node[1][1].value)

        self.assertTrue(
            ((actual == expected) or (actual == expected_alternative)),
            "duplicates aren't handled well")


class TestRepairCompress(TestCase):
    ''' Test class for the repair class '''

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

    def test_repair_empty_graph(self):
        ''' update dic with an empty graph '''
        graph = Graph([])
        repair = Repair(graph)

        compressed = repair.compress()
        self.assertEqual(graph, compressed,
                         "Empty graph is not empty when compressed")

    def test_repair_once(self):
        ''' repair where pairs show up only once in the graph '''

        # change the graph to avoid multiple pairing
        self.node1.edges = [self.node2, self.node3, self.node4, self.node5]
        self.node2.edges = [self.node1, self.node5]
        self.node3.edges = [self.node1, self.node2]
        self.node4.edges = [self.node3, self.node5]
        self.node5.edges = []

        self.graph = Graph(self.node_list)
        expected_graph = self.graph

        self.repair = Repair(self.graph)
        compressed_graph = self.repair.compress()

        self.assertEqual(compressed_graph, expected_graph)

    def test_repair_multiple(self):
        ''' repair where pairs show up multiple times in the graph '''

        self.node1.edges = [self.node2, self.node3, self.node4, self.node5]
        self.node2.edges = [self.node1, self.node4, self.node5]
        self.node3.edges = [self.node1, self.node2, self.node4, self.node5]
        self.node4.edges = [self.node3, self.node5]
        self.node5.edges = []

        self.graph = Graph(self.node_list)
        self.repair = Repair(self.graph)
        compressed_graph = self.repair.compress()

        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        inf_node = Node(math.inf)

        n1.add_edge(n2)
        n1.add_edge(n3)
        n1.add_edge(inf_node)

        n2.add_edge(inf_node)
        n2.add_edge(n1)

        n3.add_edge(n1)
        n3.add_edge(n2)
        n3.add_edge(inf_node)

        n4.add_edge(n3)
        n4.add_edge(n5)

        inf_node.add_edge(n4)
        inf_node.add_edge(n5)

        expected_graph = Graph([n1, n2, n3, n4, n5, inf_node])

        self.assertTrue(
            compare_by_value(expected_graph, compressed_graph),
            "Single run compression lossing values or positions")

    def test_compress_multiple_runs(self):
        ''' compression that requires multiple runs through the graph'''
        pass  #TODO need a good test here
