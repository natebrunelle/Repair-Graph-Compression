def visit(node, visited, graph, stack): #list, dic, list
    visited[node]=True #mark it permanently

    for n in graph[node]:
        if visited[n]== False:
            visit(n, visited, graph, stack)
        
    stack.insert(0, node)

    
def topSort(graph): #dic of node: [list of nodes]
    visited={}
    for node in graph.keys(): #mark all nodes not visited 
        visited[node]=False
    
    stack=[]
    for node in graph.keys():
        if visited[node]==False:
            visit(node, visited, graph, stack)
            
    return stack
