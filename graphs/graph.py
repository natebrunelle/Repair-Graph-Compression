import random
import uuid


class Graph(object):
    list_nodes = []

    # node_count = 0

    def __init__(self, n_list):
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
            self.add_node(
                n2)  # add_node will prevent from adding 2x, silently, no error
        n1.add_edge(n2)  # directed graph, n2 doesn't add n1

    def delete_edge(self, n1, n2):
        if n1 in self.list_nodes and n2 in self.list_nodes:
            n1.delete_edge(n2)
            n2.delete_edge(n1)
        else:
            raise ValueError('Node(s) not in graph, cannot delete edges'
                             )  # try deleting from cluster instead?
        # what if that was the only edge attaching Node to graph? Use delete_node instead?
        # or is this too strict? use delete_node for that case instead?
        # In that case, it's a cluster. Our def of graph more limited.

    def delete_node(self, n):
        # free uid or something?
        if n in self.list_nodes:
            for x in n.edges:
                self.delete_edge(x, n)
                self.list_nodes.remove(
                    x)  # Maybe this needs to be a few lines further down?
                # TODO: need to test the above line
        else:
            raise ValueError('Node not in graph, cannot delete node')
        # REALLY need to test this...

    def add_node(
            self, n
    ):  # depends on implementation of Node class attr uid, i.e. n.uid assumed to be -1
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
            raise ValueError(
                'Node already in graph, use Graph.add_edge instead')
        return n

    def __str__(self):
        ''' Prints out graphs in a nice format '''
        formatted = " "

        for node in self.list_nodes:
            formatted += str(node) + "\n"
            for adj_node in node.edges:
                formatted += "\t" + str(adj_node) + "\n"

        return formatted


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
    node_count = 0

    def __init__(self, n_list, n_count):
        Graph.__init__(self, n_list, n_count)

    def add_edge(self, n1, n2):
        if n1 not in self.list_nodes or n2 not in self.list_nodes:
            self.add_node(n1)
            self.add_node(n2)
        if (n1 not in n2.edges) or (n2 not in n1.edges):
            n1.add_edge(n2)
            n2.add_edge(n1)
        return 0

    def delete_edge(self, n1, n2):
        if n1 in self.list_nodes and n2 in self.list_nodes:
            raise ValueError('Edge removal violates complete graph structure')
        else:
            n1.delete_edge(n2)
            n2.delete_edge(n1)
        return 0

    def delete_node(self, n):
        if n.uid == -1:
            #TODO: create UID here

            if n in self.list_nodes:
                self.list_nodes.remove(n)
                self.node_count -= 1
                for x in n.edges:
                    self.delete_edge(x, n)
            else:
                raise ValueError('Node already not in graph')
        return 0

    def add_node(self, n):
        if n.uid == -1:
            #TODO: create UID here

            if n not in self.list_nodes:
                self.list_nodes.append(n)
                self.node_count += 1
                for i in range(len(self.list_nodes)):
                    self.list_nodes[i].add_edge(n)
            else:
                raise ValueError('Node already in graph')
        return 0

    """
    Since every node ends up being connected to every other node
    anyway, this method is effectively the same as add_node
    """
    # def add_node_rand(self, n):
    #
    #     return 0


"""
These graphs will consist of many nodes all connected
only to one central hub node
"""


class HubAndSpokeGraph(Graph):
    list_nodes = []
    node_count = 0

    def __init__(self, n_list, n_count, hub):
        Graph.__init__(self, n_list, n_count)
        self.hub_node = hub

    def add_edge(self, n1, n2):
        if self.hub_node not in (n1, n2):
            raise ValueError('Hub node not targeted')
        else:
            if (n1 not in n2.edges) and (n2 not in n1.edges):
                n1.add_edge(n2)
                n2.add_edge(n1)
        return 0

    def delete_edge(self, n1, n2):

        if (n1 in n2.edges) and (n2 in n1.edges):
            n1.delete_edge(n2)
            n2.delete_edge(n1)
        else:
            raise ValueError('Edge does not exist')
        return 0

    def delete_node(self, n):
        if n.uid == -1:
            # TODO: create UID here

            if n in self.list_nodes:
                self.list_nodes.remove(n)
                for i in range(len(self.list_nodes)):
                    self.list_nodes[i].delete_edge(n)
            else:
                raise ValueError('Node already does not exist in graph')

        return 0

    def add_node(self, n):
        if n.uid == -1:
            # TODO: create UID here

            if n not in self.list_nodes:
                self.list_nodes.append(n)
                self.node_count += 1
                n.add_edge(self.hub_node)
            else:
                raise ValueError('Node already exists in graph')

        return 0

    """
    Not necessary since an add is not allowed unless the hub is
    targeted; adding a random node is effectively no different
    than adding a particular node
    """
    # def add_node_rand(self, n):
    #
    #     return 0
