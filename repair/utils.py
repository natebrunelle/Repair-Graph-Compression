'''
Some common functions we will most likely be sharing
'''

from pygraphml import Graph
from pygraphml import GraphMLParser

def cleanNode(node):
    return str(node[0])+str(node[1])

def generateViz(adjList):
    g=Graph()

    lookup={}
    for node in adjList.keys():
        clean=cleanNode(node)
        n=g.add_node(clean)
        lookup[clean]=n

    
    for n1 in adjList.keys():
        for n2 in adjList[n1]:
            g.add_edge(lookup[cleanNode(n1)],lookup[cleanNode(n2)])


    
    parser = GraphMLParser()
    parser.write(g, "myGraph.graphml")

    g.show()
