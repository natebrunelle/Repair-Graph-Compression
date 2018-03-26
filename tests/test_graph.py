import unittest

from graphs.graph import *
from nodeAndRepairNode.nodes import Node


class GraphTestCase(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.g = Graph([self.n1, self.n2, self.n3])
        self.testList3 = [self.n1, self.n2, self.n3]
        self.testList4 = [self.n1, self.n2, self.n3, self.n4]

    def test_graph_add_edge(self):
        # since node count shouldn't change, this is now testing what the node does,
        # rather than the graph
        self.g.add_edge(self.n1, self.n2)
        self.assertIn(self.n2, self.n1.edges, "Adj lists not updated")
        self.assertEqual(len(self.n1.edges), 1, "Adj lists not updated")
        self.assertEqual(self.n1.edges.count(self.n2), 1, "Adj lists not updated")

    def test_graph_duplicate_add_edge(self):
        # node count shouldn't change
        self.g.add_edge(self.n1, self.n2)  # n2 is added to n1's list
        self.g.add_edge(self.n1, self.n2)
        self.assertNotIn(self.n1, self.n2.edges)  # n1 is not added to n2's list
        self.assertIn(self.n1.edges.count(self.n2), 1)

    def test_graph_add_node(self):  # should add to list_nodes, this is diff between add_node and add_edge
        self.g.add_node(self.n4)
        self.assertIn(self.n4, self.g.list_nodes, "list_nodes not updated")
        self.assertEquals(self.g.graph_id, self.n4.graph_id)  # test the uid or UUID

    def test_graph_duplicate_add_node(self):
        self.assertIn(self.n3, self.g.list_nodes)
        self.g.add_node(self.n3)
        self.assertEquals(self.g.list_nodes.count(self.n3), 1)
        self.assertEquals(self.g.list_nodes, self.testList3)
        # TODO: self.assertRaises(ValueError, "Should raise error b/c node already in graph")
        # or should fail quietly?

    def test_graph_add_node_edge(self):
        self.g.add_node(self.n4)
        self.g.add_edge(self.n1, self.n4)
        self.assertEqual(self.g.list_nodes, self.testList4)
        self.assertIn(self.n4, self.n1.edges)

    def test_graph_add_edge_node(self):
        self.g.add_edge(self.n1, self.n4)  # should add_node(n4)
        self.g.add_node(self.n4)  # should be prevented from adding 2x
        self.assertEqual(self.g.list_nodes, self.testList4)
        self.assertIn(self.n4, self.n1.edges)

    def test_graph_new_node_add_edge(self):
        self.g.add_edge(self.n1, self.n4)
        # if new node added by edge, should be added to list_nodes? (No, Currently isn't)
        self.assertEqual(len(self.g.list_nodes), 3)  # 3 not 4 because that's how clusters work - not our def of graph
        self.assertEqual(self.g.list_nodes, self.testList3)
        # also shouldn't be added to list_nodes b/c that's the job of add_node

    # def test_cluster_graphs_linked(self):
    #     # self.g.add_edge(self.n1, self.n4)  # n4 is node in another graph
    #     self.assertEqual(0, 0)
    #     # ...

    def test_graph_delete_edge(self):  # this now tests node things,
        self.g.add_edge(self.n1, self.n2)
        self.g.delete_edge(self.n1, self.n2)  # n2 removed from n1's list
        self.assertEqual(len(self.g.list_nodes), 3, "Node_count for graph incorrect")
        self.assertEqual(self.g.list_nodes, self.testList3, "Graph modified by delete_edge")
        # an edge, but not a node deleted, n2 still in list_nodes and the graph
        self.assertNotIn(self.n2, self.n1.edges, "All instances not removed from adj list")

    def test_graph_delete_node(self):
        self.g.add_edge(self.n1, self.n2)
        self.g.delete_node(self.n1)
        self.assertNotIn(self.n1, self.g.list_nodes, "Node not deleted")  # n1 no longer listed in graph
        self.assertEquals(self.n1.edges, [], "Node's adj list not cleared")  # n1 has no adj nodes
        self.assertIn(self.n2, self.g.list_nodes, "Wrong node deleted")
        self.assertNotIn(self.n1, self.n2.edges, "Found outside reference to deleted node")
        # n1 should have no outside references in other nodes (here, n2) adj_lists

    # Depreciated test?
    # def test_delete_node_delete_edge(self):
    #     self.g.add_edge(self.n2, self.n1)  # g initialized w/n1 and n2, but no connecting edges
    #     # each should be added to other's adj list.
    #     self.g.delete_edge(self.n1, self.n2)
    #     self.assertEqual(self.n1.edges, [])
    #     self.assertEqual(self.n2.edges, [])
    #     # some assert here...

    def test_delete_edge_delete_node(self):
        # we can still access deleted nodes through the uid.
        # so we can still give it edges, although deleted node's adj list should be blank
        self.assertEqual(0, 0)
        # ...

    def test_delete_nonexistent_edge(self):
        self.assertNotIn(self.n4, self.n1.edges)
        self.g.delete_edge(self.n1, self.n4)  # n4 attempted removed from n1's list
        self.assertRaises("Value Error")

    def test_delete_nonexistent_node(self):
        self.assertNotIn(self.n4, self.g.list_nodes)
        self.g.delete_node(self.n4)
        self.assertRaises("Value Error")

    # TODO: also test deleting in various order

    def test_eq_wrong_num_nodes(self):
        """Tests equals method override with graphs
        that don't have equal number of nodes"""

        second_graph = Graph([self.n1, self.n2])

        self.assertTrue((second_graph != self.g),
                        "Graphs with missing nodes shouldn't be equal")

    def test_eq_wrong_ids(self):
        """Tests the equals method with graphs that have the same
        nodes, in the same places, but wrong ids"""

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        second_graph = Graph([node1, node2, node3])
        self.assertTrue((self.g != second_graph),
                        "Graphs with wrong ids shouldn't be considered equal")

    def test_eq_wrong_positions(self):
        """Tests the equals method with graphs that have the
        same nodes but in different positions """

        second_graph = Graph([self.n2, self.n3, self.n1])

        self.assertTrue(
            (self.g != second_graph),
            "Graphs with nodes in d/f positions shouldn't be considered equal")

    def test_eq_identical(self):
        """Happy path: tests the same exact graphs are considered equal"""

        self.assertEqual(self.g, self.g, "same graphs should be equal")


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
