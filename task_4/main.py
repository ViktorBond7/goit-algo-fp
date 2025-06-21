import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "common")))
from build_tree import build_tree_from_heap, draw_tree


if __name__=="__main__":
    heap = [10, 20, 30, 40, 50, 60, 70]  # Будь-яка купа
    tree_root = build_tree_from_heap(heap) # Створення дерева
    draw_tree(tree_root)