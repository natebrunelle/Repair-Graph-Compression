'''
.. module:: Clusters
.. moduleauthor:: Yonathan Fisseha

A group of graphs need a light wrapper around them  because
if we simply  put them into a list, algorithms operating on
the cluster will only see one adjacency list. This is a problem
since, for example, repair will end up compressing only one of the
the graphs instead of the whole cluster.

This class provides this wrapper.
'''

from graphs.graph import EventType, Graph


class Cluster(Graph):
    '''
    A simple wrapper for a list of graphs.

    :param graphs: A list of graphs which it will convert into a cluster.
    :return_type: graph
    '''

    def __init__(self, cluster_graphs):
        self.list_nodes = []
        self.add_nodes_from_graphs(cluster_graphs)
        self.sort_nodes()

    def add_nodes_from_graphs(self, cluster_graphs):
        '''
        Adds all nodes from a graph to the clusters adjacency list.
        :return_type: graph
        '''
        for new_graph in cluster_graphs:
            for node in new_graph.list_nodes:
                node.observe(self)
                self.list_nodes.append(node)

    def add_node(self, node):
        '''
        Overrides the parent to avoid graph_id check
        '''
        self.list_nodes.append(node)

    def sort_nodes(self):
        '''
        Sorts the nodes by graph_id then by node_id. This is important
        for the repair algorithm to work correctly because we want nodes
        of the same graph to be clustered around together. So we do a stable
        sort by graph_id, then by node_id.
        '''

        self.list_nodes.sort(key=lambda node: (node.graph_id, node.uid))

    def update(self, event):
        '''
        Event handler for nodes
        '''

        if event.event_type == EventType.node_deleted:
            self.list_nodes.remove(event.observable)

        elif event.event_type == EventType.node_replaced:
            node1 = event.observable
            node2 = event.payload[0]
            replacement_node = event.payload[1]

            self.list_nodes.remove(node1)
            self.list_nodes.remove(node2)
            self.list_nodes.append(replacement_node)
