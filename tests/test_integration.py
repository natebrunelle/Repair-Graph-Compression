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

    def test_compress_cluster_complete(self):
        cluster = weakly_connected_cluster(25, 20, 15, self.complete_gf)
        repair = Repair(cluster)
        compressed_cluster = repair.compress()
        self.assertTrue(compare_by_value(compressed_cluster, cluster))

    def test_compress_cluster_Generic(self):
        cluster = weakly_connected_cluster(25, 20, 15, self.generic_gf)
        repair = Repair(cluster)
        compressed_cluster = repair.compress()
        self.assertTrue(compare_by_value(compressed_cluster, cluster))
