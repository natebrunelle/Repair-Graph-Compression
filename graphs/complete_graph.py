from graphs.graph import Graph


class CompleteGraph(Graph):
    ''' add the complete graph implementation here '''

    def __init__(self, nodes=None):
        if nodes:
            super().__init__(nodes)
        else:
            super().__init__([])
