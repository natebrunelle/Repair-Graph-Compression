''' Implementation of the Repair algorithm
Uses the Graph and Node classes to compress a graph.
'''
import math
# queue is not thread safe
from queue import PriorityQueue


class RepairPriorityQueue(PriorityQueue):
    ''' A priority queue implementation that overrides a few methods to make python's
    queue implementation work the way we need it to

    Note that both put and get default block to False instead of true.
    This makes the implementation closer to put_nowait and get_nowait.
    It makes a difference in a multithreaded setup'''

    def __init__(self, pairs=None):
        super().__init__()
        self.old_counts = dict()

        if pairs:
            for pair in pairs:
                self.put(pair)

    def put(self, item, block=False, timeout=None):
        ''' Uses a dictionary and the queue to handle duplicates

        Get the pair from the dictionary which contains the same number of items.
        If it finds the time, update the freq before inserting.
        Otherwise put into the queue '''

        inversed_freq = item[0] * -1
        item = (inversed_freq, item[1])

        # check dic
        try:
            old_item = self.old_counts[item[0]]
        except KeyError:
            old_item = None

        # update the freq if needed
        if old_item:
            item[1] -= old_item

        # enqueue it
        super().put(item)

    def get(self, block=False, timeout=None):
        ''' Uses the priority queue to get the most freq. Then updates the dictionary as well. '''
        freq_pair = super(RepairPriorityQueue, self).get()

        try:
            del self.old_counts[freq_pair[1]]
        except KeyError:
            pass  # ignore if the value never existed

        return freq_pair


class Repair:
    ''' The main class that holds everything together '''

    def __init__(self, uncompressed_graph, dictionary=None):
        self.graph = uncompressed_graph

        # inject dictionary, or create new
        if not dictionary:
            self.dictionary = RepairPriorityQueue()
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
        dictionary_node = RepairNode(math.inf, node1, node2)

        # loop through all nodes and replace the pair
        for node in self.graph.list_nodes:
            node.replace(dictionary_node, (node1, node2))

        # add the dictionary node the graph
        self.graph.add_node(dictionary_node)

        return self.compress_graph()
