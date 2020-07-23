import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

n, weight = int(input()), list(map(int, input().split(" ")))
sam, graph, ans = sum(weight), defaultdict(list), [float('inf')]
for _ in range(n - 1):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)


def DFS(visited, node=1):
    visited[node], temp = True, 0
    for a in graph[node]:
        if not visited[a]:
            t = DFS(visited, a)
            ans[0], temp = min(ans[0], abs(sam - (2 * t))), temp + t
    return weight[node - 1] + temp


DFS([False] * (n + 1))
print(ans[0])
