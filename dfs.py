graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

def dfs(start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            break

        for neighbor in reversed(graph[node]):
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = node
                stack.append(neighbor)

    if goal not in visited:
        print("Path not found")
        return

    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    print("Path found:", " -> ".join(path))

dfs('A', 'G')