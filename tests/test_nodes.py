import unittest

from nodeAndRepairNode.nodes import Node, RepairNode


class TestNodeAndRepairNode(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(4)
        self.rnn = RepairNode(11, self.n1, self.n2)
        self.rrn = RepairNode(12, self.rnn, self.n3)

    def test_add_edge(self):
        self.n1.add_edge(self.n2)
        self.assertEqual(len(self.n1.edges), 1, "Edge not added")
        self.assertIn(self.n2, self.n1.edges,
                      "New node not found in other node's adj list")
        # both nodes should list the other node.  This functionality and test moved to graph class.
        # self.assertEqual(len(self.n2.edges), 1, "New node's adj list not updated")

    def test_duplicate_add_edge(self):
        self.n1.add_edge(self.n2)
        self.n1.add_edge(self.n2)  # n2 shouldn't end up in list twice
        self.assertEqual(
            len(self.n1.edges), 1,
            "Re-added edge, resulted in duplicate in adj list")

    def test_delete_edge(self):
        self.n1.add_edge(self.n2)
        self.n1.delete_edge(self.n2)
        self.assertEqual(self.n1.edges.count(), 0, "Edge not deleted")
        #  This functionality and test moved to graph class.
        # self.assertEqual(len(self.n2.edges), 0, "adj list not updated")

        # TODO: better assert and checking here, don't just check len

    def test_delete_nonexistent_edge(self):
        self.n1.add_edge(self.n2)
        self.n1.delete_edge(self.n3)  # should fail
        self.assertEqual(self.n1.edges, [self.n2],
                         "deleted nonexistent or wrong edge")

    def test_replace_only_pair(self):
        self.n3.add_edge(self.n1)
        self.n3.add_edge(self.n2)
        self.n3.replace(self.n1, self.n2, self.rnn)
        self.assertEqual(
            (self.rnn in self.n3.edges), True,
            "There is not only 1 node or repair_node not in edges")
        self.assertEqual(
            len(self.n3.edges), 1, "There is not 1 edge in the AL")

    def test_equal_op(self):
        ''' tests the equla operator override '''

        self.n4.uid = 4
        self.n3.uid = 4

        self.assertTrue(self.n4 == self.n3, "Equality doesn't hold")

    def test_gt_op(self):
        ''' tests the greater than method override '''

        self.n4.uid = 4
        self.n5.uid = 5

        self.assertTrue(self.n5 > self.n4, "Greater than doesn't hold")

    def test_le_op(self):
        ''' tests the less than method override '''

        self.n4.uid = 4
        self.n5.uid = 5

        self.assertTrue(self.n4 < self.n5)


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
