# node class which adds coloring attributes to the nodes in the inputted graph


class bipartite_node:
    def __init__(self, v):
        # self.attributes = []
        self.vertex = v

    # def vertex(self,v):
    #     self.attributes.append(v)

    def color(self,node_color):
        """adds a color to the attributes list"""
        self.color = node_color

    def predecessor(self, pi):
        """adds a predecessor pi to the bipartite node"""
        self.predecessor = pi

    def adj(self, nodeList):
        self.adj = nodeList




