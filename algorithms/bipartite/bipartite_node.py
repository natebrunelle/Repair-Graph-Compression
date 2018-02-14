# node class which adds coloring attributes to the nodes in the inputted graph


class bipartite_node:
    def __init__(self):
        self.attributes = []

    def vertex(self,v):
        self.attributes.append(v)

    def color(self,node_color):
        """adds a color to the attributes list"""
        self.attributes.append(node_color)

    def predecessor(self, pi):
        """adds a predecessor pi to the bipartite node"""
        self.attributes.append(pi)





