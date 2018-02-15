# Rahul Tuladhar Nick Taylor 2/12/18


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.uid = -1

    def add_edge(self, node):
        if node not in self.edges:
            self.edges.append(node)

    def delete_edge(self, node):
        if node in self.edges:
            self.edges.remove(node)


class RepairNode(Node):
    def __init__(self, value, node1, node2, isDictNode= True):
        self.id = -1
        self.isDictNode = isDictNode
        self.edges = [node1, node2]
