
import random


class Graph(object):
    list_nodes = []
    node_count = 0

    def __init__(self, n_list, n_count):
        self.list_nodes = n_list
        self.node_count = n_count

    # @property
    # def list_nodes(self):
    #     return self.list_nodes
    #
    # @listNodes.setter
    # def list_nodes(self, list):
    #     self.list_nodes = list

    def add_edge(self, n1, n2):
        """
        Takes a dest node and a node to be added, calls Node class add_edge()
        Needs to be redefined by other graphs to check for duplicates,
        add additional rules for new graph implementations
        """
        n1.add_edge(n2)  # call add_edge() from node class (adds each node to the other node's adjacency list)

    def add_node(self, n):  # depends on implementation of Node class attr uid, i.e. n.uid assumed to be -1
        """
        Randomly selects an internal node, calls add_edge on both.
        Returns the external added node
        New implementations should redefine this function... this is not that valuable a function.
        """
        # check uid is not -1, if != -1, throw error
        if n.uid == -1:
            #################
            # TODO: CREATE UID HERE
            #################
            # set uid to some counter?
            rand_node = random.choice(self.list_nodes)
            self.add_edge(n, rand_node)
            self.node_count += 1
            return n
        else:  # uid is not -1
            raise IndexError('Expected uid of -1, cannot assign new uid')


class Cluster(Graph):

    # ONLY one cluster at a time in our system (otherwise more uid's)
    def add_graph(self, g):
        """
        Takes a random node from both graphs and calls addEdge, returns the list of nodes
        """
        node1 = random.choice(self.list_nodes)
        node2 = random.choice(g.list_nodes)
        self.add_edge(node1, node2)
        self.node_count += g.node_count

    # cluster should call AddEdge from Graph, which calls from node. Or just calls node directly?

    # def add_edge(self, g, c, gn, cn):
    #     """
    #     Takes two nodes from both graphs and calls addEdge
    #     This would be totally redundant
    #     """
