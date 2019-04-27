def visit(node, visited, graph, stack): #list, dic, list
    # mark current note as visited
    visited[node] = True

    # recursively iterate through the adjacent node paths
    for n in node.edges:
        if n not in graph.list_nodes:
            print("Error: an edge was found to a node not originally in the graph: " + str(n))
            continue
        if visited[n] == False:
            visit(n, visited, graph, stack)

    stack.insert(0, node)


def depthFirstSearch(graph):
    visited = {}

    # mark all nodes not visited
    for node in graph.list_nodes:
        visited[node] = False

    stack = []
    visit(graph.list_nodes[0], visited, graph, stack)

    return stack

def repair_depth(compressed_graph):
    depth_search_nodes = []
    depth_compressed = depthFirstSearch(compressed_graph)
    for node in depth_compressed:
        if node.value != float('inf'):
            depth_search_nodes.append(node)

    return depth_search_nodes
