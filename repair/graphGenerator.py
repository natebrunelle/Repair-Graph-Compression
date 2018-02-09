import random
import string


def weaklyConnectedClusters(number_of_connections, clusterSize, clusterNum,
                            edgeNum):
    clusters = {}
    bins = clusterNum % 26

    ids = []
    for char in list(string.ascii_lowercase):
        for i in range(bins):
            ids.append(char + str(i))

            if len(ids) == clusterNum:
                break
        if len(ids) == clusterNum:
            break

    #for testing only
    #random.seed(15)

    #get all the individual clusters
    for c in range(clusterNum):
        id = ids[c]
        hub = createHub(number_of_connections, clusterSize, id)
        for node in hub.keys():
            clusters[node] = hub[node]

    for i in range(clusterNum):
        for e in range(edgeNum):
            #choose two random nodes
            cluster1 = i * clusterSize
            cluster2 = random.randint(1, clusterNum - 1)

            #get clusters
            cluster1 = list(clusters.keys())[cluster1][1]
            cluster2 = list(clusters.keys())[cluster2 * clusterSize][1]

            while (cluster1 == cluster2):
                cluster2 = random.randint(1, clusterNum - 1)
                cluster2 = list(clusters.keys())[cluster2 * clusterSize][1]

            #randomly pick nodes from the clusters
            node1 = random.randint(1, clusterSize - 1)
            node2 = random.randint(1, clusterSize - 1)

            node1 = (node1, cluster1)
            node2 = (node2, cluster2)

            while (node2 in clusters[node1]):
                node2 = random.randint(1, clusterSize - 1)
                node2 = (node2, cluster2)

            clusters[node1].append(node2)

    for node in clusters.keys():
        for t in clusters[node]:
            if t[0] == -1:
                n = clusters[node]
                del n[0]
                clusters[node] = n

    return clusters


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
