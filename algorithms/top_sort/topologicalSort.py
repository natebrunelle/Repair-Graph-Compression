def visit(node, visited, graph, stack): #list, dic, list
    visited[node]=True #mark it permanently


    for n in node.edges:
        if n not in graph.list_nodes:
            print("Error: an edge was found to a node not originally in the graph: " + str(n))
            continue
        if visited[n]== False:
            visit(n, visited, graph, stack)
        
    stack.insert(0, node)

    
def topSort(graph):
    visited={}
    for node in graph.list_nodes: #mark all nodes not visited
        # if node.value == float('inf'):
        #     print("FOUND INFINITY!!!")
        visited[node]=False
    
    stack=[]
    for node in graph.list_nodes:
        if visited[node]==False:
            visit(node, visited, graph, stack)

    return stack

def repair_topological(compressed_graph):
    topological_sort_nodes = []
    topsort_compressed = topSort(compressed_graph)
    for node in topsort_compressed:
        if node.value != float('inf'):
            topological_sort_nodes.append(node)

    return topological_sort_nodes

