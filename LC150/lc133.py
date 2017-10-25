r"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

Nodes are labeled uniquely.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""


class Node(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def clone(node, pairs):
    if not node:
        return None

    label = node.label
    if label in pairs:
        return pairs[label]

    new_node = Node(label)
    pairs[label] = new_node

    for neighbor in node.neighbors:
        clone_neighbor = clone(neighbor, pairs)
        new_node.neighbors.append(clone_neighbor)

    return new_node


def clone_graph(node):
    pairs = {}
    return clone(node, pairs)
