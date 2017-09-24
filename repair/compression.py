''' Functions that will handle the compression stuff: 

Function 1: scan through the adjacency list of a node and update the dictionary
Function 2: get the top pair from the dictionary and replace it with new node everywhere it appears [then call function 1]

'''

# "pair": [count, [[node #, index],[ ... ]]]

def updateDictionary(adjList):
    repairDictionary={}
    for node in adjList.keys():
        for j in range(0, len(adjList[node])-1):
            numSet = (adjList[node][j],adjList[node][j+1])

            if numSet in repairDictionary.keys():
                repairDictionary[numSet][0] = repairDictionary[numSet][0]+1
                repairDictionary[numSet][1].append((node, j))
            else:
                repairDictionary[numSet] = [1, [(node, j)]]
    
    return repairDictionary

def repair(adjList):
    #generate the repair dictionary
    repairDictionary=updateDictionary(adjList)

    
