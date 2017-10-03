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


""""
Method which takes in a graph_dict object and decompresses the compressed
Re-Pair graph compression
"""
def decompress(compressedGraph):
    stack_list=[]
    
    for node in compressedGraph.keys():
        #doesn't connect to anything 
        if len(compressedGraph[node]) == 0:
            continue
        else:
            for alNode in reversed(compressedGraph[node]):
                #add each node in the related AL to stack
                stack_list.append(alNode)

            while len(stack_list) >= 0:
                #it's a literal
                if stack_list[-1][1] == False:
                    #!!!!todo!!!! doesn't work here down 
                    stack_list.pop()
                else:
                    # push the dictionary node pair onto stack
                    stack_list.append(compressedGraph[stack_list.pop()])  
    return compressedGraph

# if __name__ == "__main__":
#     print (decompression("compressed.txt"))



