def dfs_iterative(graph, start):
    stack, path = [start], []
    while stack:
        vertex = stack.pop()
        if vertex not in path:
            path.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in path:
                stack.append(neighbor)
    return path


adjacency_matrix = {1: [2, 3], 2: [1, 4, 5],
                    3: [1, 6, 7], 4: [2], 5: [2], 6: [3], 7: [3]}
print(" ".join(map(str, dfs_iterative(adjacency_matrix, 1))))