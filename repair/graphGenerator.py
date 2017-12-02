import random 
import string

def weaklyConnectedClusters(clusterSize, clusterNum, edgeNum):
    clusters={}
    ids=list(string.ascii_lowercase) #todo this limits us to 26 characters fix with A1, A1...

    #for testing only
#    random.seed(15)
    
    #get all the individual clusters
    for c in range(clusterNum):
        id=ids[c]
        hub=createHub(clusterSize, id)
        for node in hub.keys():
            clusters[node]=hub[node]

    for node in clusters:
        print(str(node)+"\t"+str(clusters[node]))


    for i in range(clusterNum):
        for e in range(edgeNum):
            #choose two random nodes
            cluster1=i*clusterSize
            cluster2=random.randint(1, clusterNum+1)

            #get clusters
            cluster1=list(clusters.keys())[cluster1][1]
            cluster2=list(clusters.keys())[clusterNum*cluster2][1]

            while(cluster1==cluster2):
                cluster2=random.randint(1, clusterNum+1)
                cluster2=list(clusters.keys())[clusterNum*cluster2][1]
                
            print("Cluster 1: "+str(cluster1)+"\t Cluster 2: "+str(cluster2))

            
            #randomly pick nodes from the clusters
            node1=random.randint(1, clusterSize-1)
            node2=random.randint(1, clusterSize-1)

            
            node1=(node1, cluster1)
            node2=(node2, cluster2)
            
            while(node2 in clusters[node1]):
                node2=random.randint(1, clusterSize-1)
                node2=(node2, cluster2)

            clusters[node1].append(node2)
            print("----------------")

    for node in clusters.keys():
        for t in clusters[node]:
            if t[0] ==-1:
                n=clusters[node]
                del n[0]
                clusters[node]=n

    return clusters
        
        

def createHub(size, clusterID):
    hub={}
    center=(0, clusterID)
    hub[center]=[]
    
    for node in range(1, size):
        n1=(node, clusterID)
        hub[center].append(n1)
        hub[n1]=[(-1, clusterID)]

    return hub
    
    
