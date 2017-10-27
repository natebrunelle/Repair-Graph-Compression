#main function for the topological sort
def topologicalSort(graph):
    visited = [False]*self.visited
    stack=[]
    
    for i in range(graph.V):
        if(visited[i]==False):
            graph.topSort(i, visited, stack)

    print stack


#recursive function that pushes elements into the stack
def topSort(graph, v, visted, stack):
    visited[v] = True

    for i in graph[v]:
        if(visited[v] == False):
