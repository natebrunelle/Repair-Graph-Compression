import unittest

from graphs.hub_and_spoke_graph import HubAndSpoke
from nodeAndRepairNode.nodes import Node


class CompleteGraphTestCase(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.h = HubAndSpoke(self.n1, [self.n2, self.n3, self.n4])


if __name__ == '__main__':
    unittest.main()
