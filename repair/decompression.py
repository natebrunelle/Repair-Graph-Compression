__author__ = "rt4hc"

#
#     Decompression for Re-Pair graph compression algorithm.
#
#     Functions:
#     @decompression - Main method which takes in the text file, and reads in the compressed lines of the adjacency list
#                      and makes the dictionary data structure to be used in the function @decompress
#     @decompress - Takes in a graph and dictionary list and substitutes in dictionary node literals into dictionary node
#
#

# def decompression(string):
#     """ Main method to read in the data file and create the dictionary data structure"""
#     f = open(string, 'r')
#     graph_adj_list = {}
#     dict_list = {}
#     for line in f:
#         input_string = line.split(" ")
#         # input_string = line.split(":")
#         node_string = input_string[0].strip('()')
#         node_tuple = tuple(node_string.split(","))
#         adj_string = input_string[1].strip()
#         adj_string = adj_string.strip("[](")
#         adj_string = adj_string.replace(")", "")
#         adj_string = adj_string.replace("'", "")
#         node_adj_list = adj_string.split(",")
#         print("The node_adjlist is: ")
#         print(node_adj_list)
#         graph_adj_list[node_tuple] = node_adj_list
#
#         if node_tuple[1] == "True":
#             dict_list[node_tuple] = node_adj_list
    # print(graph_adj_list)
    # print(dict_list)
    # return decompress(graph_adj_list, dict_list)

def decompress(graph_dict, dictionary):
    """"Method which takes in a graph_dict object and decompresses the compressed Re-Pair graph compression"""

    stack_list = []
    for edge_key in graph_dict:
        if len(graph_dict[edge_key]) == 0:
            continue
        else:
            for edge in reversed(graph_dict[edge_key]):
                stack_list.append(edge)
                graph_dict[edge_key].remove(edge)
            while len(stack_list) >= 0:
                if stack_list[-1][0] == 0: # check the flag portion of the tuple
                    graph_dict[edge_key].append(stack_list.pop())   # appends the literal into the graph_dict
                else:
                    stack_list.append(dictionary[stack_list.pop()[0]])  # push the dictionary node pair onto stack
                    stack_list.append(dictionary[stack_list.pop()[1]])
    return graph_dict

# if __name__ == "__main__":
#     print (decompression("compressed.txt"))



