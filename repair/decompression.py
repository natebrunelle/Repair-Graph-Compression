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
    stack=[]
    
    for node in compressedGraph.keys():
        #doesn't connect to anything 
        if len(compressedGraph[node]) == 0:
            continue
        else:
            for alNode in reversed(compressedGraph[node]):
                #add each node in the related AL to stack
                stack.append(alNode)

            #empty the compressed AL
            compressedGraph[node]=[]
           
            while len(stack)>=1:
                #compression node; get replacement
                if stack[-1][1]:
                    replacement=compressedGraph[stack.pop()]
                    for rNode in reversed(replacement):
                        stack.append(rNode)
                else:
                    #literal, put it back
                    compressedGraph[node].append(stack.pop())

    decompressedGraph={}
    #clean up compression nodes
    for node in compressedGraph.keys():
        if not node[1]:
            decompressedGraph[node]=compressedGraph[node]
            
    return decompressedGraph
                
                
# if __name__ == "__main__":
#     print (decompression("compressed.txt"))



