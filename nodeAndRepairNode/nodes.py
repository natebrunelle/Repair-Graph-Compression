# Rahul Tuladhar Nick Taylor 2/12/18

class Node:
	def __init__(self, value):
		self.value = value
		self.edges = []
		self.uid = -1

	def add_edge(self, node):
		self.edges.append(node)

class RepairNode(Node):
	def __init__(self, node1, node2, isDictNode=True, u_id):
		self.id = u_id
		self.isDictNode = isDictNode
		self.edges = [node1, node2]

