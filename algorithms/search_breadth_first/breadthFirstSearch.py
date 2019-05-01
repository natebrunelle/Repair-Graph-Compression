from nodes.nodes import EventType, Node, RepairNode

def breadthFirstSearch(graph):
    visited={}

    # mark all nodes not visited
    for node in graph.list_nodes:
        visited[node]=False

    queue = []

    curNode = graph.list_nodes[0]
    i = 0

    # call function recursively on itself
    while(len(graph.list_nodes[i].edges) <= 0):
        i += 1
        curNode = graph.list_nodes[i]

    visited[curNode] = True;
    queue.append(curNode)

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

    return breadth_sort_nodes
