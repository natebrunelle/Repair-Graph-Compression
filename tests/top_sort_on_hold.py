import unittest
from unittest import TestCase
from repair.topologicalSort import *

class TestTopologicalSort(TestCase):
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
        self.directedGraph[self.node8]=[self.node5]

    def testSimpleSort(self):
        topSort(self.directedGraph)
