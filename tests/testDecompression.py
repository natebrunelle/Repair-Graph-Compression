import unittest
from unittest import TestCase
from repair.decompression import *

class TestStackScan(TestCase):
    directedGraph={}

    node56=('5_6', True)
    node567=('5_6_7', True)
    node5678=('5_6_7_8', True)

    node1=(1, False)
    node2=(2, False)
    node3=(3, False)
    node4=(4, False)
    node5=(5, False)
    node6=(6, False)
    node7=(7, False)
    node8=(8, False)

    def setUp(self):
        self.directedGraph[self.node1]=[self.node5678]        
        self.directedGraph[self.node2]=[self.node5678]
        self.directedGraph[self.node3]=[self.node5678]
        self.directedGraph[self.node4]=[self.node567]
        self.directedGraph[self.node5]=[]
        self.directedGraph[self.node6]=[]
        self.directedGraph[self.node7]=[]
        self.directedGraph[self.node8]=[]

        self.directedGraph[self.node56]=[self.node5, self.node6]
        self.directedGraph[self.node567]=[self.node56, self.node7]
        self.directedGraph[self.node5678]=[self.node567, self.node8]
        
    def testDecompress(self):
        decompressedGraph=decompress(self.directedGraph)
        for node in decompressedGraph.keys():
            print(str(node)+"\t"+str(decompressedGraph[node]))

if __name__=='__main__':
    unittest.main()

