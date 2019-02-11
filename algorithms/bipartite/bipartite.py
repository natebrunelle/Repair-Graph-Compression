#bipartite assignment
#from collections import deque


# def bipartite(self, c_graph):
#     queue = [] #initialize a queue
#     for node in c_graph:
#         temp = bipartite_node(node)
#
#     return False # if the graph is not a repair bipartite graph
class bipartite_node:
    def __init__(self, v):
        self.adj = []
        self.vertex = v
        self.color = -1

    # def vertex(self,v):
    #     self.attributes.append(v)

    # def color(self,node_color):
    #     """adds a color to the attributes list"""
    #     self.color = node_color

    def predecessor(self, pi):
        """adds a predecessor pi to the bipartite node"""
        self.predecessor = pi

    def add_adj(self, adj_node):
        self.adj.append(adj_node)


def normal_bipartite(uncompressed_graph):
    # print("Inside Normal Bipartite Func")
    nodes_created = {}
    Q = []
    D = []
    visited = []
    for node in uncompressed_graph.list_nodes:
        temp = bipartite_node(node)
        if node.uid in nodes_created.keys():  # if the key is in the dictionary
            temp = nodes_created[node.uid]
        for adj in node.edges:
            temp_adj = bipartite_node(adj)
            # temp_adj.color = -1
            if adj.uid in nodes_created.keys():  # if the key is in the dictionary
                temp_adj = nodes_created[adj.uid]  # the temp_adj = the node
            else:
                nodes_created[adj.uid] = temp_adj  # if not then add new node to dictionary
            temp.add_adj(temp_adj)
        nodes_created[node.uid] = temp
        D.append(temp)
    D[0].color = 1
    new_D = []
    Q.append((D[0]))
    visited.append(D[0])
    while(len(Q) != 0):
        # print(Q)
        u = Q.pop(0)
        # print(u.adj)
        next_color = 1 - int(u.color)
        for v in u.adj:
            if v not in visited:
                v.color = next_color
                Q.append(v)
                visited.append(v)
            else:
                if v.color == u.color:
                    # print("Sad...graph is NOT bipartite :(")
                    return False
            new_D.append(v)
    # print("TRUE WOOHOO GRAPH IS BIPARTITE")
    # for each in new_D:
    #     print(each.color)
    return True


def compression_aware_bipartite(compressed_graph):
    # print("Inside compression aware bipartite fun")
    Q = []
    D = []
    V = []
    nodes_created = {}
    colored_nodes = []
    for node in compressed_graph.list_nodes:
        if node.value == float('inf'):
            D.append(node)

    for node in compressed_graph.list_nodes:
        temp = bipartite_node(node)
        temp.color = "WHITE"
        temp.predecessor(None)
        if node.uid in nodes_created.keys():  # if the key is in the dictionary
            temp = nodes_created[node.uid]
        for adj in node.edges:
            temp_adj = bipartite_node(adj)
            temp_adj.color = "WHITE"
            temp_adj.predecessor(None)
            # temp_adj.color = -1
            if adj.uid in nodes_created.keys():  # if the key is in the dictionary
                temp_adj = nodes_created[adj.uid]  # the temp_adj = the node
            else:
                nodes_created[adj.uid] = temp_adj  # if not then add new node to dictionary
            temp.add_adj(temp_adj)
        nodes_created[node.uid] = temp
        V.append(temp) # append the bipartite nodes to a list V
    # for each in V:
    #     print(each.vertex)
    V[0].color = "GRAY"
    V[0].predecessor = None
    Q.append(V[0])
    while(len(Q) != 0):
        u = Q.pop(0)
        # print("U: ", u.vertex)
        # print("U's color : ", u.color)
        for v in u.adj:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.predecessor = u
                Q.append(v)
            elif((v.color == u.color and u.vertex not in D) or (v.color != u.color and u.vertex in D)):
                # print("V.color: ", v.color)
                # print("U.color: ", u.color)
                # print("Sad, graph is not a bipartite :(")
                return False
        if(u.predecessor != None):
            if(((u.predecessor).color == "RED" and u.vertex not in D) or (u.predecessor).color == "BLUE" and u.vertex in D):
                u.color = "Blue"
            else:
                u.color = "RED"
        else:
            u.color = "RED"
        colored_nodes.append(u)
    # print("TRUE WOOHOO GRAPH IS BIPARTITE")
    # for each in colored_nodes:
    #     print(each.color)
    # for each in V:
    #     print(each.color)
    return True
    # return colored_nodes


