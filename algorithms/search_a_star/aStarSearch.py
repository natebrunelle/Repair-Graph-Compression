import queue
from priorityQueue import PriorityQueue

def breadthFirstSearch(graph, s):
    visited={}

    # mark all nodes not visited
    for node in graph.list_nodes:
        visited[node]=False

    nodeQueue = queue.Queue(maxsize=500)

    visited[s] = true;
    nodeQueue.push_back(s)

    while not nodeQueue.empty():
        s = nodeQueue.get()
        for node in graph.list_nodes:
            if visited[node] == False:
                queue.put(node)
                visited[i] = True

    return nodeQueue

def repair_breadth(compressed_graph):
    topological_sort_nodes = []
    topsort_compressed = topSort(compressed_graph)
    for node in topsort_compressed:
        if node.value != float('inf'):
            topological_sort_nodes.append(node)

    return topological_sort_nodes
