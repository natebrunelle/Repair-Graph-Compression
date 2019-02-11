import unittest
import sys
import random
from graphs.graph import Graph
from nodes.nodes import EventType, Node, RepairNode
from utils.utils import write_graphml_file
from repair.repair import Repair, RepairPriorityQueue
from graphs.hub_and_spoke_graph import HubAndSpoke

class GraphTestCase(unittest.TestCase):

    def setUp_DENSE(self): #for now, hard code a test based off of buckets of CP
                    #try to do this based off of 2 categories: < .5 and > .5

        compressed_size = 3
        list_of_nodes = []
        self.real_node_list = []

        for x in range(0, compressed_size*3):
            tempNode = Node(x)
            tempNode.edges = []
            print(tempNode)
            # print("node: ")
            # print(self.tempNode)
            list_of_nodes.append(tempNode)
            #print("Printing list of nodes so far: ")
            #print(list_of_nodes)
        print("size of list of nodes: ", str(len(list_of_nodes)))
        print(list_of_nodes)

        for each in list_of_nodes:
            for node in list_of_nodes:
                if each != node:
                    each.edges.append(node)

        # temp_list = []
        # for each in list_of_nodes:
        #     temp_list.append(each)


            # each.edges = temp_list
            # temp_list.append(each)

        # for node in list_of_nodes:
        #     node.edges.remove(node)

        # for each in list_of_nodes:
        #     print(each.edges)
        self.node_list = list_of_nodes
        self.graphNew = Graph(self.node_list)
        print("printing graph")
        print(self.graphNew)
        self.repair = Repair(self.graphNew)
        compressed_graph = self.repair.compress()
        print("COMPRESSED GRAPH")
        print(compressed_graph)


        #print("LIST OF NODES")
        #print(list_of_nodes)

        # self.node1 = Node(1)
        # self.node2 = Node(2)
        # self.node3 = Node(3)
        # self.node4 = Node(4)
        # self.node5 = Node(5)
        # self.node6 = Node(6)
        #
        # # setup edges, almost decided to use the add_edge method
        # self.node1.edges = [self.node2, self.node3, self.node4, self.node5, self.node6]
        # self.node2.edges = [self.node1, self.node3, self.node4, self.node5, self.node6]
        # self.node3.edges = [self.node1, self.node2, self.node4, self.node5, self.node6]
        # self.node4.edges = [self.node1, self.node2, self.node3, self.node5, self.node6]
        # self.node5.edges = [self.node1, self.node2, self.node3, self.node4, self.node6]
        # self.node6.edges = [self.node1, self.node2, self.node3, self.node4, self.node5]
        #
        # self.node_list = [
        #      self.node1, self.node2, self.node3, self.node4, self.node5, self.node6
        # ]
        #

        #
        # print("sizes: ")
        # print(sys.getsizeof(self.graphNew))
        # print(sys.getsizeof(compressed_graph))
                    # self.graph2 = Graph(self.node_list)
        # print("HELLOoo?")
        # print(self.graph2)

        #self.repair = Repair(self.graph)

    def setUp_SPARSE(self):  # for now, hard code a test based off of buckets of CP
        # try to do this based off of 2 categories: < .5 and > .5

        compressed_size = 2
        list_of_nodes_sparse = []
        self.real_node_list_sparse = []

        for x in range(0, compressed_size * 4):
            tempNode = Node(x)
            tempNode.edges = []
            # print(tempNode)

            list_of_nodes_sparse.append(tempNode)

        # print("size of list of nodes: ", str(len(list_of_nodes_sparse)))
        # print(list_of_nodes_sparse)

        for each in list_of_nodes_sparse:
            for node in list_of_nodes_sparse:
                x = random.randint(0,10)
                #print("X is: ", str(x))
                if each != node and x < 7:
                    each.edges.append(node)
                else:
                    break

        self.node_list_sparse = list_of_nodes_sparse
        self.graphNew_sparse = Graph(self.node_list_sparse)
        # print("printing graph")
        # print(self.graphNew_sparse)
        self.repair_sparse = Repair(self.graphNew_sparse)
        compressed_graph_sparse = self.repair_sparse.compress()
        # print("COMPRESSED GRAPH")
        # print(compressed_graph_sparse)

    def setUp(self):  # for now, hard code a test based off of buckets of CP
        # try to do this based off of 2 categories: < .5 and > .5
        """
        hub1 = Node(9999999999)
        self.hub_node_list = []
        number_of_spokes = 50
        for i in range(0, number_of_spokes):
            tempNode = Node(i)
            self.hub_node_list.append(tempNode)

        hub2 = self.hub_node_list[0]
        self.hub_node_list2 = []
        for i in range(0, number_of_spokes*2):
            tempNode = Node(i*2)
            self.hub_node_list2.append(tempNode)

        self.HubGraphOne = HubAndSpoke(hub1, self.hub_node_list)
        self.HubGraphTwo = HubAndSpoke(self.hub_node_list[0], self.hub_node_list2)

        print("Size of spokes on graph one: " + str(number_of_spokes))
        print("Size of spokes on graph two: " + str(number_of_spokes*2))

        self.repair_hub1 = Repair(self.HubGraphOne)
        self.repair_hub2 = Repair(self.HubGraphTwo)
        compressed_hub1 = self.repair_hub1.compress()
        compressed_hub2 = self.repair_hub2.compress()

        print("Number of nodes of hub1 compressed: " + str(len(compressed_hub1.list_nodes)))
        print("Number of nodes of hub2 compressed: " + str(len(compressed_hub2.list_nodes)))

        """
        sys.setrecursionlimit(100000)
        compressed_size = 2
        list_of_nodes = []

        for x in range(0, compressed_size * 4):
            tempNode = Node(x)
            tempNode.edges = []
            #print(tempNode)
            list_of_nodes.append(tempNode)

        # print("size of list of nodes: ", str(len(list_of_nodes)))
        # print(list_of_nodes)

        num_dense_edges = 0

        for each in list_of_nodes:
            for node in list_of_nodes:
                if each != node:
                    each.edges.append(node)
                    num_dense_edges+=1

        # for j in range(0, 800):
        #     for k in range(0, 800):
        #         if list_of_nodes[j] != list_of_nodes[k]:
        #             list_of_nodes[j].edges.append(list_of_nodes[k])
        #             num_dense_edges+=1

        self.node_list_dense = list_of_nodes

        num_dense_nodes = len(list_of_nodes)

        self.denseGraph = Graph(self.node_list_dense)
        print(self.denseGraph)
        # print("printing dense graph")
        # print(self.graphNew)
        self.repair = Repair(self.denseGraph)
        compressed_graph = self.repair.compress()
        self.compressed_dense_nodes = compressed_graph.list_nodes



        compressed_num_dense_edges = 0

        for node in compressed_graph.list_nodes:
            compressed_num_dense_edges+=(len(node.edges))


        # print("number of dense nodes and edges")
        # print(num_dense_nodes)
        # print(num_dense_edges)
        compressed_num_dense_nodes = len(compressed_graph.list_nodes)
        # print("Uncompressed number of dense nodes and edges: " + str(num_dense_nodes) + " and "+ str(num_dense_edges))
        # print("Compressed number of dense nodes and edges: " + str(compressed_num_dense_nodes) +" and "+ str(compressed_num_dense_edges))
        self.compression_ratio_of_dense_nodes = num_dense_nodes/compressed_num_dense_nodes
        self.compression_ratio_of_dense_edges = num_dense_edges/compressed_num_dense_edges
        print("Number of total nodes + edges before compression: " + str(num_dense_nodes) + " and " + str(num_dense_edges))


        print("Ratio of uncompressed/compressed dense nodes and edges: " + str(self.compression_ratio_of_dense_nodes)+ " and "+ str(self.compression_ratio_of_dense_edges))

        print("Size of COMPRESSED dense graph (num_edges+num_nodes): " + str(compressed_num_dense_edges + compressed_num_dense_nodes))
        print("After compression number of dense nodes: " + str(compressed_num_dense_nodes))
        #means that number of compressed nodes == size of compressed graph - compressed_num_nodes
        #print("Density of Dense graph: " + str((2*num_dense_edges)/(num_dense_nodes*(num_dense_nodes-1))))

        #self.density_of_compressed_dense_graph = (2*compressed_num_dense_edges)/(compressed_num_dense_edges*(compressed_num_dense_edges-1))

        list_of_nodes_sparse = []
        self.real_node_list_sparse = []

        self.num_dense_edges = num_dense_edges
        self.compressed_num_dense_edges = compressed_num_dense_edges

        num_sparse_edges = 0

        for x in range(0, compressed_size * 4):
            tempNode = Node(x)
            tempNode.edges = []
            #print(tempNode)

            list_of_nodes_sparse.append(tempNode)

        # print("size of list of nodes: ", str(len(list_of_nodes_sparse)))
        # print(list_of_nodes_sparse)

        for each in list_of_nodes_sparse:
            for node in list_of_nodes_sparse:
                x = random.randint(0, 10)
                #print("X is: ", str(x))
                if(len(each.edges) < 1 and each!=node):
                    each.edges.append(node)
                    num_sparse_edges+=1
                elif each != node and x < 7: #THIS manner of implementing random edges makes for optimal compression
                    each.edges.append(node)
                    num_sparse_edges+=1
                else:
                    break

        # for x in range(0,800):
        #     n1 = list_of_nodes_sparse[x]
        #     for y in range(0,800):
        #         n2 = list_of_nodes_sparse[y]
        #         rand = random.randint(0, 10)
        #         if(len(n1.edges) < 1 and n1 != list_of_nodes_sparse[y]):
        #             list_of_nodes_sparse[x].edges.append(list_of_nodes_sparse[y])
        #             num_sparse_edges+=1
        #         elif n1 != n2 and x < 7:
        #             list_of_nodes_sparse[x].edges.append(list_of_nodes_sparse[y])
        #             num_sparse_edges+=1
        #         else:
        #             break

        self.node_list_sparse = list_of_nodes_sparse
        self.graphNew_sparse = Graph(self.node_list_sparse)

        num_sparse_nodes = len(list_of_nodes_sparse)
        # print("printing sparse graph")
        # print(self.graphNew_sparse)
        self.repair_sparse = Repair(self.graphNew_sparse)
        compressed_graph_sparse = self.repair_sparse.compress()

        self.compressed_sparse_nodes = compressed_graph_sparse.list_nodes
        # print("Sparse COMPRESSED GRAPH")
        # print(compressed_graph_sparse)
        compressed_num_sparse_edges = 0

        for node in compressed_graph_sparse.list_nodes:
            compressed_num_sparse_edges+=(len(node.edges))
        # print("number of sparse nodes and edges")
        # print(num_sparse_nodes)
        # print(num_sparse_edges)


        compressed_num_sparse_nodes = len(compressed_graph_sparse.list_nodes)
        # print("Uncompressed number of sparse nodes and edges: " + str(num_sparse_nodes)+ " and " + str(num_sparse_edges))
        # print("Compressed number of sparse nodes and edges:  " + str(compressed_num_sparse_nodes) + " and " + str(compressed__num_sparse_edges))
        self.compression_ratio_of_sparse_nodes =num_sparse_nodes / compressed_num_sparse_nodes
        self.compression_ratio_of_sparse_edges = num_sparse_edges/compressed_num_sparse_edges
        print("")

        print("Sparse graph before compression: Number of nodes and edges: " + str(num_sparse_nodes)+ " and " + str(num_sparse_edges))
        print("Ratio of uncompressed/compressed sparse nodes and edges: : " + str( self.compression_ratio_of_sparse_nodes) + " and " + str(self.compression_ratio_of_sparse_edges))
        print("Size of COMPRESSED sparse graph (num_edges+num_nodes): " + str(compressed_num_sparse_edges+compressed_num_sparse_nodes))
        print("After compression number of sparse nodes: " + str(compressed_num_sparse_nodes))
        self.num_sparse_edges = num_sparse_edges
        self.compressed_num_sparse_edges = compressed_num_sparse_edges
        #print("Compressed sparse edges")
        #print(condensed_sparse_edges)
        #print(compressed_graph_sparse)



    def OGsetUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)
        self.n6 = Node(6)
        self.n1.edges = []
        self.n2.edges = []
        self.n3.edges = []
        self.n4.edges = []
        self.n5.edges = []
        self.n6.edges = []
        self.testList3 = [self.n1, self.n2, self.n3]
        self.testList4 = [self.n1, self.n2, self.n3, self.n4]
        self.g = Graph(self.testList3)
        print("PRINTING SELF.G")
        print(self.g)
        self.h = Graph([self.n5, self.n6])
        self.j = Graph()


    def test_number_of_edges_and_nodes(self):
        return True
    #     self.assertNotEqual(len(self.node_list_dense), len(self.compressed_dense_nodes)) # num of nodes uncondensed != num of nodes condensed
    #     self.assertNotEqual(len(self.node_list_sparse), len(self.compressed_sparse_nodes))
    #     self.assertNotEqual(self.num_dense_edges, self.compressed_num_dense_edges)
    #     self.assertNotEqual(self.num_sparse_edges, self.compressed_num_sparse_edges)
    #
    # def test_dense_ratio(self):
    #     self.assertTrue(0.4 <= self.compression_ratio_of_dense_nodes <= .5)
    #     self.assertTrue(1.6 <= self.compression_ratio_of_dense_edges <= 1.7)
    #
    # def test_sparse_ratio(self):
    #     self.assertTrue(.8 <= self.compression_ratio_of_sparse_nodes <= .9)
    #     self.assertTrue(1.0 <= self.compression_ratio_of_sparse_edges <= 1.9)
    #

    # def tearDown(self):
    #     self.g.list_nodes = self.testList3
    #     self.h.list_nodes = [self.n5, self.n6]
    #     self.n1.edges = []
    #     self.n2.edges = []
    #     self.n3.edges = []
    #     self.n4.edges = []
    #     self.n5.edges = []
    #     self.n6.edges = []
    #
    # def test_update_delete(self):
    #     self.h.add_edge(self.n5, self.n1)
    #     self.assertIn(self.n1, self.n5.edges)
    #
    #     self.g.delete_node(self.n1)
    #     self.assertNotIn(self.n1, self.g.list_nodes)
    #     self.assertNotIn(self.n1, self.n5.edges)
    #
    # def test_update_replace(self):
    #     replacement = RepairNode(-1, self.n5, self.n6)
    #     self.g = Graph([self.n1])
    #     self.h = Graph([self.n4])
    #
    #     self.g.add_edge(self.n1, self.n5)
    #     self.g.add_edge(self.n1, self.n6)
    #
    #     self.h.add_edge(self.n4, self.n5)
    #     self.h.add_edge(self.n4, self.n6)
    #
    #     self.n5.notify_all(EventType.node_replaced, [self.n6, replacement])
    #
    #     self.assertNotIn(self.n5, self.n1.edges,
    #                      "Replaced nodes shouldn't exit")
    #     self.assertNotIn(self.n5, self.n4.edges,
    #                      "Replaced nodes shouldn't exit")
    #
    #     self.assertNotIn(self.n6, self.n1.edges,
    #                      "Replaced nodes shouldn't exit")
    #     self.assertNotIn(self.n6, self.n4.edges,
    #                      "Replaced nodes shouldn't exit")
    #
    #     self.assertIn(replacement, self.n1.edges,
    #                   "Replacement node should exit")
    #     self.assertIn(replacement, self.n4.edges,
    #                   "Replacement node should exit")
    #
    # def test_add_edge(self):
    #     self.g.add_edge(self.n1, self.n2)
    #     self.assertIn(self.n2, self.n1.edges, "Adj list: edge not added")
    #     self.assertEqual(
    #         self.n1.edges.count(self.n2), 1,
    #         "Adj list: n2 should appear 1x, no duplicates")
    #     self.assertCountEqual(self.n1.edges, [self.n2],
    #                           "Adj list not exactly as expected")
    #
    # def test_add_outside_edge(self):
    #     self.assertNotIn(self.n4, self.g.list_nodes)  # n4 is outside graph
    #     self.g.add_edge(self.n1, self.n4)
    #     self.assertIn(self.n4, self.n1.edges, "Adj lists not updated")
    #     self.assertCountEqual(self.n1.edges, [self.n4],
    #                           "Adj list not exactly as expected")
    #
    # def test_duplicate_add_edge(self):
    #     # node count shouldn't change
    #     self.g.add_edge(self.n1, self.n2)  # n2 is added to n1's list
    #     self.g.add_edge(self.n1, self.n2)
    #     self.assertNotIn(self.n1,
    #                      self.n2.edges)  # n1 is not added to n2's list
    #     self.assertEqual(self.n1.edges.count(self.n2), 1)
    #     self.assertCountEqual(self.n1.edges, [self.n2],
    #                           "Adj list not exactly as expected")
    #
    # def test_edge_to_self(self):
    #     self.g.add_edge(self.n1, self.n1)
    #     self.assertNotIn(self.n1, self.n1.edges)
    #     self.assertCountEqual(self.n1.edges, [],
    #                           "Adj list not exactly as expected")
    #
    # def test_add_node(
    #         self
    # ):  # should add to list_nodes, this is diff between add_node and add_edge
    #     self.assertNotIn(self.n4, self.g.list_nodes, "n4 is already in graph")
    #     self.g.add_node(self.n4)
    #     self.assertIn(self.n4, self.g.list_nodes, "list_nodes not updated")
    #     self.assertEqual(self.g.graph_id, self.n4.graph_id,
    #                      "UUID not set to graph_id")
    #     self.assertCountEqual(self.g.list_nodes, self.testList4,
    #                           "Adj list not exactly as expected")
    #
    # def test_graph_duplicate_add_node(self):
    #     self.assertIn(self.n3, self.g.list_nodes)
    #     self.g.add_node(self.n3)
    #     self.assertEqual(self.g.list_nodes.count(self.n3), 1)
    #     self.assertCountEqual(self.g.list_nodes, self.testList3)
    #
    # def test_graph_add_node_edge(self):
    #     self.assertNotIn(self.n4, self.g.list_nodes, "n4 is already in graph")
    #     self.g.add_node(self.n4)
    #     self.g.add_edge(self.n1, self.n4)
    #     self.assertEqual(self.g.list_nodes, self.testList4)
    #     self.assertIn(self.n4, self.n1.edges)
    #
    # def test_graph_add_edge_node(self):
    #     # discovered problem - inherent unfairness to the add_edge function - see graph class
    #     self.assertNotIn(self.n4, self.g.list_nodes, "n4 is already in graph")
    #     self.g.add_edge(self.n4, self.n1)  # should add_node for n4
    #     self.assertIn(self.n1, self.n4.edges)
    #     self.assertIn(self.n4, self.g.list_nodes)
    #
    #     self.g.add_node(self.n4)  # should be prevented from adding 2x
    #     self.assertEqual(self.n4.edges.count(self.n1), 1)
    #     self.assertCountEqual(self.g.list_nodes, self.testList4)
    #
    # def test_delete_edge(self):
    #     self.assertTrue(
    #         self.n1 in self.g.list_nodes or self.n2 in self.g.list_nodes,
    #         "both parameters not in graph")
    #     self.g.add_edge(self.n1, self.n2)
    #     self.g.delete_edge(self.n1, self.n2)
    #
    #     self.assertEqual(
    #         len(self.g.list_nodes), 3, "Node_count for graph incorrect")
    #     self.assertEqual(self.g.list_nodes, self.testList3,
    #                      "Graph modified by delete_edge")
    #     # an edge, but not a node deleted, n2 still in list_nodes and the graph
    #     self.assertNotIn(
    #         self.n2, self.n1.edges,
    #         "All instances not removed from adj list, edge(s) not deleted")
    #
    # # TODO: add tests for where second param for delete_edge() outside graph
    #
    # def test_delete_outside_edge(self):
    #     self.assertNotIn(self.n4, self.g.list_nodes,
    #                      "n4 is already in graph, TESTS ARE STUPID")
    #     self.assertNotIn(self.n5, self.g.list_nodes)
    #     self.assertFalse(self.n5 in self.g.list_nodes
    #                      or self.n4 in self.g.list_nodes)
    #     self.h.add_edge(self.n4, self.n5)
    #     with self.assertRaises(ValueError):
    #         self.g.delete_edge(self.n4, self.n5)
    #
    # def test_delete_node(self):
    #     self.assertIn(self.n1, self.g.list_nodes,
    #                   "n1 is not part of this graph to be removed")
    #     self.assertNotIn(self.n2, self.n1.edges,
    #                      "n2 is already in n1.edges")  # since this is true...
    #     self.g.add_edge(self.n1,
    #                     self.n2)  # THIS NEEDS TO BE FULLY TESTED ELSEWHERE
    #     self.g.delete_node(self.n1)  # ...this is already true
    #     self.assertNotIn(self.n1, self.g.list_nodes,
    #                      "Node not deleted")  # n1 no longer listed in graph
    #     self.assertIn(self.n2, self.g.list_nodes, "Wrong node deleted")
    #     self.assertNotIn(self.n1, self.n2.edges,
    #                      "Found outside reference to deleted node")
    #     self.assertEqual(self.n1.edges, [],
    #                      "Node's adj list not cleared")  # n1 has no adj nodes
    #
    # def delete_nonexistent_edge(self):
    #     # test_delete_nonexistent_edge(self):
    #     self.assertNotIn(self.n4,
    #                      self.g.list_nodes)  # can delete edges btwn graphs
    #     self.assertIn(self.n1,
    #                   self.g.list_nodes)  # one node must be in the graph
    #     self.assertNotIn(self.n4, self.n1.edges)
    #     self.g.delete_edge(self.n1,
    #                        self.n4)  # n4 attempted removed from n1's list
    #     self.assertNotIn(self.n4, self.n1.edges)
    #     with self.assertRaises(ValueError):
    #         # self.n1.edges.remove(self.n4) # test passes with this, should be equivalent to line below
    #         # ValueError somehow suppressed and not passed up through classes?
    #         self.g.delete_edge(self.n1,
    #                            self.n4)  # n4 attempted removed from n1's list
    #
    # def test_delete_nonexistent_node(self):
    #     self.assertNotIn(self.n4, self.g.list_nodes)
    #     with self.assertRaises(ValueError):
    #         self.g.delete_node(self.n4)
    #
    # def test_delete_outside_node(self):
    #     self.assertNotIn(self.n4, self.h.list_nodes,
    #                      "n4 is already in graph, TESTS ARE STUPID")
    #     self.h.add_edge(self.n5, self.n4)  # 1st param must be in graph
    #     self.assertNotIn(self.n4, self.h.list_nodes)
    #     with self.assertRaises(ValueError):
    #         self.g.delete_node(self.n4)
    #     # this test fails when use graph g b/c n4 is in g, somehow, other tests corrupting g?
    #
    # TODO: also test deleting in various order
    #
    # def test_eq_wrong_num_nodes(self):
    #     """Tests equals method override with graphs
    #     that don't have equal number of nodes"""
    #
    #     second_graph = Graph([self.n1, self.n2])
    #
    #     self.assertTrue((second_graph != self.g),
    #                     "Graphs with missing nodes shouldn't be equal")
    #
    # def test_eq_wrong_ids(self):
    #     """Tests the equals method with graphs that have the same
    #     nodes, in the same places, but wrong ids"""
    #
    #     node1 = Node(1)
    #     node2 = Node(2)
    #     node3 = Node(3)
    #
    #     second_graph = Graph([node1, node2, node3])
    #     self.assertTrue((self.g != second_graph),
    #                     "Graphs with wrong ids shouldn't be considered equal")
    #
    # def test_eq_wrong_positions(self):
    #     """Tests the equals method with graphs that have the
    #     same nodes but in different positions """
    #
    #     second_graph = Graph([self.n2, self.n3, self.n1])
    #
    #     self.assertTrue(
    #         (self.g != second_graph),
    #         "Graphs with nodes in d/f positions shouldn't be considered equal")
    #
    # def test_eq_identical(self):
    #     """Happy path: tests the same exact graphs are considered equal"""
    #
    #     self.assertEqual(self.g, self.g, "same graphs should be equal")
    #
    # def test_graphml_no_nodes(self):
    #     empty_graph = Graph()
    #     expected = "<graph id=\"{}\" edgedefault=\"directed\">\n".format(
    #         empty_graph.graph_id)
    #     expected += "</graph>"
    #     actual = empty_graph.generate_graphml_format()
    #
    #     self.assertEqual(expected, actual, "Incorrect graphml format")
    #
    # def test_graphml_nodes(self):
    #     expected = "<graph id=\"{}\" edgedefault=\"directed\">\n".format(
    #         self.g.graph_id)
    #     expected += self.n1.generate_graphml_format()
    #     expected += self.n2.generate_graphml_format()
    #     expected += self.n3.generate_graphml_format()
    #
    #     expected += "</graph>"
    #     actual = self.g.generate_graphml_format()
    #
    #     self.assertEqual(expected, actual, "Incorrect graphml format")
    #
    # def test_graphml_nodes_edges(self):
    #     self.n1.add_edge(self.n2)
    #     self.n1.add_edge(self.n3)
    #
    #     expected = "<graph id=\"{}\" edgedefault=\"directed\">\n".format(
    #         self.g.graph_id)
    #     expected += self.n1.generate_graphml_format()
    #     expected += self.n2.generate_graphml_format()
    #     expected += self.n3.generate_graphml_format()
    #
    #     expected += "</graph>"
    #     actual = self.g.generate_graphml_format()
    #
    #     self.assertEqual(expected, actual, "Incorrect graphml format")


if __name__ == '__main__':
    unittest.main()
