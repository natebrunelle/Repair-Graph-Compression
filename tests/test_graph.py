import unittest
from graphs.graph import Graph
from nodeAndRepairNode.nodes import Node


class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        # self.g.list_nodes = [Node(1), Node(2), Node(3)]
        self.g = Graph([self.n1, self.n2, self.n3], 3)

    # def test_graph_add_node_edge(self):
    #     self.g.add_node(self.n4)
    #     self.g.add_edge(self.n1, self.n4)  # 1. could potentially fail if n1 randomly selected in add_node
    #     # 2. actually, doesn't fail b/c there is no checking that existing edges aren't additionally appended. Fixed.
    #     # Randomly selecting the same node (1) is still a problem.
    #     self.assertEqual(self.g.node_count(), 4)
    #
    # def test_graph_add_edge_node(self):
    #     self.g.add_edge(self.n1, self.n4)
    #     self.g.add_node(self.n4)  # adds an edge between random node and n4. Could fail if rand_node is n1.
    #     # Note that n4 could still be re-added to the graph even though
    #     # it's already attached probably elsewhere. Will fail rarely.
    #     # Checking of rand_node.adj_list() now added in Node, doesn't fix this problem.
    #     self.assertEqual(self.g.node_count(), 4)

    def test_graph_add_edge(self):
        x = self.g.node_count  # node count shouldn't change
        self.g.add_edge(self.n1, self.n2)
        self.assertEqual(self.g.node_count, x, "Graph's node_count changed")
        # both nodes should list the other node
        self.assertIn(self.n1, self.n2.edges, "Adj lists not updated")
        self.assertIn(self.n2, self.n1.edges, "Adj lists not updated")

    def test_graph_duplicate_add_edge(self):
        x = self.g.node_count  # node count shouldn't change
        self.g.add_edge(self.n1, self.n2)
        self.g.add_edge(self.n1, self.n2)  # testing self.n2, self.n1 shouldn't change anything, see Graph
        self.assertEqual(self.g.node_count, x, "Graph's node_count changed")
        # both nodes should list the other node only 1x
        self.assertEqual(self.n2.edges.count(self.n1), 1)
        self.assertEqual(self.n1.edges.count(self.n2), 1)

    def test_graph_add_node(self):  # should add to list_nodes, this is diff between add_node and add_edge
        self.g.add_node(self.n4)
        self.assertEqual(self.g.node_count, 4, "node_count not updated")
        self.assertIn(self.n4, self.g.list_nodes, "list_nodes not updated")
        self.assertRaises(ValueError, "Should raise error b/c node already in graph")
        # TODO: need to test the uid or UUID here?

    def test_graph_duplicate_add_node(self):
        self.assertEqual(0, 0)
        # ...

    def test_graph_new_node_add_edge(self):
        self.g.add_edge(self.n1, self.n4)  # if new node added by edge, should be added to list_nodes? (Currently isn't)
        self.assertEqual(self.g.node_count, 4)  # No, because that's how clusters work - not our def of graph
        # also shouldn't be added to list_nodes b/c that's the job of add_node

    def test_cluster_graphs_linked(self):
        # self.g.add_edge(self.n1, self.n4)  # n4 is node in another graph
        self.assertEqual(0, 0)
        # ...

    def test_graph_delete_edge(self):
        self.g.add_edge(self.n1, self.n2)
        self.g.delete_edge(self.n1, self.n2)  # List.remove() throws error if remove non existing
        self.assertEqual(self.g.node_count, 3, "Node_count for graph incorrect")
        # an edge, but not a node deleted, n4 still in list_nodes
        # what if that edge deleted was the only 1 attaching it to the graph? Still in cluster?
        self.assertNotIn(self.n1, self.n2.edges, "All instances not removed from adj list")
        self.assertNotIn(self.n2, self.n1.edges, "All instances not removed from adj list")

    def test_graph_delete_node(self):
        self.g.delete_node(self.n1)
        # TODO: check that n1 no longer listed in other nodes adj_lists() self.g.list_nodes
        # TODO: aka check that Node.delete_edge() worked  AssertNotIn(a, b) a not in b, don't use len only
        self.assertEqual(self.g.node_count, 2)
        self.assertEqual(self.g.list_nodes, [self.n2, self.n3], "Node not deleted")
        self.assertRaises("Value Error")

    def test_delete_node_delete_edge(self):
        self.g.add_edge(self.n2, self.n1)  # g initialized w/n1 and n2, but no connecting edges
        # each should be added to other's adj list.
        self.g.delete_edge(self.n1, self.n2)
        self.assertEqual(self.n1.edges, [])
        self.assertEqual(self.n2.edges, [])
        # some assert here...

    def test_delete_edge_delete_node(self):
        # can we still access the node? I assume so, uid.
        self.assertEqual(0, 0)
        # ...

    def test_delete_nonexistent_edge(self):
        self.assertEqual(0, 0)
        # ...

    def test_delete_nonexistent_node(self):
        self.assertEqual(0, 0)
        # ...

    # also test deleting non existent edges and nodes, deleting in various order


if __name__ == '__main__':
        unittest.main()
