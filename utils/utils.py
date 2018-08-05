'''
Helper functions that don't belong to any particular module or package.
'''


def write_graphml_file(graphml, target_path):
    '''
    Takes in a graphml representation (from a graph or a cluster)
    and writes it to the specified location as a valid XML file.
    '''
    header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\"\nxmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns\nhttp://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">"

    header += graphml
    header += "\n"
    header += '</graphml>'

    target_file = open(target_path, 'w')
    target_file.write(header)
    target_file.close()
