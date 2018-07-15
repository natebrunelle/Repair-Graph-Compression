import unittest
from unittest import TestCase

from graph_factory import GraphTypes
from graphs.graph import Graph
from graphs.graph_factory import (GraphFactory, GraphFactoryAlphaNumeric,
                                  GraphFactoryNoData)
from graphs.graph_generator import weakly_connected_graphs
from nodes.nodes import Node


class TestGraphGenerator(TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        # self.g.list_nodes = [Node(1), Node(2), Node(3)]
        # self.g = Graph([self.n1, self.n2, self.n3])
        self.gf = GraphFactoryAlphaNumeric(GraphTypes(3), 10)
        #weakly_connected_graphs(connection_num, graph_num, edge_num, graph_factory):
        self.g = weakly_connected_graphs(10, 20, 11, self.gf)

    def test_graphs(self):
        print("hello world")


'''
    # def test_graph_generator(self):
    #     # weakly_connected_graphs(connection_num, graph_num, edge_num, graph_factory):
    #     g = weakly_connected_graph(10, 20, 10, self.gf)
    #     self.assertEqual(self.gf )

    # connections
    def test_num_connections(self):
        self.assertEqual(len(self.g.list_nodes), 10, "Wrong number of connections between graphs")


    # number of nodes
    def test_number_of_nodes(self):
        all_true = True
        for graph in self.g:
            if len(graph.list_nodes is not 100):
                all_true = False
        self.assertEqual(all_true, True, "The number of nodes in the graphs are not correct")

    # number of graphs
    def test_number_of_graphs(self):
        self.assertEqual(len(self.g), 20, "The number of graphs is not correct ")


    # # number of graphs
    # def test_edge_num_of_graphs(self):
    #     pass
    #
    # # if connections are valid1
    # def test_correct_connections(self):
    #     pass
'''
