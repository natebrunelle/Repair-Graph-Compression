import re
from unittest import TestCase

from graphs.complete_graph import CompleteGraph
from graphs.graph import Graph
from graphs.graph_factory import (GraphFactory, GraphFactoryAlphaNumeric,
                                  GraphFactoryNoData, GraphTypes)
from graphs.hub_and_spoke_graph import HubAndSpoke


class TestFactoryMethod(TestCase):
    ''' Tests the base class's constructor '''

    def test_wrong_graph_type(self):
        ''' tests that wrong types are rejected '''

        self.assertRaises(Exception, GraphFactory, "complete")
        self.assertRaises(Exception, GraphFactory, 1)

    def test_correct_graph_type(self):
        ''' tests that the correct type is accepted '''

        complete = GraphTypes.complete
        self.assertTrue(
            isinstance(GraphFactory(complete), GraphFactory),
            "graph type enum should correctly instantiate in the base class")

    def test_graph_factory_fail(self):
        ''' unimplemented method fails '''

        complete = GraphTypes.complete

        graph_complete = GraphFactory(complete)
        self.assertRaises(Exception, graph_complete.get_graph,
                          "the base class shouldn't let you create objects")


class TestFactoryNoData(TestCase):
    ''' Tests the factory method that doesn't add data '''

    def test_complete_graph(self):
        ''' tests that complete graphs are created correctly '''

        factory = GraphFactoryNoData(GraphTypes.complete)
        graph = factory.get_graph()

        self.assertTrue(
            isinstance(graph, CompleteGraph), "Not creating the correct type")
        self.assertTrue(
            len(graph.list_nodes) == 0,
            "You shouldn't be creating nodes in this factory")

    def test_hub_and_spoke_graph(self):
        ''' tests that complete graphs are created correctly '''

        factory = GraphFactoryNoData(GraphTypes.hub_and_spoke)
        graph = factory.get_graph()

        self.assertTrue(
            isinstance(graph, HubAndSpoke), "Not creating the correct type")
        self.assertTrue(
            len(graph.list_nodes) == 0,
            "You shouldn't be creating nodes in this factory")

    def test_generic_graph(self):
        ''' tests that complete graphs are created correctly '''

        factory = GraphFactoryNoData(GraphTypes.generic)
        graph = factory.get_graph()

        self.assertTrue(
            isinstance(graph, Graph), "Not creating the correct type")
        self.assertTrue(
            len(graph.list_nodes) == 0,
            " 0 shouldn't be creating nodes in this factory")

    def test_with_nodes(self):
        ''' tests that we can create the correct number of nodes '''
        factory = GraphFactoryNoData(GraphTypes.generic, 5)
        graph = factory.get_graph()

        self.assertTrue(
            len(graph.list_nodes) == 5, "Should have created 5 nodes")


class TestGraphFactoryAlphaNumeric(TestCase):
    ''' Tests the factory that generates graphs populated with data '''

    def setUp(self):
        self.seed = 10  # random choice, pun intended

    def test_correct_data_format(self):
        ''' tests the data gen to make sure it produces the correct format'''

        # randomize, it's cool since we are using a regex
        factory = GraphFactoryAlphaNumeric(
            GraphTypes.complete, 5, random_seed=-1)

        data = factory.get_random_alpha_numeric()

        regex = r"\d{1,4}[a-zA-Z]{5}"

        matches = re.findall(regex, data)
        self.assertEqual(
            len(matches), 1, "The data is not formatted correctly")

    def test_correct_num_of_nodes(self):
        ''' Tests that we are generating the right number of nodes'''

        factory = GraphFactoryAlphaNumeric(
            GraphTypes.complete, 5, random_seed=self.seed)

        graph = factory.get_graph()

        self.assertTrue(
            len(graph.list_nodes) == 5, "Should have created 5 nodes")

    def test_each_graph_is_new(self):
        ''' tests that when randomized, each graph is new '''

        factory = GraphFactoryAlphaNumeric(
            GraphTypes.complete, 5, random_seed=self.seed)

        graph = factory.get_graph()
        graph2 = factory.get_graph()

        self.assertFalse(graph == graph2, "random graphs shouldn't be equal")
