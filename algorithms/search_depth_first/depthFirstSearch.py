from nodes.nodes import EventType, Node, RepairNode

def visit(node, visited, graph, stack): #list, dic, list
    # mark current note as visited
    visited[node] = True

    # add to stack for the result
    stack.insert(0, node)

    # recursively iterate through the adjacent node paths
    for n in node.edges:
        if n not in graph.list_nodes:
            print("Error: an edge was found to a node not originally in the graph: " + str(n))
            continue
        if visited[n] == False:
            visit(n, visited, graph, stack)

def depthFirstSearch(graph):
    visited = {}

    # mark all nodes not visited
    for node in graph.list_nodes:
        visited[node] = False

    stack = []

    curNode = graph.list_nodes[0]
    i = 0

    # call function recursively on itself
    while(len(graph.list_nodes[i].edges) <= 0):
        i += 1
        curNode = graph.list_nodes[i]

    visit(curNode, visited, graph, stack)

    return stack

def repair_depth(compressed_graph):
    depth_search_nodes = []
    depth_compressed = depthFirstSearch(compressed_graph)
    for node in depth_compressed:
        #if isinstance(node, RepairNode):
        #    print("You have reached a compressed node.")
        if node.value != float('inf'):
            depth_search_nodes.append(node)

    return depth_search_nodes
