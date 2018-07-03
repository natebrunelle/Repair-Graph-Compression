'''
Implementation of a graph.

This module provides the base graph used across everything.
Both the compression and decompression algorithms as well
as the cluster creating functions depend on it.
'''

import uuid


class Graph(object):
    ''' The graph class implementation '''

    def __init__(self, nodes=None):

        self.graph_id = uuid.uuid4().int
        if nodes:
            self.list_nodes = list()
            for node in nodes:
                self.add_node(node)

        else:
            self.list_nodes = list()

    def add_edge(self, n1, n2):
        """
        n2 is added to n1's adj list by calling Node.add_edge()
        n1 must be/will be a node in the graph (1st param),
        if it isn't, it's added to the graph
        n2 can be in graph, doesn't have to be (add_node not called),
        must be not equal to n1
        """
        # check if n1 not in graph
        if n1.graph_id != self.graph_id:
            self.add_node(n1)

        if n1 != n2:
            if n1.edges.count(n2) < 1:
                n1.add_edge(n2)

    def delete_edge(self, n1, n2):
        """
        :param n1: One of the two nodes that form the edge.
        :param n2: The second node that forms the edge.

        n2 is removed from n1's adj list by calling Node.delete_edge()
        One node must be in graph, the other doesn't have to be
        so can remove edges between graphs.
        """
        # if either in graph, try deleting
        if n1.graph_id == self.graph_id or n2.graph_id == self.graph_id:

            # remove n as many times as it appears in edges
            while n1.edges.count(n2) != 0:
                try:
                    n1.delete_edge(n2)
                except ValueError:
                    raise ValueError(
                        "Tried to remove a node that isn't present")
        else:
            raise ValueError(
                'Both Nodes not in graph, cannot delete edge from this graph')

    def delete_node(self, n):
        """
        removes the node from the graph,
        clears the adj list therein,
        resets the node.graph_id = None,
        and removes external references to the node
        """

        if n.graph_id == self.graph_id:
            n.edges = []
            self.list_nodes.remove(
                n)  # TODO: test this. delete the node, error if nonexistent
            n.graph_id = None

            # every outside reference to the node is deleted -
            # costly --> TODO this checks in the existing graph only
            for x in range(len(self.list_nodes)):
                self.list_nodes[x].delete_edge(n)

        else:
            raise ValueError('Node not in graph, cannot delete node')

    def add_node(self, n):
        """
        Adds a node to the Graph data structures, but it won't be connected by
        any edge. Duplicate nodes fail silently.
        New implementations should redefine this function.
        """
        if n not in self.list_nodes:  # prevent from adding >1x
            n.graph_id = self.graph_id
            self.list_nodes.append(n)

    def update(self, event):
        '''
        :param event: an event namedtuple

        Recieves an update when nodes change and reacts to the event.
        For node deletion, it will look through it's list and remove all
        references to that node. For node replacement, it will search for the
        replaced node and update it with the payload.

        .. note:: If it is a replacement update, the payload should include
                  the other node being replaced and the replacement node
        '''
        pass

    def __str__(self):
        """ Prints out graphs in a nice format """
        formatted = " "

        for node in self.list_nodes:
            formatted += str(node) + "\n"
            for adj_node in node.edges:
                formatted += "\t" + str(adj_node) + "\n"

        return formatted

    def __eq__(self, other):
        """
        Compares two graphs for equality

        .. warning:: This can be very slow.
        Don't compare two graphs unless you are in a test env.

        Two graphs are considered equal iff they have the same exact nodes,
        in the same exactly positions. The ordering of nodes makes a
        difference to our algorithms so graphs w/ the same nodes in
        different positions within the lists should be considered different.
        """

        if not isinstance(other, Graph):
            return False

        if len(self.list_nodes) != len(other.list_nodes):
            return False

        for node_index, node1 in enumerate(self.list_nodes):

            node2 = other.list_nodes[node_index]

            # check ids of "parent nodes"
            if node1.uid != node2.uid:
                return False

            # check ids of out going nodes
            for edge_index, edge1 in enumerate(node1.edges):
                edge2 = node2.edges[edge_index]

                if edge1.uid != edge2.uid:
                    return False

        return True
