
import random
import uuid


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
        if n1 not in self.list_nodes or n2 not in self.list_nodes:
            self.add_node(n1)
            self.add_node(n2)  # add_node will prevent from adding 2x
        n1.add_edge(n2)
        n2.add_edge(n1)
        # raise ValueError('Node(s) not in graph, use Graph.add_node first')

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
                self.list_nodes.remove(x) # Maybe this needs to be a few lines further down?
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
        # check uid is not -1, if != -1, throw error
        if n.uid == -1:
            # TODO: CREATE UID HERE
            # uuid.uuid1() or uuid.uuid4()  # 1 is based on host id and time, 4 is random
            # changing an int field to another class might be a problem?
            # set uid to some counter?

            if n not in self.list_nodes:  # prevent from adding >1x
                self.list_nodes.append(n)
                self.node_count += 1
            # else:
                # raise ValueError('Node already in graph, use Graph.add_edge instead')
            return n
        else:  # uid is not -1
            raise IndexError('Expected uid of -1, cannot assign new uid')

    def add_node_rand(self, n):
        """
        Randomly selects an internal node, calls add_edge on both.
        Returns the external added node.
        This does not add a node to the Graph data structures alone, but also adds a random edge.
        """
        # check uid is not -1, if != -1, throw error
        if n.uid == -1:
            # TODO: CREATE UID HERE
            # uuid.uuid1() or uuid.uuid4()  # 1 is based on host id and time, 4 is random
            # changing an int field to another class might be a problem?
            # set uid to some counter?

            rand_node = random.choice(self.list_nodes)
            if n not in self.list_nodes:  # prevent from adding >1x
                self.add_edge(n, rand_node)
                self.list_nodes.append(n)
                self.node_count += 1
            else:
                raise ValueError('Node already in graph, use Graph.add_edge instead')
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
