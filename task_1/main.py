from linkedList import LinkedList
from reverse_list import reverse_list
from sort_list import sort_list

ll = LinkedList()

for val in [7, 3, 1, 9, 5, 3, 6, 2]:
    ll.insert_at_end(val)
print("Оригінальний:")
print(ll.print_list())

ll.head = sort_list(ll.head)
print("Відсортований:")
print(ll.print_list())

ll.head = reverse_list(ll.head)
print("Реверсований:")
print(ll.print_list())


import uuid
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_tree_from_heap(heap, index=0):
    if index >= len(heap):
        return None
    root = Node(heap[index])
    root.left = build_tree_from_heap(heap, 2 * index + 1)
    root.right = build_tree_from_heap(heap, 2 * index + 2)
    return root

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
