import unittest
from unittest import TestCase
import networkx as nx


class TestScanFunction(TestCase):
    directedGraph=nx.DiGraph()
    
    def setUp(self):
        #create graph
        global directedGraph
        directedGraph.add_edges_from([([2, True],[8, True]), (2,5), (2, 6), (2,9), (3,5), (3, 8), (3, 6), (1, 2), (4, 3)])

    #testing test 
    def testScan(self):
        global directedGraph
        print(list(directedGraph.neighbors(2)))
        print(list(directedGraph.neighbors(3)))
        





if __name__=='__main__':
    unittest.main()
