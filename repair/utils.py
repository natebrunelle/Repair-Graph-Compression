'''
Some common functions we will most likely be sharing
'''

import networkx as nx
import matplotlib.pyplot as plt

#creates a vizualization of the graph using the adj list
#the list should be in the form of a dictionary
#nodeNumber: (neighbor 1, bool), (neighbor 2, bool)....
def getViz(adjList):
    graphFile=open('graph.txt', 'w')
    
    for key in adjList.keys():
        graphFile.write(str(key)+" ")
        for adjItem in adjList[key]:
            graphFile.write(str(adjItem[0])+" ")
        graphFile.write('\n')
    graphFile.close()
    graph=nx.read_adjlist('graph.txt')
    nx.draw(graph)
    plt.show()


