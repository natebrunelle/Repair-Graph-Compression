# Rahul Tuladhar Nick Taylor 2/12/18


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.uid = -1

    def add_edge(self, node):
        if node not in self.edges:
            self.edges.append(node)
            node.add_edge(self)  # is this a good way of doing this? Rather than ...
            # node.edges.append(self)  ... adds more checking this way. Shouldn't be necessary though.
            # could also shift the reversal to Graph class. Makes more sense that way.

    def delete_edge(self, node):
        if node in self.edges:  # for should remove all instances, but could result in loop
            self.edges.remove(node)
            node.delete_edge(self)  # this will loop until all instances removed?


class RepairNode(Node):
    def __init__(self, value, node1, node2, isDictNode= True):
        self.id = -1
        self.isDictNode = isDictNode
        self.edges = [node1, node2]
