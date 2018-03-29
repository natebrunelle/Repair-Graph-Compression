import unittest

from graphs.complete_graph import CompleteGraph
from nodeAndRepairNode.nodes import Node


class CompleteGraphTestCase(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        # self.g.list_nodes = [Node(1), Node(2), Node(3)]
        self.g = CompleteGraph([self.n1, self.n2, self.n3])


if __name__ == '__main__':
    unittest.main()
