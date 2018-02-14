from nodeAndRepairNode.nodes import Node
from nodeAndRepairNode.nodes import RepairNode
import unittest


class TestNodeAndRepairNode(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.rnn = RepairNode(11, self.n1, self.n2)
        self.rrn = RepairNode(12, self.rnn, self.n3)

    def test_add_node_edge(self):
        self.n1.add_edge(self.n2)
        self.assertEqual(len(self.n1.edges), 1, "Edge not added")
        self.assertEqual(len(self.n2.edges), 1, "adj list not updated")  # both nodes should list the other node, right?

    def test_delete_node_edge(self):
        self.n1.add_edge(self.n2)
        self.n1.delete_edge(self.n2)
        self.assertEqual(len(self.n1.edges), 0, "Edge not deleted")

# def test_add_repair_node_edge():
# 	self.rnn.

# def test_delete_repair_node_edge():
# 	n1 = Node(1)
# 	n2 = Node(2)
# 	n3 = Node(3)
# 	n4 = Node(4)
# 	r1 = RepairNode(1, n1, n2)
# 	r2 = RepairNode(2, n3, r2)
# 	n4.add_edge(r2)
# 	n4.delete_edge(r2)
# 	print(len(n3.edges))
# 	assert len(n3.edges) == 0, 'Repair edge not deleted'


if __name__ == '__main__':
    unittest.main()
