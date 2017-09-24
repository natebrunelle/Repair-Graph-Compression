import unittest
from unittest import TestCase
from repair.node import Node
from repair.compression import *

class TestScanFunction(TestCase):
    directedGraph={}
    
    def setUp(self):
        #create graph
        node2=(2, False)
        node3=(3, False)
        node1=(1, False)
        node4=(4, False)
        node5=(5, False)
        node6=(6, False)
        node8=(8, False)
        
        self.directedGraph[2]=[node5,
                                node6,
                                node8]
        self.directedGraph[5]=[]
        self.directedGraph[6]=[]
        self.directedGraph[4]=[node3]
        self.directedGraph[8]=[]
        self.directedGraph[1]=[node5,
                                node6,
                                node8]
        self.directedGraph[3]=[node2]
                                     

    #testing test 
    def testScan(self):
        directedGraph=self.directedGraph
        

    def testUpdateDic(self):
        compDic=updateDictionary(self.directedGraph)
        for key in compDic.keys():
            print(str(key)+"\t"+str(compDic[key]))



if __name__=='__main__':
    unittest.main()
