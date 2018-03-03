''' Implementation of the Repair algorithm
Uses the Graph and Node classes to compress a graph.
'''
import math
from pdb import set_trace as bp
# queue is not thread safe
from queue import Empty, PriorityQueue

from nodeAndRepairNode.nodes import RepairNode


class RepairPriorityQueue(PriorityQueue):
    ''' A priority queue implementation that overrides a few methods to make python's
    queue implementation work the way we need it to

    Note that both put and get default block to False instead of true.
    This makes the implementation closer to put_nowait and get_nowait.
    It makes a difference in a multithreaded setup'''

    def __init__(self, pairs=None):
        super().__init__()
        self.old_counts = dict()

        # TODO run a regex or something to make sure the pairing is right
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

        # check dic TODO: find something more better this is O(n)
        try:
            old_freq = self.old_counts[item[1]]
            item_new_freq = old_freq - 1
        except KeyError:
            item_new_freq = item[0]

        # update the freq if needed
        item = (item_new_freq, item[1])

        # add it to the dict
        self.old_counts[item[1]] = item[0]

        # enqueue it
        super().put(item)

    def get(self, block=False, timeout=None):
        ''' Uses the priority queue to get the most freq.
        Then updates the dictionary as well. '''

        freq_pair = super(RepairPriorityQueue, self).get()
        try:
            del self.old_counts[freq_pair[1]]
        except KeyError:
            pass  # ignore if the value never existed
        except Empty:
            raise Exception("Empty")

        return freq_pair

    def __str__(self):
        ''' prints the dictionary in a nice format

        This will hopefully be helpful in understanding the heap's state
        since we cannot directly iterate on that '''

        formatted_string = " "

        for key in self.old_counts:
            formatted_string += "[" + str(key[0]) + ", " + str(
                key[1]) + "]\t\t" + str(self.old_counts[key]) + "\n"

        return formatted_string


class Repair:
    ''' The main class that holds everything together '''

    def __init__(self, uncompressed_graph, dictionary=None):
        self.graph = uncompressed_graph

        # inject dictionary, or create new
        if dictionary and isinstance(RepairPriorityQueue, dictionary):
            self.dictionary = dictionary
        else:
            self.dictionary = RepairPriorityQueue()

    def update_dictionary(self):
        ''' Updates the internal dictionary

        Takes in a graph object, scans it, and updates the priority queue with
        new pairs and their frequency. Should only be called by compress_graph '''

        # this is really bad...we shouldn't reconstruct the thing every time
        # but I can't think if anything better for now ...
        self.dictionary = RepairPriorityQueue()

        # for every node, loop through its edges and check pairs
        for node in self.graph.list_nodes:
            for index, adj_node in enumerate(node.edges):
                if index + 1 == len(node.edges):
                    break

                # make a pair and pass it on
                pair = (1, (adj_node, node.edges[index + 1]))

                # see our queue implementation on how duplicates are handled
                self.dictionary.put(pair)

    def compress(self):
        ''' Compresses the graph passed into the class

        It updates the iternal dictionary, creates a dictionary node for the most,
        common pair, unless all are unique (freq == 1), recurse.
        '''

        # update dictionary
        self.update_dictionary()

        # check for empty dict
        if self.dictionary.empty():
            return self.graph

        # get the most common pairs in the graph
        most_common_pair = self.dictionary.get()

        # recursion base case, all unique
        if most_common_pair[0] == -1:
            return self.graph

        # unpack the pair
        node1 = most_common_pair[1][0]
        node2 = most_common_pair[1][1]

        # create a dictionary node
        dictionary_node = RepairNode(math.inf, node1, node2)

        # TODO move this to graph
        # loop through all nodes and replace the pair
        for node in self.graph.list_nodes:
            node.replace(node1, node2, dictionary_node)

        # add the dictionary node the graph
        self.graph.add_node(dictionary_node)

        return self.compress()
