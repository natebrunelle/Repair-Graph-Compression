import random
import string
from graphs.graph import Graph
from nodeAndRepairNode.nodes import Node



#We are particularly interested in: 
#number of clusters (groups of graphs), 
#the density of connection within these clusters, 
#the density of edges between the clusters,
#some form of randomization (how the connections happen etc).

def weaklyConnectedClusters(number_of_connections, graphSize, graphNum,
                            edgeNum, graphName):
    
    clusters = [ [] for a in range(graphNum) ]

    
    #clusters = {}

    for i in range(graphNum):
        for j in range(graphSize):
            self.n = Node(random.choice(string.letters))
            clusters[i].append(n)

    graphs = []
    for nodeList in clusters:
        self.g = graphName(clusters[nodeList][0], 1)
        for i in range(edgeNum):
            g.add_edge(random.choice(g.list_nodes), random.choice(nodeList))
        graphs.append(g)

    counter = 0
    connected = [ false for i in range(graphNum)]
    while(counter < graphNum):
        random1 = random.randint(0, graphNum-1)
        random2 = random.randint(0, graphNum-1)
        if(random1 != random2 && (connected[random1] == false || connected[random2] == false)):
            graphs[random1].add_edge(random.choice(graphs[random1].list_nodes), random.choice(graphs[random2].list_nodes))
            counter++
        
    while(counter < number_of_connections):
        random1 = random.randint(0, graphNum-1)
        random2 = random.randint(0, graphNum-1)
        #NEED TO CHECK IF THEY ARE ALREADY CONNECTED --> if they are connected then repeat until you find a pair that hasn't been connected && connect them
        graphs[random1].add_edge(random.choice(graphs[random1].list_nodes), random.choice(graphs[random2].list_nodes))
        counter ++
        





    
    # clusters = {}
    # bins = clusterNum % 26

    # ids = []
    # for char in list(string.ascii_lowercase):
    #     for i in range(bins):
    #         ids.append(char + str(i))

    #         if len(ids) == clusterNum:
    #             break
    #     if len(ids) == clusterNum:
    #         break

    # #for testing only
    # #random.seed(15)

    # #get all the individual clusters
    # for c in range(clusterNum):
    #     id = ids[c]
    #     hub = createHub(number_of_connections, clusterSize, id)
    #     for node in hub.keys():
    #         clusters[node] = hub[node]

    # for i in range(clusterNum):
    #     for e in range(edgeNum):
    #         #choose two random nodes
    #         cluster1 = i * clusterSize
    #         cluster2 = random.randint(1, clusterNum - 1)

    #         #get clusters
    #         cluster1 = list(clusters.keys())[cluster1][1]
    #         cluster2 = list(clusters.keys())[cluster2 * clusterSize][1]

    #         while (cluster1 == cluster2):
    #             cluster2 = random.randint(1, clusterNum - 1)
    #             cluster2 = list(clusters.keys())[cluster2 * clusterSize][1]

    #         #randomly pick nodes from the clusters
    #         node1 = random.randint(1, clusterSize - 1)
    #         node2 = random.randint(1, clusterSize - 1)

    #         node1 = (node1, cluster1)
    #         node2 = (node2, cluster2)

    #         while (node2 in clusters[node1]):
    #             node2 = random.randint(1, clusterSize - 1)
    #             node2 = (node2, cluster2)

    #         clusters[node1].append(node2)

    # for node in clusters.keys():
    #     for t in clusters[node]:
    #         if t[0] == -1:
    #             n = clusters[node]
    #             del n[0]
    #             clusters[node] = n

    # return clusters


def createHub(number_of_connections, size, clusterID):
    hub = {}
    center = (0, clusterID)
    hub[center] = []

    for node in range(1, size):
        n1 = (node, clusterID)
        hub[center].append(n1)
        hub[n1] = [(-1, clusterID)]

    for connection in range(0, number_of_connections):
        node1 = random.randint(1, size - 1)
        node2 = random.randint(1, size - 1)

        node1 = (node1, clusterID)
        node2 = (node2, clusterID)

        while node1 in hub[node2]:
            node1 = random.randint(1, size - 1)
            node1 = (node1, clusterID)
        hub[node1].append(node2)

    return hub
