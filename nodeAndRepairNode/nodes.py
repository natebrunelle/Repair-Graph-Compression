# Rahul Tuladhar Nick Taylor 2/12/18
import uuid


class Node:
    def __init__(self, value, edges=list):
        self.value = value
        self.edges = edges
        self.uid = uuid.uuid4()

    def add_edge(self, node):
        if node not in self.edges:
            self.edges.append(node)

    def delete_edge(self, node):
        if node in self.edges:
            self.edges.remove(node)

    def replace(self, node1, node2, repairNode):
        print("Node 1: " + str(node1) + "\tNode 2:" + str(node2))
        print("----node before delete----")
        for node in self.edges:
            print(node)

        if node1 in self.edges and node2 in self.edges:
            index_node1 = self.edges.index(node1)
            index_node2 = self.edges.index(node2)
            print("got the index")
            if index_node1 + 1 == index_node2:

                self.delete_edge(node1)
                self.delete_edge(node2)
                self.edges.insert(index_node1, repairNode)

        print("----node after delete-----")
        for node in self.edges:
            print(node)

    def __eq__(self, node2):
        ''' overrides the equals method '''

        if not isinstance(node2, Node):
            return False

        if self.uid == node2.uid:
            return True

        return False

    def __gt__(self, node2):
        ''' overrides the greater than method '''

        if not isinstance(node2, Node):
            return False

        if self.uid > node2.uid:
            return True

        return False

    def __lt__(self, node2):
        ''' overrides the less than method '''

        if not isinstance(node2, Node):
            return False

        if node2 and self.uid < node2.uid:
            return True

        return False

    def __hash__(self):
        ''' Makes node objects hashable so they can be used as keys in dict '''

        return hash((self.uid))

    def __str__(self):
        ''' overriding the str method, helps when debugging '''

        return "ID: " + str(self.uid.int) + "\tValue: [" + str(
            self.value) + "]"


class RepairNode(Node):
    def __init__(self, value, node1, node2, isDictNode=True):
        self.isDictNode = isDictNode
        edges = [node1, node2]

        # init the parent class too
        super(RepairNode, self).__init__(value, edges)
