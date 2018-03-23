from graphs.graph import Graph


class HubAndSpoke(Graph):
    ''' add the hub and spoke implementation here '''

    def __init__(self, nodes=None):
        if nodes:
            super().__init__(nodes)
        else:
            super().__init__([])
