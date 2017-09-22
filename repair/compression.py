''' Functions that will handle the compression stuff: 

Function 1: scan through the adjacency list of a node and update the dictionary
Function 2: get the top pair from the dictionary and replace it with new node everywhere it appears [then call function 1]

'''
#todo: how should we identify nodes that are there for re-pairing and actual nodes?

# "pair": [count, [[node #, index],[ ... ]]]
repairDictionary={}
