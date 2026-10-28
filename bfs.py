from collections import deque

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E', 'F', 'G'],
    'D': ['A', 'E'],
    'E': ['A', 'B', 'C', 'D', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['C', 'F']
}

def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None

path = bfs('A', 'G')

if path:
    print("Path found:", " -> ".join(path))
else:
    print("Path not found")