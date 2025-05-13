# Time Complexity O(v + e) where v is vertices and e edges
# Space Complexity O(v)

def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)
    print(node)  # or process node

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)

            for neighbor in reversed(graph[node]):
                stack.append(neighbor)
