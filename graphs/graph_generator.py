# pylint: disable=all
'''
Creates a cluster of graphs.

The graphs will be connected as specified by the parameters of the
function.
'''
import random


def pick_two_different_items(all_items):
    '''
    Picks two different items from a list of items

    :param all_items: a list of all items to pick from
    '''

    while True:
        item1 = random.choice(all_items)
        item2 = random.choice(all_items)

        if item1 != item2:
            return item1, item2


def randomly_create_edges(graphs, edge_num):
    '''
    Randomly creates the specified number of edges in the graph
    without duplicating connections.

    ..warning: It will infinite loop if you  pass a graph
    with fewer nodes that edge_num.
    '''

    for graph in graphs:
        current_edge_num = 0
        while current_edge_num < edge_num:
            node1, node2 = pick_two_different_items(graph.list_nodes)

            if node1 not in node2.edges:
                node2.add_edge(node1)
                current_edge_num += 1
            elif node2 not in node1.edges:
                node1.add_edge(node2)
                current_edge_num += 1

    return graphs


def pick_nodes_connect_incr(graph1, graph2, counter):
    '''
    Extracts the edge making logic between two graphs.
    Picks a node from graph1 and another from graph2.
    .. note:: The edge goes from graph1 to graph1
    '''
    node1 = random.choice(graph1[1].list_nodes)
    node2 = random.choice(graph2[1].list_nodes)

    node1.add_edge(node2)

    graph1[0] = True
    counter += 1

    return graph1, graph2, counter


def weakly_connected_graphs(connection_num, graph_num, edge_num,
                            graph_factory):
    '''
    Generates a group of connected graphs as specified by the parameters:

    :param connection_num: the number of connections we expect to see on ave
    :param graph_num: the number of graph in the cluster
    :param edge_num: the number of edges expected within each graph
    :param graph_factory: an instance of a graph factory to

    :return: A group of 1 or more graphs connected into one large graph
    :return_type: Graph
    '''

    # validate the params
    if connection_num < graph_num:
        raise ValueError("The number of connections must at least equal\
            the number of graphs.")

    graph_size = graph_factory.num_of_nodes

    if edge_num < graph_size:
        raise ValueError("The number of edges must be at least\
                equal to number of nodes per graph")

    # create all the graphs
    graphs = []
    for _ in range(graph_num):
        graphs.append(graph_factory.get_graph())

    # we start out with 0 connections/every graph not connected
    connections_so_far = 0
    connected = [[False, graph] for graph in graphs]

    # make sure at least every graph is connected once
    while connections_so_far < len(graphs):
        graph1, graph2 = pick_two_different_items(connected)

        if graph1[0] is False:
            graph1, graph2, connections_so_far = pick_nodes_connect_incr(
                graph1, graph2, connections_so_far)

        if graph2[0] is False:
            graph1, graph2, connections_so_far = pick_nodes_connect_incr(
                graph2, graph1, connections_so_far)

    # now we can use the rest of the connections randomly
    while connections_so_far < connection_num:
        graph1, graph2 = pick_two_different_items(connected)
        graph1, graph2, connections_so_far = pick_nodes_connect_incr(
            graph1, graph2, connections_so_far)

    return graphs
