import unittest
from unittest import TestCase
from repair.compression import *

class TestScanFunction(TestCase):
    directedGraph={}

    node1=(1, False)
    node2=(2, False)
    node3=(3, False)
    node4=(4, False)
    node5=(5, False)
    node6=(6, False)
    node7=(7, False)
    node8=(8, False)

    def setUp(self):
        self.directedGraph={}

        #create graph
        
        self.directedGraph[self.node1]=[self.node5,self.node6,self.node7,self.node8]        
        self.directedGraph[self.node2]=[self.node5,self.node6,self.node7,self.node8]
        self.directedGraph[self.node3]=[self.node5,self.node6,self.node7,self.node8]
        self.directedGraph[self.node4]=[self.node5,self.node6,self.node7]
        self.directedGraph[self.node5]=[]
        self.directedGraph[self.node6]=[]
        self.directedGraph[self.node7]=[]
        self.directedGraph[self.node8]=[]
                                     

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

        self.directedGraph[self.node1]=[self.node5,self.node6]        
        self.directedGraph[self.node2]=[self.node6,self.node7,self.node8]
        self.directedGraph[self.node3]=[self.node5,self.node7,self.node8]
        self.directedGraph[self.node4]=[self.node8]

        expected=1

        pairs=updateDictionary(self.directedGraph)
        actual=pairs[((5,False),(6,False))][0]
        
        self.assertEqual(expected, actual)

    def testUpdateOrderAffectsCount(self):

        self.directedGraph[self.node1]=[self.node6,self.node5,self.node8,self.node7]        
        self.directedGraph[self.node2]=[self.node7,self.node6,self.node8,self.node5]
        self.directedGraph[self.node3]=[self.node8,self.node6,self.node7,self.node5]
        self.directedGraph[self.node4]=[self.node5,self.node6,self.node7,self.node8]

        expected=1

        pairs=updateDictionary(self.directedGraph)
        actual=pairs[((5,False),(6,False))][0]

        self.assertEqual(expected, actual)

        actual2=pairs[((6,False),(5,False))][0]
        self.assertEqual(expected, actual)


    def testGetMostCommon(self):
        repairDictionary=updateDictionary(self.directedGraph)
        equal=((7,False), (8,False))
        
        del repairDictionary[equal]
        
        mostCommonPair=getMostCommon(repairDictionary)
        expected=((5,False),(6,False))

        self.assertEqual(expected,mostCommonPair)
        
    
    def testGetMostCommonWithEquals(self):
        repairDictionary=updateDictionary(self.directedGraph)
        
        mostCommonPair=getMostCommon(repairDictionary)

        expected=((5,False), (6,False))

        self.assertEqual(expected,mostCommonPair)
        
    def testReplacePairHappy(self):
        nodeList=[(1,False), (2,False),(3,False)]
        index=0
        newNode=('1_2',True)

        expected=[newNode, (3,False)]
        actual=replacePair(nodeList, index,newNode)

        self.assertEqual(expected, actual)

    #todo test bound checking for replacePair


    #todo write actual tests for repair
    def testRepairWithTwo(self):
        adjList=self.directedGraph

        repaired=repair(self.directedGraph)

    
if __name__=='__main__':
    unittest.main()

