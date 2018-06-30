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
    graphs = []

# create all the graphs
    for _ in range(graph_num):
        graphs.append(graph_factory.get_graph())

    node1 = random.choice(graphs[1].list_nodes)
    node2 = random.choice(graphs[0].list_nodes)

    graphs[0].add_edge(node2, node1)

#    for i in range(0,len(graphs[0].list_nodes)):
#        print(str(graphs[0].list_nodes[i]))

        #while counter < graph_num:
    counter = 0
        #random2 = random.randint(0, graph_num - 1)
#    for i in range(0,len(graphs)):
#        #if (random1 != random2 and ((connected[random1] is False or connected[random2] is False))):
#        random1 = random.randint(0, graph_num - 1)
#        print(random1)
#        print("connecting")
#        graphs[i].add_edge(random.choice(graphs[i].list_nodes),random.choice(graphs[random1].list_nodes))
#        counter += 1
#
#
#    while counter < connection_num:
#        print("second loop")
#        random1 = random.randint(0, graph_num - 1)
#        random2 = random.randint(0, graph_num - 1)
#
#        randomNode1 = random.choice(graphs[random1].list_nodes)
#        randomNode2 = random.choice(graphs[random2].list_nodes)
#
#        if (randomNode2 in graphs[random1].list_nodes or randomNode1 in graphs[random2].list_nodes):
#            continue
#        else:
#            graphs[random1].add_edge(randomNode1, randomNode2)
#            counter = counter + 1
    return graphs
