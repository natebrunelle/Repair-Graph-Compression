'''
Creates a cluster of graphs.

The graphs will be connected as specified by the parameters of the
function.
'''
import random
import string

from graphs.graph import Graph
from nodeAndRepairNode.nodes import Node


def weakly_connected_graphs(connection_num, graph_size,
                            edge_num, graph_factory):
    '''
    generates a group of connected graphs as specified by the parameters:

    connection_num: the number of connections we expect to see on ave
    graph_size: the number of nodes we expect in each graph
    edge_num: the number of edges we expect to see within each graph on ave
    graph_factory: an instance of a graph factory to specify the kind of graphs
    '''

    # if bad input, silently correct it
    # need a min of graph_num connections to ensure everything is connected
    if connection_num < graph_num:
        connection_num = graph_num

    if edge_num < graph_size:
        edge_num = graph_size

    # place holder for the graphs we will create
    # will help ensure every graph is connected at least once
    graphs = [ [] for a in range(graph_num) ]

    # create all the graphs
    for graph_index in range(graph_num):
        graphs.append(graph_factory.get_graph())

    #------------what's happening lol---------------
    counter = 0
    connected = [ False for i in range(graphNum)]
    while(counter < graphNum):
        random1 = random.randint(0, graphNum-1)
        random2 = random.randint(0, graphNum-1)
        if(random1 != random2 and (connected[random1] == false or connected[random2] == false)):
            graphs[random1].add_edge(random.choice(graphs[random1].list_nodes), random.choice(graphs[random2].list_nodes))
            connected[random1] = True
            connected[random2] = True
            counter = counter+1

    while(counter < number_of_connections):
        random1 = random.randint(0, graphNum-1)
        random2 = random.randint(0, graphNum-1)
        #NEED TO CHECK IF THEY ARE ALREADY CONNECTED --> if they are connected then repeat until you find a pair that hasn't been connected && connect them
        graphs[random1].add_edge(random.choice(graphs[random1].list_nodes), random.choice(graphs[random2].list_nodes))
        counter=counter+1
