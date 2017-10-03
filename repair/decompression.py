__author__ = "rt4hc"



def decompress(graph):
    """"Method which takes in a graph object and decompresses the compressed Re-Pair graph compression"""
    # The graph should be represented as a compressed adjacency list
    # Adjacency list format
    # 1: [B]
    # 6: [B]
    # A: [2, 3]
    # B: [A, 4]

    # Iterative solution
    keys = []
    for vertex in graph:       # Append all the keys of the adjacency list into another list
        for edge in vertex:
            if edge in graph:       # If edge is a valid compressed pair in the adjacency list
                vertex.remove(edge)     # Substitute the vertex with the nodes
                vertex.append(graph[vertex])

    # Recursive solution
    # Base case is if there are no more "pairs"




