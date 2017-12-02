from graphGenerator import weaklyConnectedClusters
from compression import repair
from decompression import decompress
from utils import generateViz

def main():
    #generate graph
    generatedGraph=weaklyConnectedClusters(60, 10, 20)
    compressedGraph=repair(generatedGraph)
    generateViz(generatedGraph, "generated")
    generateViz(compressedGraph, "compressed")

main()
