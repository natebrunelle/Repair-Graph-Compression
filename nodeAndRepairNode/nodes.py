'''
A representation of a node/vertex in a graph.

A simple implementation based on adjacency list representation of graphs.
Implements the observer pattern so that nodes that have edges
connecting to them from outside of their graph can be properly deleted.
'''

import enum
import uuid
from collections import namedtuple


class EventType(enum.Enum):
    '''
    Defines event types that graphs will recieve when they
    observe nodes
    '''
    node_deleted = 1
    node_replaced = 2


Event = namedtuple("Event", ['observable', 'event_type', 'payload'])


class Node:
    def __init__(self, value, edges=None):
        self.value = value
        if edges:
            self.edges = edges
        else:
            self.edges = list()
        self.uid = uuid.uuid4().int
        self.graph_id = None
        self.observers = list()

    def add_edge(self, node):
        if node not in self.edges:
            self.edges.append(node)

    def delete_edge(self, node):
        if node in self.edges:
            self.edges.remove(node)

    def replace(self, node1, node2, repair_node):

        if node1 in self.edges and node2 in self.edges:
            index_node1 = self.edges.index(node1)
            index_node2 = self.edges.index(node2)

            if index_node1 + 1 == index_node2:

                self.delete_edge(node1)
                self.delete_edge(node2)
                self.edges.insert(index_node1, repair_node)

    def observe(self, graph):
        '''
        :param graph: a reference to the graph that wants to observe the node

        A graph can observe a node so that it can be notified when certain
        changes are applied to the node. For example, if the node is deleted
        by the graph that owns it, all other graphs should remove their
        bindings to the node as well. Another example, if the node is replace
        by a repair node, all graphs that have edges going to this node should
        update their references.
        '''

        self.observers.append(graph)

    def notify_all(self, event_type, payload=None):
        '''
        :param event_type: the type of the event that will be broadcasted

        This notifies all observers of the event that just happened.
        The notification is passed by wrapping it in an event tuple where
        we pass the event type as well as a reference to this node
        '''

        event = Event(self, event_type, payload)

        for observer in self.observers:
            observer.update(event)

    def __eq__(self, node2):
        """overrides the equals method"""

        if not isinstance(node2, Node):
            return False

        if self.graph_id == node2.graph_id or (self.graph_id is None
                                               and node2.graph_id is None):
            if self.uid == node2.uid:
                return True

        return False

    def __gt__(self, node2):
        """overrides the greater than method """

        if not isinstance(node2, Node):
            return False

        if self.graph_id:
            if self.graph_id > node2.graph_id:
                return True

            if self.graph_id < node2.graph_id:
                return False

        if self.graph_id == node2.graph_id or (self.graph_id is None
                                               and node2.graph_id is None):
            if self.uid > node2.uid:
                return True

        return False

    def __lt__(self, node2):
        """overrides the less than method"""

        if not isinstance(node2, Node):
            return False

        if self.graph_id:
            if self.graph_id < node2.graph_id:
                return True

            if self.graph_id > node2.graph_id:
                return False

        if self.graph_id == node2.graph_id or (self.graph_id is None
                                               and node2.graph_id is None):
            if node2 and self.uid < node2.uid:
                return True

        return False

    def __hash__(self):
        """Makes node objects hashable so they can be used as keys in dict """

        return hash(self.uid)

    def __str__(self):
        """overriding the str method, helps when debugging """

        return "ID: " + str(self.uid) + "\tValue: [" + str(self.value) + "]"


class RepairNode(Node):
    def __init__(self, value, node1, node2, isDictNode=True):
        self.isDictNode = isDictNode
        edges = [node1, node2]

        # init the parent class too
        super(RepairNode, self).__init__(value, edges)
