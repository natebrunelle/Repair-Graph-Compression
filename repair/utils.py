'''
Some common functions we will most likely be sharing
'''

from pygraphml import Graph

def cleanNode(node):
    clean=str(node[0])+str(node[1])

def generateViz(adjList):
    g=Graph()
    
    for node in adjList.keys():
        g.add_node(cleanNode(node))
        
    for n1 in adjList.keys():
        for n2 in adjList[n1]:
            print(n1,n2)
            try:
                g.add_edge(cleanNode(n1),cleanNode(n2))
            except:
                pass

    print("here")
    g.show()


