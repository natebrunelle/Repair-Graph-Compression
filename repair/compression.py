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

def getMostCommon(repairDictionary):
    maxCount=0
    maxKey=()
    
    for key in repairDictionary.keys():
        if repairDictionary[key][0]>maxCount:
            maxKey=key
            maxCount=repairDictionary[key][0]

    return maxKey

def replacePair(nodeList,index,newNode):
    #remove the two neighbors
    del nodeList[index]
    del nodeList[index]

    nodeList.insert(index, newNode)

    return nodeList
    
def repair(adjList):
    #generate the repair dictionary
    repairDictionary=updateDictionary(adjList)
        
    #get the most common pair
    mostCommonPair=getMostCommon(repairDictionary)

    #all unique, base case
    if repairDictionary[mostCommonPair][0]==1:
        print('returning here: '+str(mostCommonPair))
        return adjList

    #create new node
    nodeKey=str(mostCommonPair[0][0])+'_'+str(mostCommonPair[1][0])
    newNode=(nodeKey, True)
    
    for occurrence in repairDictionary[mostCommonPair][1]:
        #node list where it appears
        nodeList=adjList[occurrence[0]]
        repairedNodeList=replacePair(nodeList, occurrence[1], newNode)

        #put it back
        adjList[occurrence[0]]=repairedNodeList

    #add the new node to the adjList
    adjList[newNode]=[mostCommonPair[0], mostCommonPair[1]]

    #recurssion step
    return repair(adjList)
