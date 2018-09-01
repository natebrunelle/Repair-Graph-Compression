import unittest
from unittest import TestCase

from graphs.clusters import Cluster
from graphs.graph import Graph
from graphs.graph_factory import GraphFactoryAlphaNumeric, GraphTypes
from graphs.graph_generator import weakly_connected_cluster
from repair.repair import *
from tests.test_compression import compare_by_value
from utils.utils import write_graphml_file


'''
:param connection_num: the number of connections we expect to see on ave
    :param graph_num: the number of graph in the cluster
    :param edge_num: the number of edges expected within each graph
    :param graph_factory: an instance of a graph factory to

'''


class ClusterRepairCompression(TestCase):
    def setUp(self):
        self.complete_gf = GraphFactoryAlphaNumeric(GraphTypes.complete, 10)
        self.generic_gf = GraphFactoryAlphaNumeric(GraphTypes.generic, 10)
        self.hubspoke_gf = GraphFactoryAlphaNumeric(GraphTypes.hub_and_spoke,
                                                    10)

    def test_compress_cluster_complete(self):
        cluster = weakly_connected_cluster(25, 20, 15, self.complete_gf)
        print("Create cluster.")
        write_graphml_file(cluster.generate_graphml_format(), "before.graphml")
        print("Writing cluster to file.")

        edge_count_before = 0
        node_count_before = 0
        for node in cluster.list_nodes:
            node_count_before += 1
            for edge in node.edges:
                edge_count_before += 1

        repair = Repair(cluster)
        print("Compressing cluster.")
        compressed_cluster = repair.compress()

        print("Writing cluster to file")
        write_graphml_file(cluster.generate_graphml_format(), "after.graphml")

        edge_count_after = 0
        node_count_after = 0
        for node in compressed_cluster.list_nodes:
            node_count_after += 1
            for edge in node.edges:
                edge_count_after += 1

        compression_ratio = edge_count_after / edge_count_before
        print("Edges before: " + str(edge_count_before) + "\nEdges after: " +
              str(edge_count_after) + "\n Nodes before: " +
              str(node_count_before) + "\nNodes after: " +
              str(node_count_after) + "\nCompression Ratio: " +
              str(compression_ratio))

        self.assertTrue(compare_by_value(compressed_cluster, cluster))

    def test_compress_cluster_Generic(self):
        cluster = weakly_connected_cluster(25, 20, 15, self.generic_gf)
        repair = Repair(cluster)
        compressed_cluster = repair.compress()
        self.assertTrue(compare_by_value(compressed_cluster, cluster))

    def test_compress_cluster_HubSpoke(self):
        cluster = weakly_connected_cluster(9, 10, 10, self.hubspoke_gf)
        edge_count_before = 0
        node_count_before = 0
        for node in cluster.list_nodes:
            node_count_before += 1
            for edge in node.edges:
                edge_count_before += 1

        print("Compressing...")
        repair = Repair(cluster)
        compressed_cluster = repair.compress()
        edge_count_after = 0
        node_count_after = 0
        for node in compressed_cluster.list_nodes:
            node_count_after += 1
            for edge in node.edges:
                edge_count_after += 1
        compression_ratio = edge_count_after / edge_count_before
        print("Edges before: " + str(edge_count_before) + "\nEdges after: " +
              str(edge_count_after) + "\n Nodes before: " +
              str(node_count_before) + "\nNodes after: " +
              str(node_count_after) + "\nCompression Ratio: " +
              str(compression_ratio))

        self.assertTrue(compare_by_value(compressed_cluster, cluster))
