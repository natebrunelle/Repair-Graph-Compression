import unittest

from graphs.complete_graph import CompleteGraph
from nodes.nodes import Node

def is_complete(graph):
    for node in graph.list_nodes:
        for other_node in graph.list_nodes:
            if other_node != node:
                if other_node not in node.edges:
                    return False

    return True

class CompleteGraphTestCase(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.g = CompleteGraph([self.n1, self.n2, self.n3])

    def test_completness(self):
        ''' tests that the nodes are all interconnected '''

        self.assertTrue(is_complete(self.g))

    def test_add_edge_two_graphs(self):
        ''' tests the abilty to add an edge between two graphs '''

        n5 = Node(5)
        g2 = CompleteGraph([n5])

        self.g.add_edge(self.n1, n5)
        self.assertIn(n5, self.n1.edges)

    def test_add_edge_same_graph(self):
        '''tests that add_edge can't add edges in the same complete graph'''

        self.assertRaises(ValueError, self.g.add_edge, self.n1, self.n2)

    def test_delete_edge_two_graphs(self):
        ''' tests the abilty to delete an edge between two graphs '''

        n5 = Node(5)
        g2 = CompleteGraph([n5])
        self.g.add_edge(self.n1, n5)

        self.g.delete_edge(self.n1, n5)
        self.assertNotIn(n5, self.n1.edges)

    def test_delete_edge_same_graph(self):
        ''' tests that it's not possible to delete an edge in the same graph'''

        self.assertRaises(ValueError, self.g.delete_edge, self.n1, self.n2)

    def test_add_new_node(self):
        '''tests that we can add a new node and still have a good structure '''

        n5 = Node(5)
        self.g.add_node(n5)

        self.assertTrue(is_complete(self.g))

    def test_add_new_node_existing(self):
        ''' tests that existing nodes can't be added again '''

        self.assertRaises(ValueError, self.g.add_node, self.n1)

if __name__ == '__main__':
    unittest.main()
