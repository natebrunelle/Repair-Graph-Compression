import unittest
from unittest import TestCase

from ddt import data, ddt, idata

from repair.compression import *


def get_dictionary_objects():
    ''' Creates objects with defaults and injection '''
    new_queue_dict = CompressionDictionary()
    injected_dict = CompressionDictionary(None)

    return [new_queue_dict, injected_dict]


@ddt
class TestCompressionDictionary(TestCase):
    ''' Test class for the compression dictionary class '''

    def setUp(self):
        pass

    @idata(get_dictionary_objects())
    def test_is_empty(self, dictionary_obj):
        ''' simple test for empty '''
        self.fail("No test")

    def test_most_common(self):
        ''' most common with no ties '''
        self.fail("No test")

    def test_most_common_duplicates(self):
        ''' most common when there are ties'''
        self.fail("No test")

    def test_most_common_empty(self):
        ''' most common when there no nodes '''
        self.fail("No test")

    def test_add_new_pair_first(self):
        ''' adding a new pair '''
        self.fail("No test")

    def test_add_new_pair_duplicate(self):
        ''' that duplicate's freq is incremented'''
        self.fail("No test")


class TestRepair(TestCase):
    ''' Test class for the repair class '''

    def setUp(self):
        pass

    def test_update_dictionary_empty_graph(self):
        ''' update dic with an empty graph '''
        self.fail("No test")

    def test_update_dictionary_once(self):
        ''' update dictionary where the pair shows up only once in the graph '''
        self.fail("No test")

    def test_update_dictionary_multiple(self):
        ''' update where a pair shows up multiple times in the graph '''
        self.fail("No test")

    def test_compress_single_run(self):
        ''' Compression that only requires a single run through the graph '''
        self.fail("No test")

    def test_compress_mutliple_runs(self):
        ''' compression that requires multiple runs through the graph'''
        self.fail("No test")
