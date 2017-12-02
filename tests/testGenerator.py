import unittest
from unittest import TestCase
from repair.graphGenerator import *

class TestWCC(TestCase):

    def setUp(self):
        pass

    def testSimpleWCC(self):
        graph=weaklyConnectedClusters(50, 7, 10)

        print("Node\t\tOutgoing\n")
        for node in graph.keys():
            print(str(node)+"\t\t"+str(graph[node]))
            
