'''
Some common functions we will most likely be sharing
'''

import networkx as nx
import matplotlib.pyplot as plt

#creates a vizualization of the graph using the adj list
#the list should be in the form of a dictionary
#nodeNumber: (neighbor 1, bool), (neighbor 2, bool)....
def getViz():
    graph=nx.read_adjlist('repair/graph.txt')
    nx.draw(graph)
    plt.show()

def getViz2():
    graph=nx.read_adjlist('repair/graphBeforeCompression.txt')
    nx.draw(graph)
    plt.show()

getViz()
getViz2()
