''' Implementation of the Repair algorithm
Uses the Graph and Node classes to compress a graph (the number of edges).
'''
# queue is not thread safe
from queue import PriorityQueue

from graphs import graph
from nodeAndRepairNode import nodes

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

    def add_new_pair(self, pair, frequency=1):
        ''' Adds new pairs to the queue. prioritizes by frequency '''
        self.pair_queue.put_nowait((frequency, pair))

    def contains_pair(self, pair):
        ''' Checks if the queue already contains a given pair '''
        pass  #todo find away to impelment this. Queue is not iteratable


def update_dictionary(uncompressed_graph, dictionary):
    ''' Takes in a graph object, scans it, and updates the priority queue with
    new pairs and their frequency '''

    # for every node, loop through its edges and check pairs
    for node in uncompressed_graph.list_nodes:
        for index, adj_node in enumerate(node.edges):
            if index + 1 == len(node.edges):
                break

            # make a pair and pass it on
            pair = (adj_node, node.edges[index + 1])

            # see our queue implementation on how duplicates are handled
            dictionary.add_new_pair(pair)


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
