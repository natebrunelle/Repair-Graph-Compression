''' Implementation of the Repair algorithm
Uses the Graph and Node classes to compress a graph.
'''
import math
# queue is not thread safe
from queue import PriorityQueue

from graphs import graph
from nodeAndRepairNode import Nodes, RepairNodes


class RepairPriorityQueue(PriorityQueue):
    ''' Implements the python priority queue to fix our issue with put '''

    def __init__(self, node_list=None):
        # todo implement this class
        pass


class CompressionDictionary:
    ''' Used to keep track of pairs which will be replaced '''

    def __init__(self, queue=None):

        # inject the queue if needed
        if not queue:
            self.pair_queue = queue
        else:
            self.pair_queue = RepairPriorityQueue()

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


class Repair:
    ''' The main class that holds everything together '''

    def __init__(self, uncompressed_graph, dictionary=None):
        self.graph = uncompressed_graph

        # inject dictionary, or create new
        if not dictionary:
            self.dictionary = CompressionDictionary()
        else:
            self.dictionary = dictionary

    def update_dictionary(self):
        ''' Takes in a graph object, scans it, and updates the priority queue with
        new pairs and their frequency '''

        # for every node, loop through its edges and check pairs
        for node in self.graph.list_nodes:
            for index, adj_node in enumerate(node.edges):
                if index + 1 == len(node.edges):
                    break

                # make a pair and pass it on
                pair = (adj_node, node.edges[index + 1])

                # see our queue implementation on how duplicates are handled
                self.dictionary.add_new_pair(pair)

    def compress_graph(self):
        ''' Compresses the graph passed into the class '''

        # update dictionary
        self.dictionary = self.update_dictionary()

        # get the most common pairs in the graph
        most_common_pair = self.dictionary.get_most_common()

        # recursion base case
        if most_common_pair[0] == 1:
            return self.graph

        # unpack the pair
        node1 = most_common_pair[1][0]
        node2 = most_common_pair[1][1]

        # create a dictionary node
        dictionary_node = RepairNodes(math.inf, node1, node2)

        # loop through all nodes and replace the pair
        for node in self.graph.list_nodes:
            node.replace(dictionary_node, (node1, node2))

        # add the dictionary node the graph
        self.graph.add_node(dictionary_node)

        return self.compress_graph()
