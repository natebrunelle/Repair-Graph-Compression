from unittest import TestCase

from graphs.graph import Graph
from nodeAndRepairNode.nodes import Node, RepairNode
from repair.compression import Repair, RepairPriorityQueue


class TestRepairPriorityQueue(TestCase):
    ''' Tests the priority queue implementation '''

    def setUp(self):
        self.queue = RepairPriorityQueue()

    def test_passed_list_queued(self):
        ''' Tests that a list of points passed in are correctly queued '''
        pair_list = list()
        pair_list.append((9, (Node(1), Node(2))))
        pair_list.append((20, (Node(3), Node(4))))
        pair_list.append((87, (Node(5), Node(6))))
        pair_list.append((4, (Node(7), Node(8))))

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

        self.queue.put((9, (Node(1), Node(2))))
        self.queue.put((9, (Node(88), Node(80))))
        self.queue.put((7, (Node(3), Node(4))))

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


class TestRepair(TestCase):
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
        ''' repair where the pair shows up only once in the graph '''

        # change the graph to avoid multiple pairing
        self.node1.edges = [self.node2, self.node3, self.node4, self.node5]
        self.node2.edges = [self.node1, self.node5]
        self.node3.edges = [self.node1, self.node2]
        self.node4.edges = [self.node3, self.node5]
        self.node5.edges = []

        self.graph = Graph(self.node_list)
        self.repair = Repair(self.graph)
        compressed_graph = self.repair.compress()

        #TODO update this when the equal method is provided

        self.assertEqual(compressed_graph, self.graph)

    def test_repair_multiple(self):
        ''' repair where a pair shows up multiple times in the graph '''

        self.node1.edges = [self.node2, self.node3, self.node4, self.node5]
        self.node2.edges = [self.node1, self.node4, self.node5]
        self.node3.edges = [self.node1, self.node2, self.node4, self.node5]
        self.node4.edges = [self.node3, self.node5]
        self.node5.edges = []

        self.graph = Graph(self.node_list)
        self.repair = Repair(self.graph)
        compressed_graph = self.repair.compress()

        #TODO update this when the equal method is provided

        self.assertEqual(compressed_graph, self.graph)

    def test_compress_mutliple_runs(self):
        ''' compression that requires multiple runs through the graph'''

        compressed_graph = self.repair.compress()

        print("-------------compressed---------------")

        print(str(compressed_graph))

        self.assertEqual(compressed_graph, self.graph)
