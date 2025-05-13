# Time Complexity O(v + e) where v is vertices and e edges
# Space Complexity O(v)

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)

            for neighbor in graph[node]:
                queue.append(neighbor)
