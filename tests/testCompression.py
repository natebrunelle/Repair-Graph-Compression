import unittest
from unittest import TestCase
from repair.compression import *

class TestScanFunction(TestCase):
    directedGraph={}
    
    def setUp(self):
        self.directedGraph={}
        #create graph
        node1=(1, False)
        node2=(2, False)
        node3=(3, False)
        node4=(4, False)
        node5=(5, False)
        node6=(6, False)
        node7=(7, False)
        node8=(8, False)


        self.directedGraph[node1]=[node5,node6,node7,node8]        
        self.directedGraph[node2]=[node5,node6,node7,node8]
        self.directedGraph[node3]=[node5,node6,node7,node8]
        self.directedGraph[node4]=[node5,node6,node7]
        self.directedGraph[node5]=[]
        self.directedGraph[node6]=[]
        self.directedGraph[node7]=[]
        self.directedGraph[node8]=[]
                                     

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
        node1=(1, False)
        node2=(2, False)
        node3=(3, False)
        node4=(4, False)
        node5=(5, False)
        node6=(6, False)
        node7=(7, False)
        node8=(8, False)

        self.directedGraph[node1]=[node5,node6]        
        self.directedGraph[node2]=[node6,node7,node8]
        self.directedGraph[node3]=[node5,node7,node8]
        self.directedGraph[node4]=[node8]

        expected=1

        pairs=updateDictionary(self.directedGraph)
        actual=pairs[((5,False),(6,False))][0]
        
        self.assertEqual(expected, actual)

    def testUpdateOrderAffectsCount(self):
        node1=(1, False)
        node2=(2, False)
        node3=(3, False)
        node4=(4, False)
        node5=(5, False)
        node6=(6, False)
        node7=(7, False)
        node8=(8, False)

        self.directedGraph[node1]=[node6,node5,node8,node7]        
        self.directedGraph[node2]=[node7,node6,node8,node5]
        self.directedGraph[node3]=[node8,node6,node7,node5]
        self.directedGraph[node4]=[node5,node6,node7,node8]

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
        graphFile=open('repair/graphBeforeCompression.txt', 'w')
        adjList=self.directedGraph
        for key in adjList.keys():
            graphFile.write('\''+str(key)+'\''+" ")
            for adjItem in adjList[key]:
                graphFile.write('\''+str(adjItem[0])+'\''+" ")
                graphFile.write('\n')
        graphFile.close()

        repaired=repair(self.directedGraph)

        print()
        for key in repaired.keys():
            print(str(key)+"\t"+str(repaired[key]))

        
    
if __name__=='__main__':
    unittest.main()

