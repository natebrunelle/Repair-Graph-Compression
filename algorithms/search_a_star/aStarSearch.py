import queue
from nodes.nodes import EventType, Node, RepairNode

def aStarSearch(graph):
    visited={}

    # mark all nodes not visited
    for node in graph.list_nodes:
        visited[node]=False

    nodeQueue = queue.PriorityQueue()

    curNode = graph.list_nodes[0]
    i = 0

    # call function recursively on itself
    while(len(graph.list_nodes[i].edges) <= 0):
        i += 1
        curNode = graph.list_nodes[i]

    visited[curNode] = True;
    nodeQueue.put((len(curNode.edges), curNode))

    stack = []

    while not nodeQueue.empty():
        curNode = nodeQueue.get()
        stack.insert(0, curNode)

        for node in graph.list_nodes:
            if visited[node] == False:
                nodeQueue.put((len(node.edges), node))
                visited[node] = True

    return stack

def repair_star(compressed_graph):
    star_sort_nodes = []
    star_compressed = aStarSearch(compressed_graph)
    for node in star_compressed:
        if node[1] != float('inf'):
            star_sort_nodes.append(node)

    return star_sort_nodes
