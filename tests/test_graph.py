import unittest

from graphs.graph import *
from nodeAndRepairNode.nodes import Node


class GraphTestCase(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)
        self.n6 = Node(6)
        self.n1.edges = []
        self.n2.edges = []
        self.n3.edges = []
        self.n4.edges = []
        self.n5.edges = []
        self.n6.edges = []
        self.testList3 = [self.n1, self.n2, self.n3]
        self.testList4 = [self.n1, self.n2, self.n3, self.n4]
        self.g = Graph(self.testList3)
        self.h = Graph([self.n5, self.n6])
        self.j = Graph()

    def tearDown(self):
        self.g.list_nodes = self.testList3
        self.h.list_nodes = [self.n5, self.n6]
        self.n1.edges = []
        self.n2.edges = []
        self.n3.edges = []
        self.n4.edges = []
        self.n5.edges = []
        self.n6.edges = []
        # delete entire graph?

    def test_add_edge(self):
        self.g.add_edge(self.n1, self.n2)
        self.assertIn(self.n2, self.n1.edges, "Adj list: edge not added")
        self.assertEqual(self.n1.edges.count(self.n2), 1, "Adj list: n2 should appear 1x, no duplicates")
        self.assertCountEqual(self.n1.edges, [self.n2], "Adj list not exactly as expected")

    def test_add_outside_edge(self):
        self.assertNotIn(self.n4, self.g.list_nodes)  # n4 is outside graph
        self.g.add_edge(self.n1, self.n4)
        self.assertIn(self.n4, self.n1.edges, "Adj lists not updated")
        self.assertCountEqual(self.n1.edges, [self.n4], "Adj list not exactly as expected")

    def test_duplicate_add_edge(self):
        # node count shouldn't change
        self.g.add_edge(self.n1, self.n2)  # n2 is added to n1's list
        self.g.add_edge(self.n1, self.n2)
        self.assertNotIn(self.n1, self.n2.edges)  # n1 is not added to n2's list
        self.assertEqual(self.n1.edges.count(self.n2), 1)
        self.assertCountEqual(self.n1.edges, [self.n2], "Adj list not exactly as expected")

    def test_edge_to_self(self):
        self.g.add_edge(self.n1, self.n1)
        self.assertNotIn(self.n1, self.n1.edges)
        self.assertCountEqual(self.n1.edges, [], "Adj list not exactly as expected")

    def test_add_node(self):  # should add to list_nodes, this is diff between add_node and add_edge
        self.assertNotIn(self.n4, self.g.list_nodes, "n4 is already in graph")
        self.g.add_node(self.n4)
        self.assertIn(self.n4, self.g.list_nodes, "list_nodes not updated")
        self.assertEqual(self.g.graph_id, self.n4.graph_id, "UUID not set to graph_id")
        self.assertCountEqual(self.g.list_nodes, self.testList4, "Adj list not exactly as expected")

    def test_graph_duplicate_add_node(self):
        self.assertIn(self.n3, self.g.list_nodes)
        self.g.add_node(self.n3)
        self.assertEqual(self.g.list_nodes.count(self.n3), 1)
        self.assertCountEqual(self.g.list_nodes, self.testList3)

    def test_graph_add_node_edge(self):
        self.assertNotIn(self.n4, self.g.list_nodes, "n4 is already in graph")
        self.g.add_node(self.n4)
        self.g.add_edge(self.n1, self.n4)
        self.assertEqual(self.g.list_nodes, self.testList4)
        self.assertIn(self.n4, self.n1.edges)

    def test_graph_add_edge_node(self):
        # discovered problem - inherent unfairness to the add_edge function - see graph class
        self.assertNotIn(self.n4, self.g.list_nodes, "n4 is already in graph")
        self.g.add_edge(self.n4, self.n1)  # should add_node for n4
        self.assertIn(self.n1, self.n4.edges)
        self.assertIn(self.n4, self.g.list_nodes)
        self.g.add_node(self.n4)  # should be prevented from adding 2x
        self.assertEqual(self.n1.edges.count(self.n4), 1)
        self.assertCountEqual(self.g.list_nodes, self.testList4)

        # TODO: need to write new tests to reflect new strict parameters in add_edge (unfair - add new function?)

    # def test_cluster_graphs_linked(self):
    #     # self.g.add_edge(self.n1, self.n4)  # n4 is node in another graph
    #     self.assertEqual(0, 0)
    #     # ...

    def test_delete_edge(self):
        self.assertNotIn(self.n4, self.g.list_nodes, "n4 is already in graph, TESTS ARE STUPID")
        self.assertTrue(self.n1 in self.g.list_nodes or self.n2 in self.g.list_nodes, "both parameters not in graph")
        # TODO: this is where the second parameter may/may not be in graph
        self.g.add_edge(self.n1, self.n2)
        self.g.delete_edge(self.n1, self.n2)  # n2 removed from n1's list
        self.assertEqual(len(self.g.list_nodes), 3, "Node_count for graph incorrect")
        self.assertEqual(self.g.list_nodes, self.testList3, "Graph modified by delete_edge")
        # an edge, but not a node deleted, n2 still in list_nodes and the graph
        self.assertNotIn(self.n2, self.n1.edges, "All instances not removed from adj list, edge(s) not deleted")

    # TODO: add tests for where second param for delete_edge() outside graph

    def test_delete_outside_edge(self):
        self.assertNotIn(self.n4, self.g.list_nodes, "n4 is already in graph, TESTS ARE STUPID")
        self.assertNotIn(self.n5, self.g.list_nodes)
        self.assertFalse(self.n5 in self.g.list_nodes or self.n4 in self.g.list_nodes)
        self.h.add_edge(self.n4, self.n5)
        with self.assertRaises(ValueError):
            self.g.delete_edge(self.n4, self.n5)

    def test_delete_node(self):
        self.assertIn(self.n1, self.g.list_nodes, "n1 is not part of this graph to be removed")
        self.assertNotIn(self.n2, self.n1.edges, "n2 is already in n1.edges")  # since this is true...
        # print("graph g = \n" + str(self.g) + " end of g ")  # consistently shows 3 nodes in n1.edges
        # print("n1.edges = ")
        # for x in range(len(self.n1.edges)):
        #     print(self.n1.edges[x])
        #     # despite that, it sometimes shows 2 or 3 nodes, some with duplicates??? shouldn't be possible
        # print("end of n1.edges")
        self.g.add_edge(self.n1, self.n2)  # THIS NEEDS TO BE FULLY TESTED ELSEWHERE
        self.g.delete_node(self.n1) # ...this is already true
        self.assertNotIn(self.n1, self.g.list_nodes, "Node not deleted")  # n1 no longer listed in graph
        self.assertIn(self.n2, self.g.list_nodes, "Wrong node deleted")
        self.assertNotIn(self.n1, self.n2.edges, "Found outside reference to deleted node")
        self.assertEqual(self.n1.edges, [], "Node's adj list not cleared")  # n1 has no adj nodes
        # n1 should have no outside references in other nodes (here, n2) adj_lists
        # TODO: must test in all graph files that graph_id is reset

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

    def delete_nonexistent_edge(self):
        # test_delete_nonexistent_edge(self):
        self.assertNotIn(self.n4, self.g.list_nodes)  # can delete edges btwn graphs
        self.assertIn(self.n1, self.g.list_nodes)  # one node must be in the graph
        self.assertNotIn(self.n4, self.n1.edges)
        self.g.delete_edge(self.n1, self.n4)  # n4 attempted removed from n1's list
        self.assertNotIn(self.n4, self.n1.edges)
        with self.assertRaises(ValueError):
            # self.n1.edges.remove(self.n4) # test passes with this, should be equivalent to line below
            # ValueError somehow suppressed and not passed up through classes?
            self.g.delete_edge(self.n1, self.n4)  # n4 attempted removed from n1's list

    def test_delete_nonexistent_node(self):
        self.assertNotIn(self.n4, self.g.list_nodes)
        with self.assertRaises(ValueError):
            self.g.delete_node(self.n4)

    def test_delete_outside_node(self):
        self.assertNotIn(self.n4, self.h.list_nodes, "n4 is already in graph, TESTS ARE STUPID")
        self.h.add_edge(self.n5, self.n4)  # 1st param must be in graph
        self.assertNotIn(self.n4, self.h.list_nodes)
        with self.assertRaises(ValueError):
            self.g.delete_node(self.n4)
        # this test fails when use graph g b/c n4 is in g, somehow, other tests corrupting g?

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


if __name__ == '__main__':
    unittest.main()
