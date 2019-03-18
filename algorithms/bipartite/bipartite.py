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
    bipartite = True
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
                    bipartite = False
            new_D.append(v)
    # print("TRUE WOOHOO GRAPH IS BIPARTITE")
    # for each in new_D:
    #     print(each.color)
    return bipartite


def compression_aware_bipartite(compressed_graph):
    # print("Inside compression aware bipartite fun")
    # print("Printing graph that was passed in:\n", compressed_graph)

    Q = []
    D = []
    V = []
    nodes_created = {}
    colored_nodes = []
    # for node in compressed_graph.list_nodes:
    #     if node.value == float('inf'):
    #         D.append(node)

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
                nodes_created[adj.uid] = temp_adj
                # if not then add new node to dictionary
            temp.add_adj(temp_adj)
        nodes_created[node.uid] = temp
        V.append(temp) # append the bipartite nodes to a list V
        if temp.vertex.value == float('inf'):
            D.append(temp.vertex)
    # for each in V:
    #     print(each.vertex)
    V[0].color = "GRAY"
    V[0].predecessor = None
    print("size of graph: ", len(V))
    Q.append(V[0])
    #compressed_graph.todot()


    while(len(Q) != 0):
        u = Q.pop(0)
        # print("U: ", u.vertex)
        # print("U's color : ", u.color)
        for v in u.adj:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.predecessor = u
                Q.append(v)
            elif((v.color == u.color and u.vertex not in D ) or (v.color != u.color and u.vertex in D)):
                print("u", u.vertex, u.color)
                print("v", v.vertex, v.color)
                print("Sad, graph is not a bipartite :(")

                compressed_graph.todot()

                for each in V:
                    print(str(each.vertex.uid)[-4:], "[color = ", each.color.lower(), "];")
                print("}")

                return False
        if(u.predecessor != None):
            # if(((u.predecessor).color == "RED" and u.vertex not in D) or (u.predecessor).color == "BLUE" and u.vertex in D):
            if((u.predecessor).color == "RED"):
                u.color = "Blue"
            else:
                u.color = "RED"
        else:
            u.color = "RED"
        print("u", u.vertex, u.color)
        colored_nodes.append(u)


    # print("TRUE WOOHOO GRAPH IS BIPARTITE")
    # for each in colored_nodes:
    #     print(each.color)
    # for each in V:
    #     print(each.color)

    compressed_graph.todot()

    for each in V:
        print(str(each.vertex.uid)[-4:], "[color = ", each.color.lower(), "];")
    print("}")

    return True
    # return colored_nodes



def armans_algo(compressed_graph):
    Q = []
    D = []
    V = []
    nodes_created = {}
    colored_nodes = []
    # for node in compressed_graph.list_nodes:
    #     if node.value == float('inf'):
    #         D.append(node)

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
                nodes_created[adj.uid] = temp_adj
                # if not then add new node to dictionary
            temp.add_adj(temp_adj)
        nodes_created[node.uid] = temp
        V.append(temp)  # append the bipartite nodes to a list V
        if temp.vertex.value == float('inf'):
            D.append(temp.vertex)
    # for each in V:
    #     print(each.vertex)
    V[0].color = "GRAY"
    V[0].predecessor = None
    # print("size of graph: ", len(V))
    Q.append(V[0])
    # compressed_graph.todot()


    while (len(Q) != 0):
        u = Q.pop(0)
        # print("U: ", u.vertex)
        # print("U's color : ", u.color)
        for v in u.adj:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.predecessor = u
                Q.append(v)
            if(u.color == "BLUE" and u.vertex.value == float('inf') or u.color == "RED" and u.vertex.value != float('inf')):
                v.color = "BLUE"
            elif(u.color == "BLUE" and u.vertex.value != float('inf') or (u.color == "RED" and u.vertex.value == float('inf'))):
                v.color = "RED"
        if (u.predecessor != None):
            if ((u.predecessor).color == "RED" and (u.predecessor).vertex.value == float('inf') or
                            (u.predecessor).color == "BLUE" and u.predecessor.vertex.value != float('inf')):
                u.color = "RED"
            else:
                u.color = "BLUE"
        else:
            u.color = "RED"

        colored_nodes.append(u)



    # print(compressed_graph.todot())
    #
    # for each in V:
    #     print(str(each.vertex.uid)[-4:], "[color = ", each.color.lower(), "];")
    # print("}")

    bipartite = True

    for node in colored_nodes:
        for dest in node.adj:
            if(node.color == dest.color):
                if(node.vertex.value == float('inf') or dest.vertex.value == float('inf')):
                    continue
                print("This aint it chief!")
                print(node.color)
                print(dest.color)
                bipartite = False


    return bipartite

