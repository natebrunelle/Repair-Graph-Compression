# Rahul Tuladhar Nick Taylor 2/12/18
import uuid


class Node:

    def __init__(self, value):
        self.value = value
        self.edges = []  # TODO: NEW POLICY/clarification: as of 3/2 we have declared .edges holds outgoing edges,
                            # or a list of outgoing nodes
        self.uid = uuid.uuid4()

    def add_edge(self, node):
        if node not in self.edges:
            self.edges.append(node)

    def delete_edge(self, node):
        if node in self.edges:
            self.edges.remove(node)

    def replace(self, node1, node2, repairNode):
        if node1 in repairNode.edges and node2 in repairNode.edges:
            index_node1 = self.edges.index(node1)
            index_node2 = self.edges.index(node2)
            if index_node1+1 == index_node2:
                
                self.delete_edge(node1)
                self.delete_edge(node2)
                self.edges.insert(index_node1, repairNode)

    def __eq__(self, node2):
        if node2:
            return self.value == node2.value

    # TODO overwrite python operator


class RepairNode(Node):

    def __init__(self, value, node1, node2, isDictNode= True):
        self.id = -1
        self.isDictNode = isDictNode
        self.edges = [node1, node2]

