from graphGenerator import weaklyConnectedClusters
from compression import repair
from decompression import decompress
from utils import generateViz


def main():
    #generate graph
    # node1=(1, False)
    # node2=(2, False)
    # node3=(3, False)
    # node4=(4, False)
    # node5=(5, False)
    # node6=(6, False)
    # node7=(7, False)
    # node8=(8, False)

    # directedGraph={} #weaklyConnectedClusters(100, 30, 700)
    # directedGraph[node1]=[node5,node6,node7,node8]
    # directedGraph[node2]=[node5,node6,node7,node8]
    # directedGraph[node3]=[node5,node6,node7,node8]
    # directedGraph[node4]=[node5,node6,node7]
    # directedGraph[node5]=[]
    # directedGraph[node6]=[]
    # directedGraph[node7]=[]
    # directedGraph[node8]=[]
    # clusterSize, clusterNum, edgeNum

    directedGraph = weaklyConnectedClusters(500, 200, 700, 20)
    generateViz(directedGraph, "generated")

    genEdges = 0
    for node in directedGraph.keys():
        for connected in directedGraph[node]:
            genEdges += 1
    #print(generatedGraph)

    compressedGraph = repair(directedGraph)
    compEdges = 0

    for node in compressedGraph.keys():
        for connected in compressedGraph[node]:
            compEdges += 1


# print(compressedGraph)

    print("Gen. # of Edges: " + str(genEdges))
    print("Comp. # of Edges: " + str(compEdges))
    print("Comp ratio: " + str(compEdges / genEdges))

    generateViz(directedGraph, "generated")
    generateViz(compressedGraph, "compressed")

main()
