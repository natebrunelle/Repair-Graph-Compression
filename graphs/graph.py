
import random

class Graph(object):
    list_nodes = []
    # node_count = 0
    # TODO: Graph needs it's own unique ID, it will inject to every node as it gets added
    # then stable sort by each graph uuid, then sort by each node uuid so nodes in the same graph will be closer,
    # needed for compression algorithm

    def __init__(self, n_list=None):  # TODO: check usage of None
        self.list_nodes = n_list
        # self.node_count = n_count  # this removed b/c have UUID's

    def add_edge(self, n1, n2):
        """
        Takes a dest node and a node to be added, calls Node class add_edge()
        Needs to be redefined by other graphs to check for duplicates,
        add additional rules for new graph implementations
        """
        if n1 not in self.list_nodes or n2 not in self.list_nodes:
            self.add_node(n1)
            self.add_node(n2)  # add_node will prevent from adding 2x, silently, no error
        n1.add_edge(n2)  # directed graph, n2 doesn't add n1

    def delete_edge(self, n1, n2):
        if n1 in self.list_nodes and n2 in self.list_nodes:
            n1.delete_edge(n2)
            n2.delete_edge(n1)
        else:
            raise ValueError('Node(s) not in graph, cannot delete edges')  # try deleting from cluster instead?
        # what if that was the only edge attaching Node to graph? Use delete_node instead?
        # or is this too strict? use delete_node for that case instead?
        # In that case, it's a cluster. Our def of graph more limited.

    def delete_node(self, n):
        # free uid or something?
        if n in self.list_nodes:
            for x in n.edges:
                self.delete_edge(x, n)
                self.list_nodes.remove(x)  # Maybe this needs to be a few lines further down?
                # TODO: need to test the above line
        else:
            raise ValueError('Node not in graph, cannot delete node')
        # REALLY need to test this...

    def add_node(self, n):  # depends on implementation of Node class attr uid, i.e. n.uid assumed to be -1
        """
        Returns the external added node.
        Adds a node to the Graph data structures, but it won't be connected by any edge.
        New implementations should redefine this function.
        """
        if n not in self.list_nodes:  # prevent from adding >1x
            self.list_nodes.append(n)
            # self.node_count += 1
        # else:
        #     raise ValueError('Node already in graph, use Graph.add_edge instead')
        # TODO: add Warnings here instead so fail quietly but is still tracked
        return n

    def add_node_rand(self, n):
        """
        Randomly selects an internal node, calls add_edge on both.
        Returns the external added node.
        This does not add a node to the Graph data structures alone, but also adds a random edge.
        """
        rand_node = random.choice(self.list_nodes)
        if n not in self.list_nodes:  # prevent from adding >1x
            self.add_edge(n, rand_node)
            self.list_nodes.append(n)
            # self.node_count += 1
        else:
            raise ValueError('Node already in graph, use Graph.add_edge instead')
        return n


class Cluster(Graph):

    # ONLY one cluster at a time in our system (otherwise more uid's)
    def add_graph(self, g):
        """
        Takes a random node from both graphs and calls addEdge, returns the list of nodes
        """
        node1 = random.choice(self.list_nodes)
        node2 = random.choice(g.list_nodes)
        self.add_edge(node1, node2)
        # self.node_count += g.node_count

    # cluster should call AddEdge from Graph, which calls from node. Or just calls node directly?

    # def add_edge(self, g, c, gn, cn):
    #     """
    #     Takes two nodes from both graphs and calls addEdge
    #     This would be totally redundant
    #     """


"""
These graphs will consist exclusively of nodes which
are connected to every other node in the graph
"""


class CompleteGraph(Graph):
    list_nodes = []

    def __init__(self, n_list=None):  # n_list = None allows us to optionally pass all the nodes we want at start
        if n_list:
            Graph.__init__(n_list)  # this is a placeholder
            # connect all nodes in n_list here
            # may need to redesign functions or add new functions here.
            # Maybe a hub and spoke function called recursively?
        Graph.__init__(self, n_list)

    def add_edge(self, n1, n2):
        if n1 not in self.list_nodes or n2 not in self.list_nodes:
            self.add_node(n1)
            self.add_node(n2)
        if n1 not in n2.edges:
            n1.add_edge(n2)  # directed graph

    def delete_edge(self, n1, n2):
        if n1 in self.list_nodes and n2 in self.list_nodes:  # if edge inside graph and not out into cluster
            raise ValueError('Edge removal violates complete graph structure')
            # TODO: maybe this should be a warning, not an error, so it doesn't stop the program?
        else:
            n1.delete_edge(n2)  # directed graph

    def delete_node(self, n):
        if n in self.list_nodes:
            self.list_nodes.remove(n)
            for x in n.edges:
                self.delete_edge(x, n)
        else:
            raise ValueError('Node not in graph')  # TODO: call add_node here instead

    def add_node(self, n):  # TODO: Simonne check this
        if n not in self.list_nodes:
            self.list_nodes.append(n)
            for i in range(len(self.list_nodes)):
                self.list_nodes[i].add_edge(n)
        else:
            raise ValueError('Node already in graph')

    """
    Since every node ends up being connected to every other node
    anyway, this method is effectively the same as add_node
    """
    # def add_node_rand(self, n):
    #
    #     return 0


"""
These graphs will consist of many nodes all connected
only to one central hub node.
This graph should implement from the top down a guaranteed connected graph 
rather than the Graph class' possible bottom-up of creation of a connected graph
"""


class HubAndSpokeGraph(Graph):
    list_nodes = []

    def __init__(self, hub, n_list=None):
        Graph.__init__(self, n_list)
        self.hub_node = hub

    def add_edge(self, n1, n2):
        if self.hub_node not in (n1, n2):
            raise ValueError('Hub node not targeted')  # wouldn't it be easier to change the parameters?
            # Or overriding, so can't? IDK.  Is it necessary to override/can we create a new function?
        else:
            if n2 not in n1.edges:  # TODO: fix other classes so they look like this
                n1.add_edge(n2)  # n2 is appended to n1's list

    def delete_edge(self, n1, n2):
        if n1 in n2.edges:
            n1.delete_edge(n2)
        else:
            raise ValueError('Edge does not exist')  # TODO: should exit quietly instead?

    def delete_node(self, n):
        if n in self.list_nodes:
            # TODO: call delete_edge remove n from nodes that list it in otherNode.edge
            # see general Graph class above
            self.list_nodes.remove(n)
            for i in range(len(self.list_nodes)):
                self.list_nodes[i].delete_edge(n)
        else:
            raise ValueError('Node does not exist, cannot be deleted')

    def add_node(self, n):
        if n not in self.list_nodes:
            self.list_nodes.append(n)
            n.add_edge(self.hub_node)
        else:
            raise ValueError('Node already exists in graph')
            # TODO: exit/fail quietly w/out error b/c called by other functions

    """
    Not necessary since an add is not allowed unless the hub is
    targeted; adding a random node is effectively no different
    than adding a particular node
    """
    # def add_node_rand(self, n):
    #
