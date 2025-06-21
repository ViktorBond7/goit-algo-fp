import uuid
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#A0A0A0"  # Базовий сірий
        self.id = str(uuid.uuid4())

# Побудова дерева з купи
def build_tree_from_heap(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = build_tree_from_heap(heap, 2 * index + 1)
    node.right = build_tree_from_heap(heap, 2 * index + 2)
    return node

# Додавання ребер для візуалізації
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, l, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, r, y - 1, layer + 1)
    return graph

# Візуалізація дерева з поточними кольорами
def draw_tree(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [tree.nodes[n]['color'] for n in tree.nodes()]
    labels = {n: tree.nodes[n]['label'] for n in tree.nodes()}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()