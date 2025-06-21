from collections import deque
import sys
import os
from colorama import Fore, Style

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "common")))
from build_tree import Node, build_tree_from_heap, add_edges, draw_tree

# Генерація градієнта кольору в HEX
def generate_gradient_colors(n, start_rgb=(0x12, 0x30, 0x60), end_rgb=(0xB0, 0xD0, 0xFF)):
    # Якщо потрібен лише один колір — повертаємо стартовий
    if n <= 1:
        r, g, b = start_rgb
        return [f"#{r:02X}{g:02X}{b:02X}"]

    sr, sg, sb = start_rgb
    er, eg, eb = end_rgb
    # передкомпонуємо різниці каналів
    dr, dg, db = er - sr, eg - sg, eb - sb

    # будуємо список через comprehension
    return [
        # інтерполяція трьох каналів і форматування в HEX
        f"#{int(sr + dr * i / (n - 1)):02X}"
        f"{int(sg + dg * i / (n - 1)):02X}"
        f"{int(sb + db * i / (n - 1)):02X}"
        for i in range(n)
    ]

def dfs(root, colors):
    # початковий стек із кореня
    stack = [root]
    i = 0

    while stack:
        # беремо останній доданий (LIFO)
        node = stack.pop()
        if not node:
            continue

        # 1) Оновлюємо колір і малюємо крок
        node.color = colors[i]
        i += 1
        draw_tree(root, title=f"DFS step {i}")

        # 2) Додаємо дітей у стек: правий першим, щоб лівий обробився раніше
        stack.append(node.right)
        stack.append(node.left)

# Обхід у ширину (BFS)
def bfs(root, colors):
    queue = deque([root])
    i = 0
    while queue:
        node = queue.popleft()
        if node:
            node.color = colors[i]
            i += 1
            draw_tree(root, title=f"BFS step {i}")
            queue.append(node.left)
            queue.append(node.right)


if __name__== "__main__":
    # === Запуск ===
    heap = [10, 20, 30, 40, 50, 60, 70]
    root = build_tree_from_heap(heap)

    # Вибір типу обходу:
    order_type = input(f"{Fore.RED} Виберіть тип обходу: dfs або bfs -> {Style.RESET_ALL}")

    # Кількість вузлів у дереві
    def count_nodes(node):
        if node is None:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)

    total_nodes = count_nodes(root)
    colors = generate_gradient_colors(total_nodes)

    # Виконати обхід з візуалізацією
    if order_type == "dfs":
        dfs(root, colors)
    elif order_type == "bfs":
        bfs(root, colors)
