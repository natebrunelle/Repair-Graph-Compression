from unittest import TestCase

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

        expected = [1, 2, 88, 80, 3, 4]
        actual = list()

        while not self.queue.empty():
            node = self.queue.get()
            actual.append(node[1][0].value)
            actual.append(node[1][1].value)

        self.assertEqual(actual, expected, "duplicates aren't handled well")


class TestRepair(TestCase):
    ''' Test class for the repair class '''

    def setUp(self):
        pass

    def test_update_dictionary_empty_graph(self):
        ''' update dic with an empty graph '''
        self.fail("No test")

    def test_update_dictionary_once(self):
        ''' update dictionary where the pair shows up only once in the graph '''
        self.fail("No test")

    def test_update_dictionary_multiple(self):
        ''' update where a pair shows up multiple times in the graph '''
        self.fail("No test")

    def test_compress_single_run(self):
        ''' Compression that only requires a single run through the graph '''
        self.fail("No test")

    def test_compress_mutliple_runs(self):
        ''' compression that requires multiple runs through the graph'''
        self.fail("No test")
