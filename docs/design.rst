.. _design:

=======
Design 
=======

Overview
^^^^^^^^^

The source code is made up of three main components:

 1. Nodes
 2. Graphs and Clusters
 3. Repair Compression 

**1. Nodes**

Nodes are the basic building blocks of everything. Different kinds of graphs are formed by connecting these nodes in different ways, repair compresses graphs and clusters by replacing nodes, and decompression works similarly. At the most basic level, a node is simply a value and a list. The list has a references to every other node this node points (for every edge beween this node and any other node). This makes it easier to represent graphs in the standard adjacency form by simply having a list of nodes. [1]_ 

In addition to the value and edges list, nodes also provide some other functionalities. These functionalities are placed in the node class, instead of in graphs, because they might enable parallelism when we need to optimize in the future (e.g. `replace`). In other cases, they simply make more sense inside nodes than  anywhere else (e.g. `add_edge`).

Each node has a unique id, `uid`, because every node must be uniquely identifiable. [2]_
Nodes also have a `graph_id` attribute. This is necessary because when we create clusters, we would like to have nodes from the same graph appear closer to each other.



**2. Graphs and Clusters**




**3. Repair Compression**


Architecture
^^^^^^^^^^^^

.. [1] Older versions of the code actually had a list of list implementation. This quickly got out of control and we ended up refactoring the codebase. 

.. [2] Previous implementations made use of the value to identify nodes. This turned out to be an unnecessary limitation (e.g. the data can't have two 5s). 






