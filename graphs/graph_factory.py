''' A factory method to help with the creation of objects
of the different types of graph types. I added this to make it
easier for future development. It is not really need for the
three graph implementations we have right now. '''

import enum

from graphs.complete_graph import CompleteGraph
from graphs.graph import Graph
from graphs.hub_and_spoke_graph import HubAndSpoke


class GraphTypes(enum.Enum):
    ''' Defines an enum to avoid using strings directly and
    add more type checking '''

    complete = 1
    hub_and_spoke = 2
    generic = 3


class GraphFactory(object):
    def __init__(self, graph_type):

        # type check
        if not isinstance(graph_type, GraphTypes):
            raise "Use the GraphTypes enum to as a param"
        else:
            self.graph_type = graph_type

    def graph_factory(self):
        ''' Creates graphs of different type based on the parameter '''

        if self.graph_type.value == 1:
            return CompleteGraph([])

        if self.graph_type.value == 2:
            return HubAndSpoke([])

        if self.graph_type.value == 3:
            return Graph([])
