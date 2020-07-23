from collections import defaultdict, deque


def desopo(graph):
    v = len(graph)
    adj = defaultdict(list)
    for i in range(v):
        for j in range(i + 1, v):
            if graph[i][j] != 0:
                adj[i].append([graph[i][j], j])
                adj[j].append([graph[i][j], i])
    q = deque([])
    distance = [float('inf')] * v
    is_in_queue = [False] * v
    source = 0
    distance = 0
    q.append(source)
    is_in_queue = True
    while q:
        u = q.popleft()
        is_in_queue[u] = False
        for e in adj[u]:
            if distance[e[1]] > distance[u] + e[0]:
                distance[e[1]] = distance[u] + e[0]
                if not is_in_queue[e[1]]:
                    if distance[e[1]] == float('inf'):
                        q.append(e[1])
                    else:
                        q.appendleft(e[1])
                    is_in_queue[e[1]] = True
    return distance


if __name__ == "__main__":
    graph = [[0, 4, 0, 0, 8],
             [0, 0, 8, 0, 11],
             [0, 8, 0, 2, 0],
             [0, 0, 2, 0, 1],
             [8, 11, 0, 1, 0]]
    print(desopo(graph))