import unittest

from graphs.hub_and_spoke_graph import HubAndSpoke
from nodes.nodes import Node


class CompleteGraphTestCase(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.h = HubAndSpoke(self.n1, [self.n2, self.n3, self.n4])

    def test_delete_node_not_hub(self):
        ''' tests that we can delete non-hub nodes'''
        self.h.delete_node(self.n3)

        for node in self.h.list_nodes:
            self.assertNotIn(self.n3, node.edges)

    def test_delete_node_hub(self):
        ''' tests that we can't delete the hub'''

        self.assertRaises(ValueError, self.h.delete_node, self.n1)

if __name__ == '__main__':
    unittest.main()
