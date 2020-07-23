from collections import defaultdict

n, m = map(int, list(input().split(" "))[:2])
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, list(input().split(" "))[:2])
    graph[a].append(b)
can_go = {}


def DFS(visited, node=1):
    visited[node], temp = True, 0
    if node == n:
        visited[node] = False
        return temp + 1
    for a in graph[node]:
        if not visited[a]:
            temp = DFS(visited, a)
    visited[node] = False
    can_go[node] = True if temp > 0 else False
    return temp


print(DFS([False] * (n + 1)))
print(can_go)