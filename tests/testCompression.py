import unittest
from unittest import TestCase
from repair.compression import *

class TestScanFunction(TestCase):
    directedGraph={}
    
    def setUp(self):
        #create graph
        node1=(1, False)
        node2=(2, False)
        node3=(3, False)
        node4=(4, False)
        node5=(5, False)
        node6=(6, False)
        node7=(7, False)
        node8=(8, False)


        self.directedGraph[1]=[node5,node6,node7,node8]        
        self.directedGraph[2]=[node5,node6,node7,node8]
        self.directedGraph[3]=[node5,node6,node7,node8]
        self.directedGraph[4]=[node5,node6,node7,node8]
        self.directedGraph[5]=[]
        self.directedGraph[6]=[]
        self.directedGraph[7]=[]
        self.directedGraph[8]=[]
                                     

    def testUpdateDicCount(self):
        pairs=updateDictionary(self.directedGraph)

        expected=4
        actual=pairs[((5,False),(6,False))][0]
        
        self.assertEqual(expected,actual)

    def testUpdateDicCountEmpty(self):
        directedGraph={}
        expected=0

        self.assertEqual(expected,len(updateDictionary(directedGraph)))

    def testUpdateDicCountNoCommon(self):
        node5=(5, False)
        node6=(6, False)
        node7=(7, False)
        node8=(8, False)

        self.directedGraph[1]=[node5,node6]        
        self.directedGraph[2]=[node6,node7,node8]
        self.directedGraph[3]=[node5,node7,node8]
        self.directedGraph[4]=[node8]

        expected=1

        pairs=updateDictionary(self.directedGraph)
        actual=pairs[((5,False),(6,False))][0]
        
        self.assertEqual(expected, actual)

    def testUpdateOrderAffectsCount(self):
        node5=(5, False)
        node6=(6, False)
        node7=(7, False)
        node8=(8, False)

        self.directedGraph[1]=[node6,node5,node8,node7]        
        self.directedGraph[2]=[node7,node6,node8,node5]
        self.directedGraph[3]=[node8,node6,node7,node5]
        self.directedGraph[4]=[node5,node6,node7,node8]

        expected=1

        pairs=updateDictionary(self.directedGraph)
        actual=pairs[((5,False),(6,False))][0]
        
        self.assertEqual(expected, actual)

        actual2=pairs[((6,False),(5,False))][0]
        self.assertEqual(expected, actual)
        
    
    def testRepairWithTwo(self):
        repaired=repair(self.directedGraph)
        print(repaired)
        

if __name__=='__main__':
    unittest.main()
