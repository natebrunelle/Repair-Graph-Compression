import unittest
import sys
import random
from algorithms.search_breadth_first.breadthFirstSearch import breadthFirstSearch, repair_breadth
from algorithms.search_depth_first.depthFirstSearch import depthFirstSearch, repair_depth
from algorithms.search_a_star.aStarSearch import aStarSearch, repair_star
from graphs.graph import Graph
from nodes.nodes import EventType, Node, RepairNode
from repair.repair import Repair, RepairPriorityQueue
import time
import csv
from unittest import TestCase

class TestSearchingAlgorithms(unittest.TestCase):
    path_set = set()
    visited_set = set()

    def check_cycle(self, vertex):
        if vertex in self.visited_set:
            return False
        self.visited_set.add(vertex)
        self.path_set.add(vertex)
        for neighbour in vertex.edges:
            if neighbour in self.path_set or self.check_cycle(neighbour):
                return True
        self.path_set.remove(vertex)
        return False


    def setUpRandomCompression(self, num_nodes):
        sys.setrecursionlimit(100000)

        nodes_list = []
        frequency_tracker = {}
        for x in range(0, num_nodes):
            num = random.randint(0, 1000)
            tempNode = Node(num)
            tempNode.edges = []
            nodes_list.append(tempNode)
            frequency_tracker[tempNode] = 0

        for n in nodes_list:
            curr_index = nodes_list.index(n)
            first_rand = random.randint(0, num_nodes-1)
            while(first_rand == curr_index):
                first_rand = random.randint(0, num_nodes - 1)
            second_rand = random.randint(0, (num_nodes-1)//4)
            while(second_rand == first_rand or second_rand == curr_index):
                second_rand = random.randint(0, (num_nodes - 1)//4)
            n.edges.append(nodes_list[first_rand])
            n.edges.append(nodes_list[second_rand])

        for n in nodes_list:
            for adj in n.edges:
                frequency_tracker[adj] += 1

        list_of_dicts = []
        current_max = max(frequency_tracker, key=frequency_tracker.get) #gets the key of the highest value in the dict frequency_tracker
        while(frequency_tracker[current_max] > 1 and current_max.value != float('inf')):
            temp_key = current_max
            list_of_dicts.append(current_max)
            if( any(self.check_cycle(v) for v in list_of_dicts) == False) :
                list_of_dicts.remove(current_max)
                del frequency_tracker[temp_key]
                current_max = max(frequency_tracker, key=frequency_tracker.get)
                continue
            if((current_max.edges[0].value == float('inf') or current_max.edges[1].value == float('inf'))):
                list_of_dicts.remove(current_max)
                del frequency_tracker[temp_key]
                current_max = max(frequency_tracker, key=frequency_tracker.get)
                print("CYCLE FOUND, skipping over")
                continue
            current_max.__class__ = RepairNode
            current_max.value = float('inf')
            del frequency_tracker[temp_key]
            current_max = max(frequency_tracker, key=frequency_tracker.get)

        str_to_ret = ""
        random_compressed_graph = Graph(nodes_list)
        str_to_ret += "Length of generated compressed graph:\n"
        str_to_ret += str((len(nodes_list))) + "\n"
        var1_repair = Repair(random_compressed_graph)
        start = time.time()
        var1 = var1_repair.decompress()
        end = time.time()
        str_to_ret += "Length of decompressed graph:\n"
        str_to_ret +=str((len(var1.list_nodes))) + "\n"
        str_to_ret += ("Time for Decompression: \n" + str(end - start) + '\n')

        return str_to_ret


    def setUpDenseGraph(self, num_nodes): #self.real_dense_graph
            sys.setrecursionlimit(100000)

            list_of_nodes = []
            list_for_compression = []

            for x in range(0, num_nodes):
                num = random.randint(0, 1000)
                tempNode = Node(num)
                tempNode.edges = []
                list_of_nodes.append(tempNode)

            num_dense_edges = 0

            for each in list_of_nodes:
                for node in list_of_nodes:
                    if each != node:
                        each.edges.append(node)
                        num_dense_edges += 1

            self.real_dense_graph = Graph(list_of_nodes)


    def setUpSparseGraph(self, num_nodes):
        sys.setrecursionlimit(100000)
        list_of_nodes_sparse = []
        self.real_node_list_sparse = []

        num_sparse_edges = 0

        for x in range(0, num_nodes):
            num = random.randint(0, 1000)
            tempNode = Node(num)
            tempNode.edges = []
            list_of_nodes_sparse.append(tempNode)

        for each in list_of_nodes_sparse:
            for node in list_of_nodes_sparse:
                x = random.randint(0, 10)
                if (len(each.edges) < 1 and each != node):
                    each.edges.append(node)
                    num_sparse_edges += 1
                elif each != node and x < 7:  # THIS manner of implementing random edges makes for optimal compression
                    each.edges.append(node)
                    num_sparse_edges += 1
                else:
                    break

        sparse_graph = Graph(list_of_nodes_sparse)
        self.sparse_graph = sparse_graph


    def setUpSparseCompressedGraph(self, num_nodes):
        list_of_nodes_sparse = []
        self.real_node_list_sparse = []

        num_sparse_edges = 0

        for x in range(0, num_nodes):
            num = random.randint(0, 1000)
            tempNode = Node(num)
            tempNode.edges = []
            list_of_nodes_sparse.append(tempNode)

        for each in list_of_nodes_sparse:
            for node in list_of_nodes_sparse:
                x = random.randint(0, 10)
                if (len(each.edges) < 1 and each != node):
                    each.edges.append(node)
                    num_sparse_edges += 1
                elif each != node and x < 7:  # THIS manner of implementing random edges makes for optimal compression
                    each.edges.append(node)
                    num_sparse_edges += 1
                else:
                    break

        sparse_graph = Graph(list_of_nodes_sparse)

        num_sparse_nodes = len(list_of_nodes_sparse)
        repair_sparse = Repair(sparse_graph)
        self.compressed_graph_sparse = repair_sparse.compress()

    def testDepthFirstSearchDense(self):
        print("NOW STARTING DENSE DFS TEST...")
        print("-----------------------------------------------------------")
        self.setUpDenseGraph(200)

        string_to_ret = ""
        dense_graph = self.real_dense_graph

        start = time.time()
        dense_normal_result = depthFirstSearch(dense_graph)
        end = time.time()
        print("Time for dense Normal DFS: \n" + str(end - start) + '\n')
        print("Test 1 Done")
        print("")

        start = time.time()
        dense_compressed_algo = repair_depth(dense_graph)
        end = time.time()
        print("Time for dense compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 2 Done")
        print("")

        dense_repair = Repair(dense_graph)

        start = time.time()
        compressed_dense = dense_repair.compress()
        end = time.time()
        print("Time for compression of dense graph:  \n" + str(end - start) + '\n')
        print("Test 3 Done")
        print("")

        start = time.time()
        dense_compressed_result = repair_depth(compressed_dense)
        end = time.time()
        print("Time for dense Compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 4 Done")
        print("")

        start = time.time()
        decompressed_dense_graph = dense_repair.decompress()
        end = time.time()
        print("Time for actual decompression of dense graph:  \n" + str(end - start) + '\n')
        print("Test 5 Done")
        print("")

        start = time.time()
        decompressed_normal_result = depthFirstSearch(decompressed_dense_graph)
        end = time.time()
        print("Time for DECOMPRESSED dense 'normal' DFS: \n" + str(end - start) + '\n')
        print("Test 6 Done")
        print("")

        start = time.time()
        decompressed_normal_result2 = repair_depth(decompressed_dense_graph)
        end = time.time()
        print("Time for DECOMPRESSED dense compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 7 Done")
        print("")

        self.assertEqual(decompressed_normal_result, decompressed_normal_result2, dense_compressed_result)
        self.assertEqual(dense_normal_result, dense_compressed_algo, dense_compressed_result)

        return string_to_ret


    def testDepthFirstSearchSparse(self):
        print("NOW STARTING SPARSE DFS TEST...")
        print("-----------------------------------------------------------")
        self.setUpSparseGraph(500)

        string_to_ret = ""
        sparse_graph = self.sparse_graph

        start = time.time()
        sparse_normal_result = depthFirstSearch(sparse_graph)
        end = time.time()
        print("Time for Sparse Normal DFS: \n" + str(end - start) + '\n')
        print("Test 1 Done")
        print("")

        start = time.time()
        sparse_compressed_algo = repair_depth(sparse_graph)
        end = time.time()
        print("Time for Sparse compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 2 Done")
        print("")

        sparse_repair = Repair(sparse_graph)

        start = time.time()
        compressed_sparse = sparse_repair.compress()
        end = time.time()
        print("Time for compression of sparse graph:  \n" + str(end - start) + '\n')
        print("Test 3 Done")
        print("")

        start = time.time()
        sparse_compressed_result = repair_depth(compressed_sparse)
        end = time.time()
        print("Time for Sparse Compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 4 Done")
        print("")

        start = time.time()
        decompressed_sparse_graph = sparse_repair.decompress()
        end = time.time()
        print("Time for actual decompression of sparse graph:  \n" + str(end - start) + '\n')
        print("Test 5 Done")
        print("")

        start = time.time()
        decompressed_normal_result = depthFirstSearch(decompressed_sparse_graph)
        end = time.time()
        print("Time for DECOMPRESSED Sparse 'normal' DFS: \n" + str(end - start) + '\n')
        print("Test 6 Done")
        print("")

        start = time.time()
        decompressed_normal_result2 = repair_depth(decompressed_sparse_graph)
        end = time.time()
        print("Time for DECOMPRESSED Sparse compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 7 Done")
        print("")

        self.assertEqual(decompressed_normal_result, decompressed_normal_result2, sparse_compressed_result)
        self.assertEqual(sparse_normal_result, sparse_compressed_algo, sparse_compressed_result)

        return string_to_ret


    def testBreadthFirstSearchDense(self):
        print("NOW STARTING DENSE BFS TEST...")
        print("-----------------------------------------------------------")
        self.setUpDenseGraph(200)

        string_to_ret = ""
        dense_graph = self.real_dense_graph

        start = time.time()
        dense_normal_result = breadthFirstSearch(dense_graph)
        end = time.time()
        print("Time for dense Normal DFS: \n" + str(end - start) + '\n')
        print("Test 1 Done")
        print("")

        start = time.time()
        dense_compressed_algo = repair_breadth(dense_graph)
        end = time.time()
        print("Time for dense compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 2 Done")
        print("")

        dense_repair = Repair(dense_graph)

        start = time.time()
        compressed_dense = dense_repair.compress()
        end = time.time()
        print("Time for compression of dense graph:  \n" + str(end - start) + '\n')
        print("Test 3 Done")
        print("")

        start = time.time()
        dense_compressed_result = repair_breadth(compressed_dense)
        end = time.time()
        print("Time for dense Compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 4 Done")
        print("")

        start = time.time()
        decompressed_dense_graph = dense_repair.decompress()
        end = time.time()
        print("Time for actual decompression of dense graph:  \n" + str(end - start) + '\n')
        print("Test 5 Done")
        print("")

        start = time.time()
        decompressed_normal_result = breadthFirstSearch(decompressed_dense_graph)
        end = time.time()
        print("Time for DECOMPRESSED dense 'normal' DFS: \n" + str(end - start) + '\n')
        print("Test 6 Done")
        print("")

        start = time.time()
        decompressed_normal_result2 = repair_breadth(decompressed_dense_graph)
        end = time.time()
        print("Time for DECOMPRESSED dense compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 7 Done")
        print("")

        self.assertEqual(decompressed_normal_result, decompressed_normal_result2, dense_compressed_result)
        self.assertEqual(dense_normal_result, dense_compressed_algo, dense_compressed_result)

        return string_to_ret


    def testBreadthFirstSearchSparse(self):
        print("NOW STARTING SPARSE BFS TEST...")
        print("-----------------------------------------------------------")
        self.setUpSparseGraph(500)

        string_to_ret = ""
        sparse_graph = self.sparse_graph

        start = time.time()
        sparse_normal_result = breadthFirstSearch(sparse_graph)
        end = time.time()
        print("Time for Sparse Normal DFS: \n" + str(end - start) + '\n')
        print("Test 1 Done")
        print("")

        start = time.time()
        sparse_compressed_algo = repair_breadth(sparse_graph)
        end = time.time()
        print("Time for Sparse compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 2 Done")
        print("")

        sparse_repair = Repair(sparse_graph)

        start = time.time()
        compressed_sparse = sparse_repair.compress()
        end = time.time()
        print("Time for compression of sparse graph:  \n" + str(end - start) + '\n')
        print("Test 3 Done")
        print("")

        start = time.time()
        sparse_compressed_result = repair_breadth(compressed_sparse)
        end = time.time()
        print("Time for Sparse Compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 4 Done")
        print("")

        start = time.time()
        decompressed_sparse_graph = sparse_repair.decompress()
        end = time.time()
        print("Time for actual decompression of sparse graph:  \n" + str(end - start) + '\n')
        print("Test 5 Done")
        print("")

        start = time.time()
        decompressed_normal_result = breadthFirstSearch(decompressed_sparse_graph)
        end = time.time()
        print("Time for DECOMPRESSED Sparse 'normal' DFS: \n" + str(end - start) + '\n')
        print("Test 6 Done")
        print("")

        start = time.time()
        decompressed_normal_result2 = repair_breadth(decompressed_sparse_graph)
        end = time.time()
        print("Time for DECOMPRESSED Sparse compression aware DFS: \n" + str(end - start) + '\n')
        print("Test 7 Done")
        print("")

        self.assertEqual(decompressed_normal_result, decompressed_normal_result2, sparse_compressed_result)
        self.assertEqual(sparse_normal_result, sparse_compressed_algo, sparse_compressed_result)

        return string_to_ret


    def testAStarSearchDense(self):
        print("NOW STARTING DENSE A STAR TEST...")
        print("-----------------------------------------------------------")
        self.setUpDenseGraph(200)

        string_to_ret = ""
        dense_graph = self.real_dense_graph

        start = time.time()
        dense_normal_result = aStarSearch(dense_graph)
        end = time.time()
        print("Time for dense Normal A Star: \n" + str(end - start) + '\n')
        print("Test 1 Done")
        print("")

        start = time.time()
        dense_compressed_algo = repair_star(dense_graph)
        end = time.time()
        print("Time for dense compression aware A Star: \n" + str(end - start) + '\n')
        print("Test 2 Done")
        print("")

        dense_repair = Repair(dense_graph)

        start = time.time()
        compressed_dense = dense_repair.compress()
        end = time.time()
        print("Time for compression of dense graph:  \n" + str(end - start) + '\n')
        print("Test 3 Done")
        print("")

        start = time.time()
        dense_compressed_result = repair_star(compressed_dense)
        end = time.time()
        print("Time for dense Compression aware A Star: \n" + str(end - start) + '\n')
        print("Test 4 Done")
        print("")

        start = time.time()
        decompressed_dense_graph = dense_repair.decompress()
        end = time.time()
        print("Time for actual decompression of dense graph:  \n" + str(end - start) + '\n')
        print("Test 5 Done")
        print("")

        start = time.time()
        decompressed_normal_result = aStarSearch(decompressed_dense_graph)
        end = time.time()
        print("Time for DECOMPRESSED dense 'normal' A Star: \n" + str(end - start) + '\n')
        print("Test 6 Done")
        print("")

        start = time.time()
        decompressed_normal_result2 = repair_star(decompressed_dense_graph)
        end = time.time()
        print("Time for DECOMPRESSED dense compression aware A Star: \n" + str(end - start) + '\n')
        print("Test 7 Done")
        print("")

        self.assertEqual(decompressed_normal_result, decompressed_normal_result2, dense_compressed_result)
        self.assertEqual(dense_normal_result, dense_compressed_algo, dense_compressed_result)

        return string_to_ret


    def testAStarSearchSparse(self):
        print("NOW STARTING SPARSE A STAR TEST...")
        print("-----------------------------------------------------------")
        self.setUpSparseGraph(500)

        string_to_ret = ""
        sparse_graph = self.sparse_graph

        start = time.time()
        sparse_normal_result = aStarSearch(sparse_graph)
        end = time.time()
        print("Time for Sparse Normal A Star: \n" + str(end - start) + '\n')
        print("Test 1 Done")
        print("")

        start = time.time()
        sparse_compressed_algo = repair_star(sparse_graph)
        end = time.time()
        print("Time for Sparse compression aware A Star: \n" + str(end - start) + '\n')
        print("Test 2 Done")
        print("")

        sparse_repair = Repair(sparse_graph)

        start = time.time()
        compressed_sparse = sparse_repair.compress()
        end = time.time()
        print("Time for compression of sparse graph:  \n" + str(end - start) + '\n')
        print("Test 3 Done")
        print("")

        start = time.time()
        sparse_compressed_result = repair_star(compressed_sparse)
        end = time.time()
        print("Time for Sparse Compression aware A Star: \n" + str(end - start) + '\n')
        print("Test 4 Done")
        print("")

        start = time.time()
        decompressed_sparse_graph = sparse_repair.decompress()
        end = time.time()
        print("Time for actual decompression of sparse graph:  \n" + str(end - start) + '\n')
        print("Test 5 Done")
        print("")

        start = time.time()
        decompressed_normal_result = aStarSearch(decompressed_sparse_graph)
        end = time.time()
        print("Time for DECOMPRESSED Sparse 'normal' A Star: \n" + str(end - start) + '\n')
        print("Test 6 Done")
        print("")

        start = time.time()
        decompressed_normal_result2 = repair_star(decompressed_sparse_graph)
        end = time.time()
        print("Time for DECOMPRESSED Sparse compression aware A Star: \n" + str(end - start) + '\n')
        print("Test 7 Done")
        print("")

        self.assertEqual(decompressed_normal_result, decompressed_normal_result2, sparse_compressed_result)
        self.assertEqual(sparse_normal_result, sparse_compressed_algo, sparse_compressed_result)

        return string_to_ret
