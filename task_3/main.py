import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней: нескінченність для всіх, крім стартової вершини
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Мін-купа: (поточна_відстань, вершина)
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # Пропускаємо, якщо знайшли кращу відстань
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


if __name__=="__main__":
    # Створення зваженого графа
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 5), ('D', 10)],
        'C': [('A', 2), ('B', 5), ('D', 3)],
        'D': [('B', 10), ('C', 3)]
    }

    # Виклик алгоритму Дейкстри
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    # Виведення результату
    for vertex, distance in shortest_paths.items():
        print(f"Найкоротший шлях від {start_vertex} до {vertex} = {distance}")
