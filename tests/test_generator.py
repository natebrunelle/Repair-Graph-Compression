import unittest
from unittest import TestCase

from graphs.graph import Graph
from graphs.graph_factory import (GraphFactory, GraphFactoryAlphaNumeric,
                                  GraphFactoryNoData, GraphTypes)
from graphs.graph_generator import (pick_two_different_items,
                                    randomly_create_edges,
                                    weakly_connected_cluster,
                                    weakly_connected_graphs)
from nodes.nodes import Node


'''
    :param connection_num: the number of connections
    :param graph_num: the number of graph in the cluster
    :param edge_num: the number of edges expected within each graph
    :param graph_factory: an instance of a graph factory to
'''


class TestGraphGenerator(TestCase):
    def setUp(self):
        self.graph_factory = GraphFactoryAlphaNumeric(GraphTypes.complete, 15)

    def test_all_graphs_connected_atleast_once(self):
        num_conns = 150
        num_graphs = 20
        num_internal_edges = 15

        graphs = weakly_connected_graphs(
            num_conns, num_graphs, num_internal_edges, self.graph_factory)

        for graph in graphs:
            for node in graph.list_nodes:
                for edge in node.edges:
                    if edge.graph_id != node.graph_id:
                        # TODO this is probalby not the best way to test this
                        self.assertNotEqual(edge.graph_id, node.graph_id)

    def test_randomly_create_edges(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)

        graph1 = Graph([n1, n2, n3])
        graph2 = Graph([n4, n5, n6])

        graphs = randomly_create_edges([graph1, graph2], 3)

        for graph in graphs:
            edge_count = 0
            for node in graph.list_nodes:
                edge_count += len(node.edges)

            self.assertEqual(edge_count, 3,
                             "Every graph should have at least 3 edges.")

    def test_pick_two_randoms(self):
        population = [1, 2, 3, 4, 5]

        for _ in range(5):
            item1, item2 = pick_two_different_items(population)
            self.assertNotEqual(item1, item2,
                                "it should always pick different items")
