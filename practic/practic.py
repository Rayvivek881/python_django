import sys
from collections import defaultdict
sys.setrecursionlimit(50000)
n, m = map(int, list(input().split(" "))[:2])
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, list(input().split(" "))[:2])
    graph[a].append(b)
can_go = {}


def makarray(visited, node=1):
    visited[node], temp = True, 0
    if node == n:
        can_go[node] = True
        visited[node] = False
        return temp + 1
    for a in graph[node]:
        if not visited[a]:
            temp = makarray(visited, a)
    visited[node] = False
    can_go[node] = True if temp > 0 else False
    return temp


def DFS(visited, node=1):
    visited[node], temp = True, 0
    if node == n:
        visited[node] = False
        return 1
    for a in graph[node]:
        if not visited[a]:
            temp += (DFS(visited, a) % (10 ** 9))
        elif can_go[a]:
            return -float('inf')
    visited[node] = False
    return temp % (10 ** 9)


makarray([False] * (n + 1))
t = DFS([False] * (n + 1))
print(t % int(10e9) if t > 0 else "INFINITE PATHS")