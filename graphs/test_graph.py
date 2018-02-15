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

    def test_graph_add_node_edge(self):
        self.g.add_node(self.n4)
        self.g.add_edge(self.n1, self.n4)  # 1. could potentially fail if n1 randomly selected in add_node
        # 2. actually, doesn't fail b/c there is no checking that existing edges aren't additionally appended. Fixed.
        # Randomly selecting the same node (1) is still a problem.
        self.assertEqual(self.g.node_count(), 4)


    def test_graph_add_edge_node(self):
        self.g.add_edge(self.n1, self.n4)
        self.g.add_node(self.n4)  # adds an edge between random node and n4. Could fail if rand_node is n1.
        # Note that n4 could still be re-added to the graph even though
        # it's already attached probably elsewhere. Will fail rarely.
        # Checking of rand_node.adj_list() now added in Node, doesn't fix this problem.
        self.assertEqual(self.g.node_count(), 4)

    def test_graph_add_edge(self):
        x = self.g.node_count()
        self.g.add_edge(self.n1, self.n2)
        self.assertEqual(self.g.node_count(), x, "Graph's node_count changed")
        self.assertEqual(self.n1.edges, [n2])
        self.assertEqual(self.n2.edges, [n1])

    def test_graph_new_node(self):
        self.g.add_edge(self.n1, self.n4)  # if new node added by edge, should be added to list_nodes? (Currently isn't)
        self.assertEqual(self.g.node_count(), 4) # No, because that's how clusters work - not our def of graph

    # def test_cluster_graphs_linked(self):
    #     self.g.add_edge(self.n1, self.n4)  # n4 is node in another graph

    def test_graph_delete_edge(self):
        self.g.add_edge(self.n1, self.n2)
        self.g.delete_edge(self.n1,self.n2)  # List.remove() throws error if remove non existing
        self.assertEqual(self.g.node_count(), 3, "Node_count for graph incorrect")
        # an edge, but not a node deleted, n4 still in list_nodes
        # what if that edge deleted was the only 1 attaching it to the graph?

    def test_graph_delete_node(self):
        self.g.delete_node(self.n1)
        # check that n1 no longer listed in other nodes adj_lists() self.g.list_nodes
        # aka check that Node.delete_edge() worked  AssertNotIn(a, b) a not in b
        self.assertEqual(self.g.node_count(), 2)
        self.assertEqual(self.g.list_nodes, [self.n2, self.n3], "Node not deleted")

    def test_delete_node_delete_edge(self):
        self.g.add_edge(self.n2, self.n1)  # g initialized w/n1 and n2, but no connecting edges
        self.g.delete_edge(self.n1, self.n2)
        # some assert here...

    # also test deleting non existent edges and nodes, deleting in various order
