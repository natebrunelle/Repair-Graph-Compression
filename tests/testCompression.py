import unittest
from unittest import TestCase
from repair.node import Node

class TestScanFunction(TestCase):
    directedGraph={}
    
    def setUp(self):
        #create graph
        node2=Node(2, False)
        node3=Node(3, False)
        node1=Node(1, False)
        node4=Node(4, False)
        node5=Node(5, False)
        node6=Node(6, False)
        node8=Node(8, False)
        
        self.directedGraph[2]=[node5,
                                node6,
                                node8]
        self.directedGraph[5]=[]
        self.directedGraph[6]=[]
        self.directedGraph[4]=[node3]
        self.directedGraph[8]=[]
        self.directedGraph[1]=[node2]
                                     

    #testing test 
    def testScan(self):
        directedGraph=self.directedGraph
        print(list(directedGraph[2]))
        print(list(directedGraph[1]))
        





if __name__=='__main__':
    unittest.main()
