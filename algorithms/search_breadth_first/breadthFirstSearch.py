import queue

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
    breadth_sort_nodes = []
    breadth_compressed = breadthFirstSearch(compressed_graph)
    for node in breadth_compressed:
        if node.value != float('inf'):
            breadth_sort_nodes.append(node)

    return breadth_sort_nodes
