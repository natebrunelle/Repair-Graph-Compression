from nodes.nodes import EventType, Node, RepairNode

def breadthFirstSearch(graph, s):
    visited={}

    # mark all nodes not visited
    for node in graph.list_nodes:
        visited[node]=False

    queue = []

    curNode = graph.list_nodes[0]

    visited[curNode] = true;
    nodeQueue.push_back(curNode)

    stack = []

    while queue:
        curNode = queue.pop(0)
        stack.insert(0, curNode)

        for node in graph.list_nodes:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True

    return stack

def repair_breadth(compressed_graph):
    breadth_sort_nodes = []
    breadth_compressed = breadthFirstSearch(compressed_graph)
    for node in breadth_compressed:
        if node.value != float('inf'):
            breadth_sort_nodes.append(node)
            print(node)

    return breadth_sort_nodes
