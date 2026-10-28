import heapq

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 3, 'E': 2},
    'C': {'A': 3, 'F': 2, 'G': 3},
    'D': {'B': 3, 'H': 3},
    'E': {'B': 2, 'H': 4},
    'F': {'C': 2, 'H': 3},
    'G': {'C': 3, 'H': 2},
    'H': {'D': 3, 'E': 4, 'F': 3, 'G': 2}
}

h = {
    'A': 5, 'B': 4, 'C': 3, 'D': 3,
    'E': 3, 'F': 2, 'G': 1, 'H': 0
}

def astar(start, goal):
    queue = []
    count = 0

    heapq.heappush(queue, (h[start], count, start, [start], 0))
    best_cost = {start: 0}

    while queue:
        f, order, node, path, g = heapq.heappop(queue)

        if node == goal:
            return path, g

        if g > best_cost[node]:
            continue

        for neighbor, cost in graph[node].items():
            new_g = g + cost

            if new_g < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_g
                count += 1
                new_f = new_g + h[neighbor]

                heapq.heappush(
                    queue,
                    (new_f, count, neighbor,
                     path + [neighbor], new_g)
                )

    return None, 0

path, cost = astar('A', 'H')

if path:
    print("Path found:", " -> ".join(path))
    print("Total path cost:", cost)
else:
    print("Path not found")