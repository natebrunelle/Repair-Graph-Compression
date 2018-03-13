'''
Creates a cluster of graphs.

The graphs will be connected as specified by the parameters of the
function.
'''
import random
import string

from graphs.graph import Graph
from nodeAndRepairNode.nodes import Node


def weakly_connected_graphs(connection_num, graph_num, edge_num,
                            graph_factory):
    '''
    generates a group of connected graphs as specified by the parameters:

    connection_num: the number of connections we expect to see on ave
    graph_num: the number of graph in the cluster
    edge_num: the number of edges we expect to see within each graph on ave
    graph_factory: an instance of a graph factory to specify the kind of graphs
    '''

    # if bad input, silently correct it
    # need a min of graph_num connections to ensure everything is connected
    if connection_num < graph_num:
        connection_num = graph_num

    # get the graph size
    graph_size = graph_factory.num_of_nodes

    # fix bad input if needed
    if edge_num < graph_size:
        edge_num = graph_size

    # place holder for the graphs we will create
    # will help ensure every graph is connected at least once
    graphs = [[] for a in range(graph_num)]

    # create all the graphs
    for _ in range(graph_num):
        graphs.append(graph_factory.get_graph())

    counter = 0
    connected = [False for i in range(graph_num)]
    while counter < graph_num:
        random1 = random.randint(0, graph_num - 1)
        random2 = random.randint(0, graph_num - 1)
        if (random1 != random2 and \
            (connected[random1] is False or connected[random2] is False)):
            graphs[random1].add_edge(
                random.choice(graphs[random1].list_nodes),
                random.choice(graphs[random2].list_nodes))
            connected[random1] = True
            connected[random2] = True
            counter += 1

    while counter < connection_num:
        random1 = random.randint(0, graph_num - 1)
        random2 = random.randint(0, graph_num - 1)

        randomNode1 = random.choice(graphs[random1].list_nodes)
        randomNode2 = random.choice(graphs[random2].list_nodes)

        if (randomNode1 in random1.list_nodes
                or randomNode2 in random2.list_nodes):
            continue
        else:
            graphs[random1].add_edge(randomNode1, randomNode2)
            counter = counter + 1
