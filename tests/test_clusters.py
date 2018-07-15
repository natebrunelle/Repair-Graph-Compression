from unittest import TestCase

from graphs.clusters import Cluster
from graphs.graph import EventType, Graph
from nodes.nodes import Node
from repair.repair import Repair


class TestClusterRepairIntegration(TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)
        self.n6 = Node(6)
        self.n7 = Node(7)
        self.n8 = Node(8)

        self.graph1 = Graph([self.n1, self.n2])
        self.graph2 = Graph([self.n3, self.n4])
        self.graph3 = Graph([self.n5, self.n6, self.n7, self.n8])

        self.graphs = [self.graph1, self.graph2, self.graph3]
        self.nodes = [
            self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7,
            self.n8
        ]
        self.cluster = Cluster(self.graphs)
        self.repair = Repair(self.cluster)

    def test_basic_compression(self):
        self.graph1.add_edge(self.n1, self.n2)
        self.graph1.add_edge(self.n1, self.n3)

        self.graph3.add_edge(self.n5, self.n2)
        self.graph3.add_edge(self.n5, self.n3)

        self.graph3.add_edge(self.n6, self.n2)
        self.graph3.add_edge(self.n6, self.n3)

        self.graph3.add_edge(self.n7, self.n2)
        self.graph3.add_edge(self.n7, self.n3)

        self.graph3.add_edge(self.n8, self.n2)
        self.graph3.add_edge(self.n8, self.n3)

        self.repair.compress()

        self.assertNotIn(self.n2, self.n1.edges)
        self.assertNotIn(self.n2, self.n5.edges)
        self.assertNotIn(self.n2, self.n6.edges)
        self.assertNotIn(self.n2, self.n7.edges)
        self.assertNotIn(self.n2, self.n8.edges)

        self.assertNotIn(self.n3, self.n1.edges)
        self.assertNotIn(self.n3, self.n5.edges)
        self.assertNotIn(self.n3, self.n6.edges)
        self.assertNotIn(self.n3, self.n7.edges)
        self.assertNotIn(self.n3, self.n8.edges)


class TestClusterBasics(TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)
        self.n6 = Node(6)
        self.n7 = Node(7)
        self.n8 = Node(8)

        self.graph1 = Graph([self.n1, self.n2])
        self.graph2 = Graph([self.n3, self.n4])
        self.graph3 = Graph([self.n5, self.n6, self.n7, self.n8])

        self.graphs = [self.graph1, self.graph2, self.graph3]
        self.nodes = [
            self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7,
            self.n8
        ]
        self.cluster = Cluster(self.graphs)

    def test_cluster_contains_all_nodes(self):

        for node in self.nodes:
            self.assertIn(node, self.cluster.list_nodes,
                          "Lost node: " + str(node))

    def test_graphs_stay_alive(self):
        self.graph1.list_nodes[0].value = -99
        self.assertTrue(
            self.n1.value == self.graph1.list_nodes[0].value ==
            self.cluster.list_nodes[self.cluster.list_nodes.index(
                self.n1)].value,
            "The value of the node should be consistent in all three.")

    def test_cluster_observes_nodes(self):
        for node in self.nodes:
            self.assertIn(self.cluster, node.observers,
                          "The cluster is not observing: " + str(node))

    def test_cluster_handles_delete_event(self):
        self.n1.notify_all(EventType.node_deleted)
        self.assertNotIn(
            self.n1, self.cluster.list_nodes,
            "The node was deleted, but cluster still holds a reference.")

    def test_cluster_handles_replace_event(self):
        replacement = Node(9)
        self.n1.notify_all(EventType.node_replaced, [self.n2, replacement])

        self.assertNotIn(self.n1, self.cluster.list_nodes,
                         "A replaced node shouldn't be in the cluster.")
        self.assertNotIn(self.n2, self.cluster.list_nodes,
                         "A replaced node shouldn't be in the cluster.")
        self.assertIn(replacement, self.cluster.list_nodes,
                      "Replacement node should be in the cluster.")

    def sort_test_helper(self):
        self.cluster.sort_nodes()
        return self.cluster.list_nodes

    def test_cluster_nodes_sorted(self):
        '''
        This test is pretty useless because it does the same thing as the code
        itself. Will update if I find a better way other than manually sorting.
        '''

        self.assertEqual(
            sorted(self.cluster.list_nodes, key=lambda x: (x.graph_id, x.uid)),
            self.sort_test_helper())
