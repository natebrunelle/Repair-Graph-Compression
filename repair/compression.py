''' Implementation of the Repair algorithm
Uses the Graph and Node classes to compress a graph (the number of edges).
'''
import sys
# queue is not thread safe
from queue import PriorityQueue

from graphs import graph
from nodeAndRepairNode import nodes

# helps import stuff outside dir
# might be platform depedent. Todo: use packages

sys.path.append('../')

# "pair": [count, [[node #, index],[ ... ]]]


class compression_dictionary:
    ''' Used to keep track of pairs which will be replaced '''

    def __init__(self):
        self.pair_queue = PriorityQueue()

    def is_empty(self):
        ''' Just a wrapper for the empty method '''
        return self.pair_queue.empty()

    def get_most_common(self):
        ''' Returns the most common pairs '''
        return self.pair_queue.get_nowait()

    def add_new_pair(self, pair, frequency):
        ''' Adds new pairs to the queue. prioritizes by frequency '''
        ''' @note queue actually does lowest first, the negative flips this '''
        self.pair_queue.put_nowait((-frequency, pair))

    def contains_pair(self, pair):
        ''' Checks if the queue already contains a given pair '''
        pass  #todo find away to impelment this. Queue is not iteratable

    def update_dictionary(self, uncompressed_graph):
        ''' Takes in a graph object, scans it, and updates the priority queue with
        new pairs and their frequency '''

        # for every node, loop through its edges and check pairs
        for node in uncompressed_graph.list_nodes:
            for index, adj_node in enumerate(node.edges):
                if index + 1 == len(node.edges):
                    break

                pair = (adj_node, node.edges[index + 1])
                # todo find a way to get current freq


def updateDictionary(adjList):
    repairDictionary = {}
    for node in adjList.keys():
        for j in range(0, len(adjList[node]) - 1):
            numSet = (adjList[node][j], adjList[node][j + 1])

            if numSet in repairDictionary.keys():
                repairDictionary[numSet][0] = repairDictionary[numSet][0] + 1
                repairDictionary[numSet][1].append((node, j))
            else:
                repairDictionary[numSet] = [1, [(node, j)]]

    return repairDictionary


def getMostCommon(repairDictionary):
    maxCount = 0
    maxKey = ()

    for key in repairDictionary.keys():
        if repairDictionary[key][0] > maxCount:
            maxKey = key
            maxCount = repairDictionary[key][0]

    return maxKey


def replacePair(nodeList, index, newNode):
    #remove the two neighbors
    del nodeList[index]
    del nodeList[index]

    nodeList.insert(index, newNode)

    return nodeList


def repair(adjList):
    #generate the repair dictionary
    repairDictionary = updateDictionary(adjList)

    #get the most common pair
    mostCommonPair = getMostCommon(repairDictionary)

    #all unique, base case
    if repairDictionary[mostCommonPair][0] == 1:
        return adjList

    #create new node
    nodeKey = str(mostCommonPair[0][0]) + '_' + str(mostCommonPair[1][0])
    newNode = (nodeKey, True)

    for occurrence in repairDictionary[mostCommonPair][1]:
        #node list where it appears
        nodeList = adjList[occurrence[0]]
        repairedNodeList = replacePair(nodeList, occurrence[1], newNode)

        #put it back
        adjList[occurrence[0]] = repairedNodeList

    #add the new node to the adjList
    adjList[newNode] = [mostCommonPair[0], mostCommonPair[1]]

    #recurssion step
    return repair(adjList)
