import unittest
import sys
import random
from algorithms.bipartite.bipartite import normal_bipartite, compression_aware_bipartite, armans_algo
from algorithms.top_sort.topologicalSort import topSort, repair_topological
from graphs.graph import Graph
from nodes.nodes import EventType, Node, RepairNode
from repair.repair import Repair, RepairPriorityQueue
import time
import csv
from unittest import TestCase



class TestTopologicalSort(unittest.TestCase):
    def setUpCompleteBipartite(self, num_nodes):
        sys.setrecursionlimit(100000)

        red_nodes = []
        blue_nodes = []


        for x in range(0, num_nodes):
            num = random.randint(0, 1000)
            tempNode = Node(num)
            tempNode.edges = []
            red_nodes.append(tempNode)

            num2 = random.randint(0, 1000)
            tempNode2 = Node(num2)
            tempNode2.edges = []
            blue_nodes.append(tempNode2)

        for red in red_nodes:
            for blue in blue_nodes:
                red.edges.append(blue)

        for blue in blue_nodes:
            for red in red_nodes:
                blue.edges.append(red)

        list_of_nodes = blue_nodes + red_nodes

        self.complete_bipartite = Graph(list_of_nodes)



    def setUpDenseGraph(self, num_nodes): #self.real_dense_graph
            sys.setrecursionlimit(100000)

            list_of_nodes = []
            list_for_compression = []

            for x in range(0, num_nodes):
                num = random.randint(0, 1000)
                tempNode = Node(num)
                tempNode.edges = []
                # print(tempNode)
                list_of_nodes.append(tempNode)


            # print("size of list of nodes: ", str(len(list_of_nodes)))
            # print(list_of_nodes)

            num_dense_edges = 0

            for each in list_of_nodes:
                for node in list_of_nodes:
                    if each != node:
                        each.edges.append(node)
                        num_dense_edges += 1

            self.real_dense_graph = Graph(list_of_nodes)
            #print(self.real_dense_graph)

            # self.repair = Repair(Graph(list_for_compression))
            # self.compressed_dense_graph = self.repair.compress()

            #print(self.compressed_dense_graph)
            # self.repaired_dense = Repair(self.real_dense_graph)
            # self.real_compressed_graph = self.repaired_dense.compress()

            #print(self.real_compressed_graph)




    def setUpSparseGraph(self, num_nodes):
        sys.setrecursionlimit(100000)
        list_of_nodes_sparse = []
        self.real_node_list_sparse = []

        num_sparse_edges = 0

        for x in range(0, num_nodes):
            num = random.randint(0, 1000)
            tempNode = Node(num)
            tempNode.edges = []
            # print(tempNode)
            list_of_nodes_sparse.append(tempNode)


        for each in list_of_nodes_sparse:
            for node in list_of_nodes_sparse:
                x = random.randint(0, 10)
                # print("X is: ", str(x))
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

        # repaired_sparse_graph = Repair(sparse_graph)
        # compressed_sparse_graph = repaired_sparse_graph.compress()
        # self.compressed_sparse = compressed_sparse_graph

        # num_sparse_nodes = len(list_of_nodes_sparse)
        # print("printing sparse graph")
        # print(self.graphNew_sparse)
        # self.repair_sparse = Repair(self.graphNew_sparse)
        # self.compressed_graph_sparse = self.repair_sparse.compress()

    def setUpSparseCompressedGraph(self, num_nodes):
        list_of_nodes_sparse = []
        self.real_node_list_sparse = []


        num_sparse_edges = 0

        for x in range(0, num_nodes):
            num = random.randint(0, 1000)
            tempNode = Node(num)
            tempNode.edges = []
            # print(tempNode)
            list_of_nodes_sparse.append(tempNode)


        for each in list_of_nodes_sparse:
            for node in list_of_nodes_sparse:
                x = random.randint(0, 10)
                # print("X is: ", str(x))
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
        # print("printing sparse graph")
        # print(self.graphNew_sparse)
        repair_sparse = Repair(sparse_graph)
        self.compressed_graph_sparse = repair_sparse.compress()



    def testTopologicalSorts(self): #tests topsort algorithm, both normal and compression aware on dense graphs (normal and compressed)

        # self.setUpDenseGraph(800)
        #
        # ret_str = ""
        # dense_graph = self.real_dense_graph
        # # ret_str += (dense_graph)
        # # ret_str += ("Topsort Dense Graph: ")
        # start = time.time()
        # dense_normal_result = topSort(dense_graph)
        # end = time.time()
        # ret_str += ("Time for Dense Normal topsort: \n" + str(end - start) + '\n')
        # ret_str += ("")
        #
        # start = time.time()
        # compressed_algo = repair_topological(dense_graph)
        # end = time.time()
        # ret_str += ("Time for normal graph using compression aware topsort: \n" + str(end - start) + '\n')
        # ret_str += ("")
        # # ret_str += ("Dense normal topsort result:\n", dense_normal_result)
        #
        #
        # # ret_str += ("Topsort compressed: ")
        # dense_repair = Repair(dense_graph)
        # start = time.time()
        # compressed_dense = dense_repair.compress()
        # end = time.time()
        # ret_str += ("Time for compression of dense graph: \n" + str(end - start) + '\n')
        #
        # start = time.time()
        # # ret_str += (compressed_dense)
        # dense_compressed_result = repair_topological(compressed_dense)
        # end = time.time()
        # ret_str += ("Time for compressed graph ran in compression aware topsort:\n " + str(end - start) + '\n')
        # ret_str += ("")
        # # ret_str += ("Dense compression aware topsort result:\n", dense_compressed_result)
        #
        # start = time.time()
        # decompressed_dense = dense_repair.decompress()
        # end = time.time()
        # ret_str += ("Time for actual decompression of dense graph:  \n" + str(end - start) + '\n')
        #
        # start = time.time()
        # dense_decompressed_result2 = topSort(decompressed_dense)
        # end = time.time()
        # ret_str += ("Time for Decompressed dense graph ran in normal topsort:\n " + str(end - start) + '\n')
        # ret_str += ("")
        #
        # start = time.time()
        # decompressed_dense = dense_repair.decompress()
        # end = time.time()
        # ret_str += ("Time for actual decompression of dense graph:  \n" + str(end - start) + '\n')
        #
        # start = time.time()
        # dense_decompressed_compression_aware = repair_topological(decompressed_dense)
        # end = time.time()
        # ret_str += ("Time for Decompressed dense graph ran in compression aware topsort:\n " + str(end - start) + '\n')
        # ret_str += ("")
        #
        # ret_str += ("------------------------------------------")
        # return ret_str

        # dense_graph = self.real_dense_graph
        # # print(dense_graph)
        # # print("Topsort Dense Graph: ")
        # start = time.time()
        # dense_normal_result = topSort(dense_graph)
        # end = time.time()
        # print("Time for Dense Normal topsort: \n" + str(end - start))
        # print("")
        #
        # start = time.time()
        # compressed_algo = repair_topological(dense_graph)
        # end = time.time()
        # print("Time for normal graph using compression aware topsort: \n" + str(end - start))
        # print("")
        # # print("Dense normal topsort result:\n", dense_normal_result)
        #
        #
        # # print("Topsort compressed: ")
        # dense_repair = Repair(dense_graph)
        # start = time.time()
        # compressed_dense = dense_repair.compress()
        # end = time.time()
        # print("Time for compression of dense graph: \n" + str(end - start))
        #
        # start = time.time()
        # # print(compressed_dense)
        # dense_compressed_result = repair_topological(compressed_dense)
        # end = time.time()
        # print("Time for compressed graph ran in compression aware topsort:\n " + str(end - start))
        # print("")
        # # print("Dense compression aware topsort result:\n", dense_compressed_result)
        #
        # start = time.time()
        # decompressed_dense = dense_repair.decompress()
        # end = time.time()
        # print("Time for actual decompression of dense graph:  \n" + str(end - start))
        #
        # start = time.time()
        # dense_decompressed_result2 = topSort(decompressed_dense)
        # end = time.time()
        # print("Time for Decompressed dense graph ran in normal topsort:\n " + str(end - start))
        # print("")
        #
        # start = time.time()
        # decompressed_dense = dense_repair.decompress()
        # end = time.time()
        # print("Time for actual decompression of dense graph:  \n" + str(end - start))
        #
        # start = time.time()
        # dense_decompressed_compression_aware = repair_topological(decompressed_dense)
        # end = time.time()
        # print("Time for Decompressed dense graph ran in compression aware topsort:\n " + str(end - start))
        # print("")
        #
        # print("------------------------------------------")

        self.setUpSparseGraph(500)

        string_to_ret = ""
        sparse_graph = self.sparse_graph
        # string_to_ret += (sparse_graph)
        start = time.time()
        sparse_normal_result = topSort(sparse_graph)
        end = time.time()
        string_to_ret += ("Time for Sparse Normal topsort: \n" + str(end - start) + '\n')
        string_to_ret += ("")

        start = time.time()
        sparse_compressed_algo = repair_topological(sparse_graph)
        end = time.time()
        string_to_ret += ("Time for Sparse compression aware topsort: \n" + str(end - start) + '\n')
        string_to_ret += ("")
        # string_to_ret += ("Sparse normal topsort result:\n", sparse_normal_result)


        sparse_repair = Repair(sparse_graph)

        start = time.time()
        compressed_sparse = sparse_repair.compress()
        end = time.time()
        string_to_ret += ("Time for compression of sparse graph:  \n" + str(end - start) + '\n')

        start = time.time()
        sparse_compressed_result = repair_topological(compressed_sparse)
        end = time.time()
        string_to_ret += ("Time for Sparse Compression aware topsort: \n" + str(end - start) + '\n')
        string_to_ret += ("")

        # string_to_ret += ("Sparse compression aware topsort result:\n", sparse_compressed_result)

        start = time.time()
        decompressed_sparse_graph = sparse_repair.decompress()
        end = time.time()
        string_to_ret += ("Time for actual decompression of sparse graph:  \n" + str(end - start) + '\n')

        start = time.time()
        decompressed_normal_result = topSort(decompressed_sparse_graph)
        end = time.time()
        string_to_ret += ("Time for DECOMPRESSED Sparse 'normal' topsort: \n" + str(end - start) + '\n')
        string_to_ret += ("")

        start = time.time()
        decompressed_sparse_graph = sparse_repair.decompress()
        end = time.time()
        string_to_ret += ("Time for actual decompression of sparse graph:  \n" + str(end - start) + '\n')

        start = time.time()
        decompressed_normal_result2 = repair_topological(decompressed_sparse_graph)
        end = time.time()
        string_to_ret += ("Time for DECOMPRESSED Sparse compression aware topsort: \n" + str(end - start) + '\n')
        string_to_ret += ("")

        return string_to_ret
        # sparse_graph = self.sparse_graph
        # # print(sparse_graph)
        # start = time.time()
        # sparse_normal_result = topSort(sparse_graph)
        # end = time.time()
        # print("Time for Sparse Normal topsort: \n" + str(end - start))
        # print("")
        #
        # start = time.time()
        # sparse_compressed_algo = repair_topological(sparse_graph)
        # end = time.time()
        # print("Time for Sparse compression aware topsort: \n" + str(end - start))
        # print("")
        # # print("Sparse normal topsort result:\n", sparse_normal_result)
        #
        #
        # sparse_repair = Repair(sparse_graph)
        #
        #
        # start = time.time()
        # compressed_sparse = sparse_repair.compress()
        # end = time.time()
        # print("Time for compression of sparse graph:  \n" + str(end - start))
        #
        # start = time.time()
        # sparse_compressed_result = repair_topological(compressed_sparse)
        # end = time.time()
        # print("Time for Sparse Compression aware topsort: \n" + str(end - start))
        # print("")
        #
        # # print("Sparse compression aware topsort result:\n", sparse_compressed_result)
        #
        # start = time.time()
        # decompressed_sparse_graph = sparse_repair.decompress()
        # end = time.time()
        # print("Time for actual decompression of sparse graph:  \n" + str(end - start))
        #
        # start = time.time()
        # decompressed_normal_result = topSort(decompressed_sparse_graph)
        # end = time.time()
        # print("Time for DECOMPRESSED Sparse 'normal' topsort: \n" + str(end - start))
        # print("")
        #
        # start = time.time()
        # decompressed_sparse_graph = sparse_repair.decompress()
        # end = time.time()
        # print("Time for actual decompression of sparse graph:  \n" + str(end - start))
        #
        # start = time.time()
        # decompressed_normal_result2 = repair_topological(decompressed_sparse_graph)
        # end = time.time()
        # print("Time for DECOMPRESSED Sparse compression aware topsort: \n" + str(end - start))
        # print("")


        self.assertEqual(decompressed_normal_result, decompressed_normal_result2, sparse_compressed_result)
        self.assertEqual(sparse_compressed_algo, sparse_normal_result )
        self.assertEqual(dense_normal_result, compressed_algo, dense_compressed_result)
        self.assertEqual(dense_decompressed_result2, dense_decompressed_compression_aware)



    def testBipartiteSort(self):
        return
        self.setUpDenseGraph(400)

        dense_graph = self.real_dense_graph
        start = time.time()
        #dense_normal_result = normal_bipartite(dense_graph)
        compressed_algo = compression_aware_bipartite(dense_graph)
        end = time.time()
        print("Time for Dense Normal Bipartite: \n" + str(end - start))
        #print("Results from Dense normal bipartite: ", dense_normal_result)
        print("Results from compression aware normal bipartite: ", compressed_algo)

        #print("Bipartite compressed: ")
        dense_repair = Repair(dense_graph)
        start = time.time()
        compressed_dense = dense_repair.compress()
        end = time.time()
        print("Time for compression of dense graph:  \n" + str(end - start))

        start = time.time()
        # print(compressed_dense)
        dense_compressed_result = compression_aware_bipartite(compressed_dense)
        end = time.time()
        print("Time for dense compression aware Bipartite: \n" + str(end - start))
        # print("Results from dense compression aware bipartite:", "poop")

        print("Results from dense compression aware bipartite:", dense_compressed_result)


        #self.assertEqual(dense_normal_result, dense_compressed_result)
        self.assertEqual(compressed_algo, dense_compressed_result)

        print("")
        self.setUpSparseGraph(400)
        sparse_graph = self.sparse_graph
        # print(sparse_graph)
        start = time.time()
        #sparse_normal_result = normal_bipartite(sparse_graph)
        sparse_compressed_algo = compression_aware_bipartite(sparse_graph)

        end = time.time()
        print("Time for Sparse Normal bipartite: \n" + str(end - start))
        #print("Results from Sparse normal bipartite:", sparse_normal_result)
        print("Results from sparse compression aware normal bipartite:", sparse_compressed_algo)

        sparse_repair = Repair(sparse_graph)
        start = time.time()
        compressed_sparse = sparse_repair.compress()
        end = time.time()
        print("Time for compression of sparse graph:  \n" + str(end - start))

        start = time.time()
        sparse_compressed_result = compression_aware_bipartite(compressed_sparse)
        end = time.time()
        print("Time for Sparse Compression aware bipartite: \n" + str(end - start))
        print("Sparse compression aware bipartite result:", sparse_compressed_result)

        # start = time.time()
        # decompressed_sparse_graph = sparse_repair.decompress()
        # decompressed_normal_result = normal_bipartite(decompressed_sparse_graph)
        # end = time.time()
        # print("Time for DECOMPRESSED Sparse normal bippartite: \n" + str(end - start))
        # print("DECOMPRESSED sparse 'normal' bipartite result: ", decompressed_normal_result)

        print("")
        # self.assertEqual(sparse_normal_result, sparse_compressed_result)





    def testCompleteBipartite(self):
        return
        self.setUpCompleteBipartite(50)
        complete_bipartite = self.complete_bipartite

        start = time.time()
        ans2 = normal_bipartite(complete_bipartite)
        end = time.time()
        print("Time for perfect normal bippartite algorithm: \n" + str(end - start))
        # print("Results from complete bipartite:", complete_bipartite_result)
        print("Result for perfect normal bippartite algorithm: ", ans2)
        print("")


        start = time.time()
        result = armans_algo(complete_bipartite)
        end = time.time()
        print("Time for normal bippartite run using compression aware algorithm: \n" + str(end - start))
        # print("Results from complete bipartite:", complete_bipartite_result)
        print("Result for normal bippartite run using compression aware algorithm: ", result)
        print("")



        # print("Printing graph: ")
        # print(complete_bipartite)

        complete_bipartite_repair = Repair(complete_bipartite)


        start = time.time()
        compressed_graph = complete_bipartite_repair.compress()
        end = time.time()
        print("Time for actual compression of complete bipartite: \n" + str(end - start))

        start = time.time()
        # compressed_complete_bipartite_result = compression_aware_bipartite(compressed_graph)
        armans_compressed_complete_bipartite_result = armans_algo(compressed_graph)
        end = time.time()

        # print("printing compressed graph: ")
        # print(compressed_graph)


        print("Time for compressed graph ran in compression aware algorithm: \n" + str(end - start))
        # print("Results from complete bipartite compressed", compressed_complete_bipartite_result)
        print("Result for compressed graph ran using compression aware algorithm: ", armans_compressed_complete_bipartite_result)
        print("")

        start = time.time()
        decompressed_compressed_perfect_bipartite = complete_bipartite_repair.decompress()
        end = time.time()
        print("Time for actual decompression of complete bipartite graph: \n" + str(end - start))

        start = time.time()
        decompressed_bipartite_results = normal_bipartite(decompressed_compressed_perfect_bipartite)
        end = time.time()


        # print("printing decompressed graph: ")
        # print(decompressed_compressed_perfect_bipartite)


        print("Time for DECOMPRESSED graph ran in normal algorithm: \n" + str(end - start))
        print("Results from decompressed graph ran in normal algorithm:", decompressed_bipartite_results)
        print("")




        start = time.time()
        decompressed_compressed_perfect_bipartite = complete_bipartite_repair.decompress()
        end = time.time()
        print("Time for actual decompression of complete bipartite graph: \n" + str(end - start))
        start = time.time()
        decompressed_bipartite_results2 = armans_algo(decompressed_compressed_perfect_bipartite)
        end = time.time()


        # print("printing decompressed graph: ")
        # print(decompressed_compressed_perfect_bipartite)


        print("Time for DECOMPRESSED graph ran using compression aware algorithm: \n" + str(end - start))
        print("Results from decompressed graph ran using compression aware algorithm", decompressed_bipartite_results2)

