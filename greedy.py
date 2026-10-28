graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 3,
    'F': 2,
    'G': 1,
    'H': 0
}

def greedy_best_first(start, goal):
    open_list = [(heuristic[start], [start])]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: x[0])
        h, path = open_list.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                open_list.append(
                    (heuristic[neighbor], path + [neighbor])
                )

    return None

path = greedy_best_first('A', 'H')

if path:
    print("Path found:", " -> ".join(path))
else:
    print("Path not found")